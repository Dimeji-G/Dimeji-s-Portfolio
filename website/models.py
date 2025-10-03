from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Applications'),
        ('tools', 'Tools & Utilities'),
        ('GUI', 'Python GUIs'),
        ('desktop', 'Desktop Applications'),
        ('automation', 'Automation Scripts'),
        ('api', 'API Development'),
        ('data', 'Data Analysis'),
    ]
    
    # Basic Information
    title = models.CharField(max_length=200, help_text="Project title")
    slug = models.SlugField(max_length=250, unique=True, blank=True, help_text="URL-friendly version of title")
    description = models.TextField(help_text="Detailed project description")
    short_description = models.CharField(max_length=300, blank=True, help_text="Brief summary for cards")
    
    # Project Classification
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    featured = models.BooleanField(default=False, help_text="Mark as featured project")
    
    # Links
    github_url = models.URLField(help_text="GitHub repository URL")
    live_url = models.URLField(blank=True, null=True, help_text="Live demo/deployment URL")
    documentation_url = models.URLField(blank=True, null=True, help_text="Documentation URL")
    
    # Media
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Project screenshot or logo")
    thumbnail = models.ImageField(upload_to='projects/thumbnails/', blank=True, null=True, help_text="Thumbnail image")
    
    # Technical Details
    technologies = models.TextField(help_text="Comma-separated list of technologies used (e.g., Python, Django, React)")
    
    # Metrics & Status
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active Development'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
        ('on_hold', 'On Hold'),
    ], default='completed')
    
    start_date = models.DateField(blank=True, null=True, help_text="Project start date")
    end_date = models.DateField(blank=True, null=True, help_text="Project completion date")
    
    # SEO & Display
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    visible = models.BooleanField(default=True, help_text="Show on website")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', '-featured', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.short_description:
            # Create short description from main description if not provided
            self.short_description = self.description[:250] + '...' if len(self.description) > 250 else self.description
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('website:project_detail', kwargs={'slug': self.slug})
    
    def get_technologies_list(self):
        """Return technologies as a list"""
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]
    
    @property
    def is_featured(self):
        return self.featured
    
    @property
    def has_live_demo(self):
        return bool(self.live_url)


class ProjectImage(models.Model):
    """Additional images for projects (gallery)"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.project.title} - Image {self.order}"


class Technology(models.Model):
    """Technology/Skill model for better organization"""
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50, choices=[
        ('language', 'Programming Language'),
        ('framework', 'Framework'),
        ('library', 'Library'),
        ('database', 'Database'),
        ('tool', 'Tool'),
        ('platform', 'Platform'),
        ('service', 'Service'),
    ], default='language')
    icon = models.CharField(max_length=100, blank=True, help_text="Font Awesome icon class (e.g., fab fa-python)")
    color = models.CharField(max_length=7, blank=True, help_text="Hex color code (e.g., #3776ab)")
    website = models.URLField(blank=True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Technologies'
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, choices=[
        ('project', 'Project Collaboration'),
        ('freelance', 'Freelance Opportunity'),
        ('internship', 'Internship Inquiry'),
        ('question', 'General Question'),
        ('other', 'Other'),
    ])
    message = models.TextField()
    newsletter = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
