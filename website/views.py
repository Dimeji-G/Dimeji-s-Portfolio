from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Technology, Contact
import json


def home(request):
    # Get featured projects for the homepage
    featured_projects = Project.objects.filter(featured=True, visible=True)[:3]
    context = {
        'featured_projects': featured_projects,
    }
    return render(request, 'website/index.html', context)


def about(request):
    # Get technologies for skills section
    technologies = Technology.objects.all()
    context = {
        'technologies': technologies,
    }
    return render(request, 'website/about.html', context)


def projects(request):
    # Get all visible projects
    all_projects = Project.objects.filter(visible=True)
    
    # Filter by category if specified
    category = request.GET.get('category')
    if category and category != 'all':
        if category == 'featured':
            all_projects = all_projects.filter(featured=True)
        else:
            all_projects = all_projects.filter(category=category)
    
    context = {
        'projects': all_projects,
    }
    return render(request, 'website/projects.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, visible=True)
    related_projects = Project.objects.filter(
        category=project.category, 
        visible=True
    ).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'website/project_detail.html', context)


def contact(request):
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        newsletter = request.POST.get('newsletter') == 'on'
        
        # Save to database
        contact_submission = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            newsletter=newsletter
        )
        
        # Send email notification (optional)
        try:
            send_mail(
                subject=f'Portfolio Contact: {subject}',
                message=f'From: {name} ({email})\n\nMessage:\n{message}',
                from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@dimroid.com',
                recipient_list=[settings.CONTACT_EMAIL if hasattr(settings, 'CONTACT_EMAIL') else 'dimeji@dimroid.com'],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Failed to send email: {e}")
        
        messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
        return render(request, 'website/contact.html')
    
    return render(request, 'website/contact.html')


def projects_api(request):
    """API endpoint to get projects data for JavaScript"""
    projects = Project.objects.filter(visible=True)
    
    # Filter by category if specified
    category = request.GET.get('category')
    if category and category != 'all':
        if category == 'featured':
            projects = projects.filter(featured=True)
        else:
            projects = projects.filter(category=category)
    
    projects_data = []
    for project in projects:
        project_dict = {
            'title': project.title,
            'description': project.description,
            'tags': project.get_technologies_list(),
            'github': project.github_url,
            'live': project.live_url,
            'category': project.category,
            'featured': project.featured,
            'image': project.image.url if project.image else None,
            'slug': project.slug,
        }
        projects_data.append(project_dict)
    
    return JsonResponse({'projects': projects_data})
