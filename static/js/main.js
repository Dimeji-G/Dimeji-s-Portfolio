// Main JavaScript file for portfolio
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initTheme();
    initNavigation();
    initMobileMenu();
    initScrollAnimations();
    initProjectFilters();
    initSpotifyWidget();
    initContactForm();
    initSmoothScrolling();
    initProfileImage();
    initParticles();
});

// Theme Management
function initTheme() {
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = themeToggle.querySelector('i');
    
    // Get saved theme or default to dark
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);
    
    themeToggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    });
    
    function setTheme(theme) {
        // Temporarily disable transitions to prevent flickering
        document.documentElement.style.setProperty('--transition', 'none');
        
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        
        // Update icon
        if (theme === 'dark') {
            themeIcon.className = 'fas fa-sun';
        } else {
            themeIcon.className = 'fas fa-moon';
        }
        
        // Re-enable transitions after a short delay
        setTimeout(() => {
            document.documentElement.style.removeProperty('--transition');
        }, 50);
    }
}

// Navigation
function initNavigation() {
    const navbar = document.getElementById('navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Handle scroll effect on navbar
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            if (document.documentElement.getAttribute('data-theme') === 'dark') {
                navbar.style.background = 'rgba(15, 23, 42, 0.95)';
            }
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.8)';
            if (document.documentElement.getAttribute('data-theme') === 'dark') {
                navbar.style.background = 'rgba(15, 23, 42, 0.8)';
            }
        }
    });
    
    // Handle active nav link
    window.addEventListener('scroll', () => {
        let current = '';
        const sections = document.querySelectorAll('section');
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
}

// Mobile Menu
function initMobileMenu() {
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
    const mobileMenuClose = document.getElementById('mobile-menu-close');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');
    
    mobileMenuToggle.addEventListener('click', () => {
        mobileMenuOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    });
    
    mobileMenuClose.addEventListener('click', closeMobileMenu);
    mobileMenuOverlay.addEventListener('click', (e) => {
        if (e.target === mobileMenuOverlay) {
            closeMobileMenu();
        }
    });
    
    mobileNavLinks.forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });
    
    function closeMobileMenu() {
        mobileMenuOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }
}

// Scroll Animations
function initScrollAnimations() {
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    animateElements.forEach(element => {
        observer.observe(element);
    });
}

// Project Filters
function initProjectFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectsGrid = document.getElementById('projects-grid');
    
    // Project data
    const projects = [
        {
            title: "Suncore",
            description: "An open-source offline web-based audio processor with features like nightcore effect, reverb, and bass boost.",
            tags: ["Next.js", "TypeScript", "Audio Processing", "Web Audio API"],
            github: "https://github.com/Dimeji-G/suncore",
            live: "https://suncore.vercel.app",
            category: "web"
        },
        {
            title: "Flashy",
            description: "Modern offline flashcard application for students to use.",
            tags: ["Next.js", "TypeScript", "Offline", "Study", "Flashcards"],
            github: "https://github.com/Dimeji-G/flashy",
            live: "https://flashy-byigitt.vercel.app",
            category: "web"
        },
        {
            title: "OneTimeLink",
            description: "One-time-link generator for uploading files.",
            tags: ["Next.js", "TypeScript", "File Upload", "One-Time Links"],
            github: "https://github.com/Dimeji-G/onetimelink",
            category: "tools"
        },
        {
            title: "URL Shortener",
            description: "A simple but effective URL shortener service built with JavaScript.",
            tags: ["JavaScript", "Node.js", "Express", "MongoDB"],
            github: "https://github.com/Dimeji-G/shrtn",
            category: "tools"
        },
        {
            title: "Portfolio Website",
            description: "My personal portfolio website built with Next.js 15, TypeScript, and Tailwind CSS.",
            tags: ["Next.js", "TypeScript", "Tailwind CSS", "Shadcn/UI"],
            github: "https://github.com/Dimeji-G/portfolio",
            live: "https://portfolio.bayburt.lu",
            category: "web"
        },
        {
            title: "Cankaya Chat",
            description: "Real-time chat application for students.",
            tags: ["React", "Socket.io", "Node.js", "MongoDB"],
            github: "https://github.com/Dimeji-G/cankaya-chat",
            category: "web"
        },
        {
            title: "Smart Move",
            description: "Intelligent moving and logistics platform.",
            tags: ["React", "TypeScript", "Node.js", "PostgreSQL"],
            github: "https://github.com/Dimeji-G/smart-move",
            category: "web"
        },
        {
            title: "Star Sales",
            description: "E-commerce platform with advanced analytics.",
            tags: ["Next.js", "TypeScript", "Stripe", "Prisma"],
            github: "https://github.com/Dimeji-G/star-sales",
            category: "web"
        }
    ];
    
    // Render projects
    function renderProjects(projectsToShow = projects) {
        projectsGrid.innerHTML = '';
        
        projectsToShow.forEach((project, index) => {
            const projectCard = createProjectCard(project, index);
            projectsGrid.appendChild(projectCard);
        });
        
        // Animate new cards
        setTimeout(() => {
            const newCards = projectsGrid.querySelectorAll('.project-card');
            newCards.forEach((card, index) => {
                setTimeout(() => {
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                }, index * 100);
            });
        }, 50);
    }
    
    function createProjectCard(project, index) {
        const card = document.createElement('div');
        card.className = 'project-card animate-on-scroll';
        card.style.animationDelay = `${index * 0.1}s`;
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease';
        
        card.innerHTML = `
            <div class="project-image">
                <i class="fas fa-code"></i>
            </div>
            <div class="project-content">
                <h3 class="project-title">${project.title}</h3>
                <p class="project-description">${project.description}</p>
                <div class="project-tags">
                    ${project.tags.map(tag => `<span class="project-tag">${tag}</span>`).join('')}
                </div>
                <div class="project-links">
                    <a href="${project.github}" target="_blank" rel="noopener noreferrer" class="project-link">
                        <i class="fab fa-github"></i>
                        GitHub
                    </a>
                    ${project.live ? `
                        <a href="${project.live}" target="_blank" rel="noopener noreferrer" class="project-link">
                            <i class="fas fa-external-link-alt"></i>
                            Live Demo
                        </a>
                    ` : ''}
                </div>
            </div>
        `;
        
        return card;
    }
    
    // Filter functionality
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            const filter = button.getAttribute('data-filter');
            
            if (filter === 'all') {
                renderProjects(projects);
            } else {
                const filteredProjects = projects.filter(project => project.category === filter);
                renderProjects(filteredProjects);
            }
        });
    });
    
    // Initial render
    renderProjects();
}

