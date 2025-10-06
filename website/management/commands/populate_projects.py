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
        
        # Replace the projects_data below with expanded versions from projects.md
        projects_data = [
            {
                'title': 'Nigeria Map Game',
                'description': (
                    'An educational desktop application to help users learn the 36 states of Nigeria. '
                    'Features an interactive map, state quizzes, scoring, and progressive difficulty. '
                    'Built as a lightweight desktop app for offline use.'
                ),
                'category': 'education',
                'featured': False,
                'github_url': '',
                'live_url': '',
                'technologies': 'Python, Tkinter, SQLite, Desktop',
                'status': 'completed',
                'order': 1,
            },
            {
                'title': 'Automated Email System for NGO Volunteer Management',
                'description': (
                    'Python-powered email automation system created to manage communications with NGO volunteers. '
                    'Supports personalized templates, scheduled sends, batching, and logging to reduce manual effort '
                    'and improve volunteer engagement.'
                ),
                'category': 'automation',
                'featured': False,
                'github_url': '',
                'live_url': '',
                'technologies': 'Python, smtplib, email, Automation, Logging',
                'status': 'completed',
                'order': 2,
            },
            {
                'title': 'Vocabulary Web Learning Tool',
                'description': (
                    'An interactive glossary and flashcard web tool designed to master 1000+ vocabulary words. '
                    'Implements spaced repetition concepts to reinforce learning and tracks progress over time. '
                    'Accessible as a light web app with offline-ready behavior where possible.'
                ),
                'category': 'web',
                'featured': False,
                'github_url': '',
                'live_url': 'https://glossary.dimroid.com',
                'technologies': 'Python, HTML5, CSS3, JavaScript, Flashcards, Spaced Repetition',
                'status': 'active',
                'order': 3,
            },
            {
                'title': 'Blog Application with Django',
                'description': (
                    'A full-featured blog system built with Django including categories, tagging for post recommendations, '
                    'latest posts view, and admin-managed content. Designed for performance and easy content workflows; '
                    'deployed with PostgreSQL and optionally hosted on Azure.'
                ),
                'category': 'web',
                'featured': True,
                'github_url': '',
                'live_url': 'https://dimroid.com/blog',
                'technologies': 'Django, Python, PostgreSQL, HTML5, CSS3, Azure',
                'status': 'completed',
                'order': 4,
            },
            {
                'title': 'Dimeji\'s Personal Portfolio',
                'description': (
                    'Personal portfolio site showcasing projects, blog posts, and contact information for the founder. '
                    'Focuses on clean design, responsiveness, and easy content updates.'
                ),
                'category': 'web',
                'featured': True,
                'github_url': '',
                'live_url': 'https://dimeji.tech',
                'technologies': 'Django, HTML5, CSS3, JavaScript, Responsive Design',
                'status': 'active',
                'order': 5,
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