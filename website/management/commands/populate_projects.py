from django.core.management.base import BaseCommand
from website.models import Project, Technology


class Command(BaseCommand):
    help = 'Populate database with initial project data'

    def handle(self, *args, **options):
        self.stdout.write('Creating initial project data...')
        
        # Create some technologies first
        technologies_data = [
            {'name': 'Python', 'category': 'language', 'icon': 'fab fa-python', 'color': '#3776ab'},
            {'name': 'Django', 'category': 'framework', 'icon': 'fab fa-python', 'color': '#092e20'},
            {'name': 'JavaScript', 'category': 'language', 'icon': 'fab fa-js-square', 'color': '#f7df1e'},
            {'name': 'React', 'category': 'library', 'icon': 'fab fa-react', 'color': '#61dafb'},
            {'name': 'Next.js', 'category': 'framework', 'icon': 'fab fa-js', 'color': '#000000'},
            {'name': 'TypeScript', 'category': 'language', 'icon': 'fab fa-js', 'color': '#3178c6'},
            {'name': 'PostgreSQL', 'category': 'database', 'icon': 'fas fa-database', 'color': '#336791'},
            {'name': 'HTML5', 'category': 'language', 'icon': 'fab fa-html5', 'color': '#e34f26'},
            {'name': 'CSS3', 'category': 'language', 'icon': 'fab fa-css3-alt', 'color': '#1572b6'},
        ]
        
        for tech_data in technologies_data:
            tech, created = Technology.objects.get_or_create(
                name=tech_data['name'],
                defaults=tech_data
            )
            if created:
                self.stdout.write(f'Created technology: {tech.name}')
        
        # Project data based on your existing projects
        projects_data = [
            {
                'title': 'Suncore',
                'description': 'An open-source offline web-based audio processor with features like nightcore effect, reverb, and bass boost. Built with modern web technologies for optimal performance.',
                'category': 'web',
                'featured': True,
                'github_url': 'https://github.com/Dimeji-G/suncore',
                'live_url': 'https://suncore.vercel.app',
                'technologies': 'Next.js, TypeScript, Audio Processing, Web Audio API, Offline',
                'status': 'completed',
                'order': 1,
            },
            {
                'title': 'Flashy',
                'description': 'Modern offline flashcard application designed for students. Features spaced repetition, progress tracking, and offline functionality for seamless studying.',
                'category': 'web',
                'featured': True,
                'github_url': 'https://github.com/Dimeji-G/flashy',
                'live_url': 'https://flashy-byigitt.vercel.app',
                'technologies': 'Next.js, TypeScript, PWA, Study Tools, Flashcards',
                'status': 'completed',
                'order': 2,
            },
            {
                'title': 'OneTimeLink',
                'description': 'Secure one-time-link generator for file sharing. Features encryption, expiration times, and secure file uploads with automatic cleanup.',
                'category': 'tools',
                'featured': False,
                'github_url': 'https://github.com/Dimeji-G/onetimelink',
                'technologies': 'Next.js, TypeScript, File Upload, Security, Encryption',
                'status': 'completed',
                'order': 3,
            },
            {
                'title': 'Portfolio Website',
                'description': 'My personal portfolio website built with Django, featuring modern design, responsive layout, and dynamic content management.',
                'category': 'web',
                'featured': True,
                'github_url': 'https://github.com/Dimeji-G/portfolio',
                'live_url': 'https://dimroid.com',
                'technologies': 'Django, Python, HTML5, CSS3, Responsive',
                'status': 'active',
                'order': 4,
            },
            {
                'title': 'Inventory Automation System',
                'description': 'Python automation system for retail inventory management. Saves 100+ hours monthly with automated supplier tracking and price optimization.',
                'category': 'tools',
                'featured': True,
                'github_url': 'https://github.com/Dimeji-G/inventory-automation',
                'technologies': 'Python, Automation, Data Processing, Business Logic',
                'status': 'completed',
                'order': 5,
            },
            {
                'title': 'Web Scraping Suite',
                'description': 'Comprehensive web scraping toolkit with support for multiple sites, data processing, and automated reporting systems.',
                'category': 'tools',
                'featured': False,
                'github_url': 'https://github.com/Dimeji-G/scraping-suite',
                'technologies': 'Python, Selenium, BeautifulSoup, Data Mining',
                'status': 'completed',
                'order': 6,
            },
            {
                'title': 'Django E-commerce Platform',
                'description': 'Full-featured e-commerce platform with payment processing, inventory management, and customer analytics built with Django.',
                'category': 'web',
                'featured': False,
                'github_url': 'https://github.com/Dimeji-G/django-ecommerce',
                'technologies': 'Django, Python, PostgreSQL, Stripe, E-commerce',
                'status': 'completed',
                'order': 7,
            },
            {
                'title': 'API Integration Framework',
                'description': 'Reusable framework for integrating multiple third-party APIs with automatic retry logic, rate limiting, and error handling.',
                'category': 'tools',
                'featured': False,
                'github_url': 'https://github.com/Dimeji-G/api-framework',
                'technologies': 'Python, API, Framework, Integration',
                'status': 'completed',
                'order': 8,
            },
            {
                'title': 'Data Analysis Dashboard',
                'description': 'Interactive dashboard for business data analysis with real-time charts, filtering, and export capabilities.',
                'category': 'web',
                'featured': False,
                'github_url': 'https://github.com/Dimeji-G/data-dashboard',
                'technologies': 'Django, Chart.js, Data Analysis, Dashboard',
                'status': 'completed',
                'order': 9,
            },
            {
                'title': 'Automated Report Generator',
                'description': 'Python tool for generating automated business reports from multiple data sources with PDF and Excel export.',
                'category': 'tools',
                'featured': False,
                'github_url': 'https://github.com/Dimeji-G/report-generator',
                'technologies': 'Python, Automation, Reporting, PDF Generation',
                'status': 'completed',
                'order': 10,
            },
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'Created project: {project.title}')
            else:
                self.stdout.write(f'Project already exists: {project.title}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with project data!')
        )