// Spotify Widget
function initSpotifyWidget() {
    const spotifyWidget = document.getElementById('spotify-widget');
    
    // Simulate Spotify API call (replace with actual API call)
    setTimeout(() => {
        // Mock data - replace with actual Spotify API
        const mockTrack = {
            name: "Currently not playing",
            artist: "Spotify",
            image: null,
            isPlaying: false
        };
        
        updateSpotifyWidget(mockTrack);
    }, 2000);
    
    function updateSpotifyWidget(track) {
        if (track.isPlaying && track.name !== "Currently not playing") {
            spotifyWidget.innerHTML = `
                <div class="spotify-track">
                    ${track.image ? `<img src="${track.image}" alt="${track.name}">` : '<div class="track-placeholder"><i class="fab fa-spotify"></i></div>'}
                    <div class="track-info">
                        <h4>${track.name}</h4>
                        <p>by ${track.artist}</p>
                    </div>
                </div>
            `;
        } else {
            spotifyWidget.innerHTML = `
                <div class="spotify-loading">
                    <i class="fab fa-spotify"></i>
                    <span>Not playing</span>
                </div>
            `;
        }
    }
}

// Contact Form
function initContactForm() {
    const contactForm = document.getElementById('contact-form');
    
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(contactForm);
        const data = {
            name: formData.get('name'),
            email: formData.get('email'),
            message: formData.get('message')
        };
        
        // Get submit button
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        
        // Show loading state
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
        submitBtn.disabled = true;
        
        try {
            // Simulate form submission (replace with actual endpoint)
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            // Success state
            submitBtn.innerHTML = '<i class="fas fa-check"></i> Message Sent!';
            submitBtn.style.background = '#000000';
            
            // Reset form
            contactForm.reset();
            
            // Show success message
            showNotification('Message sent successfully!', 'success');
            
        } catch (error) {
            // Error state
            submitBtn.innerHTML = '<i class="fas fa-times"></i> Failed to Send';
            submitBtn.style.background = '#333333';
            
            showNotification('Failed to send message. Please try again.', 'error');
        }
        
        // Reset button after 3 seconds
        setTimeout(() => {
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
            submitBtn.style.background = '';
        }, 3000);
    });
}

// Smooth Scrolling
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 80; // Account for navbar height
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Notification System
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => notification.remove());
    
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${type === 'success' ? '#000000' : type === 'error' ? '#333333' : '#000000'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        z-index: 1000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        max-width: 300px;
    `;
    
    notification.innerHTML = `
        <div style="display: flex; align-items: center; gap: 0.5rem;">
            <i class="fas fa-${type === 'success' ? 'check' : type === 'error' ? 'times' : 'info'}"></i>
            <span>${message}</span>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 5000);
}

