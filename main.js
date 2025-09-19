<script>
        // Loading screen
        window.addEventListener('load', () => {
            const loadingOverlay = document.getElementById('loadingOverlay');
            setTimeout(() => {
                loadingOverlay.style.opacity = '0';
                setTimeout(() => {
                    loadingOverlay.style.display = 'none';
                }, 500);
            }, 1000);
        });
        // Counter Animation
        function animateCounter(element, target, duration = 1200) {
            const start = 0;
            const increment = target / (duration / 16);
            let current = start;
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    element.textContent = target;
                    clearInterval(timer);
                } else {
                    element.textContent = Math.floor(current * 10) / 10;
                }
            }, 16);
        }
        // Scroll Reveal Animation - Optimized
        const observerOptions = {
            threshold: 0.15,
            rootMargin: '0px 0px -80px 0px'
        };
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('visible')) {
                    // Add small delay to prevent overlapping animations
                    setTimeout(() => {
                        entry.target.classList.add('visible');
                    }, 100);
                    // Animate counters when dashboard comes into view
                    const counters = entry.target.querySelectorAll('.counter');
                    counters.forEach(counter => {
                        if (!counter.classList.contains('animated')) {
                            counter.classList.add('animated');
                            const target = parseFloat(counter.getAttribute('data-target'));
                            setTimeout(() => animateCounter(counter, target), 300);
                        }
                    });
                }
            });
        }, observerOptions);
        // Observe all scroll reveal elements
        document.addEventListener('DOMContentLoaded', () => {
            // Initialize counters after page load
            setTimeout(() => {
                const counters = document.querySelectorAll('.counter');
                counters.forEach(counter => {
                    const target = parseFloat(counter.getAttribute('data-target'));
                    animateCounter(counter, target);
                });
            }, 2000);
            // Observe sections for scroll animations
            const scrollElements = document.querySelectorAll('.scroll-reveal, .dashboard-mockup');
            scrollElements.forEach(el => observer.observe(el));
            // Smooth scrolling for anchor links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    const targetId = this.getAttribute('href');
                    const target = document.querySelector(targetId);
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });
            // Navbar scroll effect
            let lastScrollTop = 0;
            const navbar = document.querySelector('.navbar');
            window.addEventListener('scroll', () => {
                let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                if (scrollTop > lastScrollTop && scrollTop > 100) {
                    navbar.style.transform = 'translateY(-100%)';
                } else {
                    navbar.style.transform = 'translateY(0)';
                }
                lastScrollTop = scrollTop;
            });
            // Logo click to scroll to top
            document.getElementById('logoLink').addEventListener('click', function(e) {
                e.preventDefault();
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
            // Mobile menu toggle
            const mobileMenuBtn = document.getElementById('mobileMenuBtn');
            const navLinks = document.getElementById('navLinks');
            mobileMenuBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                navLinks.classList.toggle('active');
            });
            // Close mobile menu when clicking a link (but preserve functionality)
            document.querySelectorAll('.nav-links a').forEach(link => {
                link.addEventListener('click', function(e) {
                    // Only close menu on mobile if it's actually open
                    if (window.innerWidth <= 768 && navLinks.classList.contains('active')) {
                        navLinks.classList.remove('active');
                    }
                });
            });
            // Handle window resize to reset menu state
            window.addEventListener('resize', function() {
                if (window.innerWidth > 768) {
                    navLinks.classList.remove('active');
                }
            });
