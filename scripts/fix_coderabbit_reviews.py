import os
import glob
import re

# Use relative paths for better portability
blog_dir = 'cbam-blog'

BAD_BLOCK = '''            .mobile-only-icon { display: none; }
            @media (max-width: 768px) { .mobile-only-icon { display: inline-block !important; } }
            .toc-title i {'''

GOOD_BLOCK = '''            .mobile-only-icon { display: none; }
            .toc-title i {'''

# Find all HTML files in the blog directory
for filepath in glob.glob(os.path.join(blog_dir, '*.html')):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # 1. Fix CSS nesting issue
        if BAD_BLOCK in content:
            content = content.replace(BAD_BLOCK, GOOD_BLOCK)
            changed = True
            
        # Add the proper mobile-only-icon media query rule where it belongs if it's not present globally
        # We will insert it inside the @media (max-width: 768px) block correctly.
        # It's cleaner to just replace the first instance of .toc-sidebar { in the 768px query.
        FIXED_MOBILE_ICON_CSS = '''            .mobile-only-icon { display: inline-block !important; }
            .toc-sidebar {'''
        if FIXED_MOBILE_ICON_CSS not in content and '.toc-sidebar {' in content and '@media (max-width: 768px)' in content:
            # Let's cleanly inject it before .toc-sidebar { inside the mobile query
            content = content.replace('        @media (max-width: 768px) {\n            .toc-sidebar {', '        @media (max-width: 768px) {\n' + FIXED_MOBILE_ICON_CSS)
            changed = True

        # 2. Add accessibility and keyboard support to TOC title
        bad_title_1 = '<div class="toc-title" id="mobileTocToggle">ON THIS PAGE <i class="fas fa-chevron-down mobile-only-icon" style="display:none;"></i></div>'
        bad_title_2 = '<div class="toc-title" id="mobileTocToggle">ON THIS PAGE <i class="fas fa-chevron-down mobile-only-icon"></i></div>'
        good_title = '<div class="toc-title" id="mobileTocToggle" role="button" aria-expanded="false" tabindex="0" aria-label="Toggle Table of Contents">ON THIS PAGE <i class="fas fa-chevron-down mobile-only-icon"></i></div>'
        
        if bad_title_1 in content:
            content = content.replace(bad_title_1, good_title)
            changed = True
        elif bad_title_2 in content:
            content = content.replace(bad_title_2, good_title)
            changed = True

        # 3. Fix JS resize bug
        bad_js = '''        // Mobile TOC Toggle
        const tocToggle = document.getElementById('mobileTocToggle');
        const tocList = document.querySelector('.toc-list');
        
        if (tocToggle && tocList && window.innerWidth <= 768) {
            tocToggle.addEventListener('click', function() {
                tocList.classList.toggle('active');
                this.classList.toggle('expanded');
            });
            
            // Close TOC when a link is clicked on mobile
            const tocLinks = document.querySelectorAll('.toc-list a');
            tocLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth <= 768) {
                        tocList.classList.remove('active');
                        tocToggle.classList.remove('expanded');
                    }
                });
            });
        }'''
        
        good_js = '''        // Mobile TOC Toggle
        const tocToggle = document.getElementById('mobileTocToggle');
        const tocList = document.querySelector('.toc-list');
        
        if (tocToggle && tocList) {
            const toggleMenu = () => {
                if (window.innerWidth <= 768) {
                    const isActive = tocList.classList.toggle('active');
                    tocToggle.classList.toggle('expanded');
                    tocToggle.setAttribute('aria-expanded', String(isActive));
                }
            };

            tocToggle.addEventListener('click', toggleMenu);
            tocToggle.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    toggleMenu();
                }
            });
            
            // Close TOC when a link is clicked on mobile
            const tocLinks = document.querySelectorAll('.toc-list a');
            tocLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth <= 768) {
                        tocList.classList.remove('active');
                        tocToggle.classList.remove('expanded');
                        tocToggle.setAttribute('aria-expanded', 'false');
                    }
                });
            });

            // Reset state on resize to handle rotation/resizing gracefully
            window.addEventListener('resize', () => {
                if (window.innerWidth > 768) {
                    tocList.classList.remove('active');
                    tocToggle.classList.remove('expanded');
                    tocToggle.setAttribute('aria-expanded', 'false');
                }
            });
        }'''
        
        if bad_js in content:
            content = content.replace(bad_js, good_js)
            changed = True

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")

print("Review fixes completed.")