// Utility Functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// GitHub API for project stats (optional enhancement)
async function fetchGitHubStats(repo) {
    try {
        const response = await fetch(`https://api.github.com/repos/byigitt/${repo}`);
        const data = await response.json();
        return {
            stars: data.stargazers_count,
            forks: data.forks_count,
            language: data.language
        };
    } catch (error) {
        console.error('Error fetching GitHub stats:', error);
        return null;
    }
}

// Performance optimization
window.addEventListener('load', () => {
    // Remove loading states
    document.body.classList.add('loaded');
    
    // Lazy load images
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
});

// Error handling
window.addEventListener('error', (e) => {
    console.error('JavaScript error:', e.error);
});

// Service Worker registration (optional for PWA features)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}

// Profile Image Handler
function initProfileImage() {
    const profileImg = document.getElementById('profile-img');
    const profilePlaceholder = document.getElementById('profile-placeholder');
    
    if (profileImg && profilePlaceholder) {
        // Initially show placeholder
        profileImg.style.display = 'none';
        profilePlaceholder.style.display = 'flex';
        
        // Try to load the image
        profileImg.onload = function() {
            profileImg.style.display = 'block';
            profilePlaceholder.style.display = 'none';
        };
        
        // If image fails to load, keep placeholder
        profileImg.onerror = function() {
            profileImg.style.display = 'none';
            profilePlaceholder.style.display = 'flex';
        };
        
        // Force check if image is already loaded (cached)
        if (profileImg.complete && profileImg.naturalHeight !== 0) {
            profileImg.style.display = 'block';
            profilePlaceholder.style.display = 'none';
        }
    }
}

// Particles.js Spider Web Effect
function initParticles() {
    if (typeof particlesJS !== 'undefined') {
        particlesJS('particles-js', {
            particles: {
                number: {
                    value: 50,
                    density: {
                        enable: true,
                        value_area: 800
                    }
                },
                color: {
                    value: getComputedStyle(document.documentElement).getPropertyValue('--accent-primary').trim() || '#000000'
                },
                shape: {
                    type: 'circle',
                    stroke: {
                        width: 0,
                        color: '#000000'
                    }
                },
                opacity: {
                    value: 0.5,
                    random: false,
                    anim: {
                        enable: false,
                        speed: 1,
                        opacity_min: 0.1,
                        sync: false
                    }
                },
                size: {
                    value: 3,
                    random: true,
                    anim: {
                        enable: false,
                        speed: 40,
                        size_min: 0.1,
                        sync: false
                    }
                },
                line_linked: {
                    enable: true,
                    distance: 150,
                    color: getComputedStyle(document.documentElement).getPropertyValue('--accent-primary').trim() || '#000000',
                    opacity: 0.4,
                    width: 1
                },
                move: {
                    enable: true,
                    speed: 6,
                    direction: 'none',
                    random: false,
                    straight: false,
                    out_mode: 'out',
                    bounce: false,
                    attract: {
                        enable: false,
                        rotateX: 600,
                        rotateY: 1200
                    }
                }
            },
            interactivity: {
                detect_on: 'canvas',
                events: {
                    onhover: {
                        enable: true,
                        mode: 'grab'
                    },
                    onclick: {
                        enable: true,
                        mode: 'push'
                    },
                    resize: true
                },
                modes: {
                    grab: {
                        distance: 140,
                        line_linked: {
                            opacity: 1
                        }
                    },
                    bubble: {
                        distance: 400,
                        size: 40,
                        duration: 2,
                        opacity: 8,
                        speed: 3
                    },
                    repulse: {
                        distance: 200,
                        duration: 0.4
                    },
                    push: {
                        particles_nb: 4
                    },
                    remove: {
                        particles_nb: 2
                    }
                }
            },
            retina_detect: true
        });

        // Update particles color when theme changes
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', () => {
                setTimeout(() => {
                    const newColor = getComputedStyle(document.documentElement).getPropertyValue('--accent-primary').trim() || '#000000';
                    if (window.pJSDom && window.pJSDom[0] && window.pJSDom[0].pJS) {
                        window.pJSDom[0].pJS.particles.color.value = newColor;
                        window.pJSDom[0].pJS.particles.line_linked.color = newColor;
                        window.pJSDom[0].pJS.fn.particlesRefresh();
                    }
                }, 100);
            });
        }
    }
}