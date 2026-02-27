import os
import re

# Use relative path derived from the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
blog_dir = os.path.join(root_dir, 'cbam-blog')

TOC_CSS = '''        @media (max-width: 1024px) {
            .article-layout {
                flex-direction: column;
            }

            .toc-sidebar {
                width: 100%;
                order: -1;
            }

            .toc-sticky {
                position: relative;
                top: 0;
            }
        }

        @media (max-width: 768px) {
            .toc-sidebar {
                /* Changed to block to allow customization */
                display: block;
                margin-top: 80px; /* Space for navbar */
            }

            .toc-sticky {
                padding: 15px; /* Smaller padding on mobile */
            }

            .toc-title {
                display: flex;
                justify-content: space-between;
                align-items: center;
                cursor: pointer;
                margin-bottom: 0; /* Remove margin when collapsed */
                border-bottom: none; /* Add border gracefully on expand */
            }

            .toc-title i {
                transition: transform 0.3s ease;
            }

            .toc-title.expanded i {
                transform: rotate(180deg);
            }

            .toc-list {
                display: none; /* Hidden by default on mobile */
                margin-top: 15px;
                padding-top: 15px;
                border-top: 2px solid #e9ecef;
                animation: slideDown 0.3s ease-out;
            }
            
            .toc-list.active {
                display: block;
            }

            .article-layout {
                margin-top: 20px; /* Reduced from 80px since TOC handles it */
                padding: 0 20px;
            }

            h1 {
                font-size: 32px;
            }

            .article-content h2 {
                font-size: 26px;
            }

            .featured-image {
                height: 250px;
            }
            
            @keyframes slideDown {
                from { opacity: 0; transform: translateY(-10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        }'''

old_media_query = '''        @media (max-width: 1024px) {
            .article-layout {
                flex-direction: column;
            }

            .toc-sidebar {
                width: 100%;
                order: -1;
            }

            .toc-sticky {
                position: relative;
                top: 0;
            }
        }

        @media (max-width: 768px) {
            .toc-sidebar {
                display: none;
            }

            .article-layout {
                margin-top: 80px;
                padding: 0 20px;
            }

            h1 {
                font-size: 32px;
            }

            .article-content h2 {
                font-size: 26px;
            }

            .featured-image {
                height: 250px;
            }
        }'''

old_toc_title = '<div class="toc-title">ON THIS PAGE</div>'
new_toc_title = '<div class="toc-title" id="mobileTocToggle" role="button" aria-expanded="false" tabindex="0" aria-label="Toggle Table of Contents">ON THIS PAGE <i class="fas fa-chevron-down mobile-only-icon" style="display:none;"></i></div>'

# New JS to handle TOC toggle correctly avoiding initial window resize constraints
toc_js = '''<script>
        // Mobile TOC Toggle
        document.addEventListener('DOMContentLoaded', () => {
            const tocToggle = document.getElementById('mobileTocToggle');
            const tocList = document.querySelector('.toc-list');
            
            if (tocToggle && tocList) {
                // Support keyboard interaction for accessibility
                tocToggle.addEventListener('keydown', function(e) {
                    if (e.key === 'Enter' || e.key === ' ') {
                        e.preventDefault();
                        this.click();
                    }
                });
                
                tocToggle.addEventListener('click', function() {
                    if (window.innerWidth <= 768) {
                        const isExpanded = this.getAttribute('aria-expanded') === 'true';
                        this.setAttribute('aria-expanded', !isExpanded);
                        tocList.classList.toggle('active');
                        this.classList.toggle('expanded');
                    }
                });
                
                // Close TOC when a link is clicked on mobile
                const tocLinks = document.querySelectorAll('.toc-list a');
                tocLinks.forEach(link => {
                    link.addEventListener('click', () => {
                        if (window.innerWidth <= 768) {
                            tocToggle.setAttribute('aria-expanded', 'false');
                            tocList.classList.remove('active');
                            tocToggle.classList.remove('expanded');
                        }
                    });
                });
            }
        });
</script>'''

for filename in os.listdir(blog_dir):
    if not filename.endswith('.html'):
        continue

    filepath = os.path.join(blog_dir, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        continue

    changed = False

    # 1. Update CSS
    if old_media_query in content:
        content = content.replace(old_media_query, TOC_CSS, 1)
        changed = True
        
    # Idempotent CSS addition
    if '.mobile-only-icon { display: none; }' not in content and '.toc-title i {' in content:
        content = content.replace('.toc-title i {', '.mobile-only-icon { display: none; }\n            @media (max-width: 768px) { .mobile-only-icon { display: inline-block !important; } }\n            .toc-title i {')
        changed = True

    # 2. Update HTML (using regex to make sure we don't duplicate attributes if already changed)
    if 'id="mobileTocToggle"' not in content:
        if old_toc_title in content:
            content = content.replace(old_toc_title, new_toc_title, 1)
            changed = True

    # 3. Update JS
    if 'Mobile TOC Toggle' not in content and '</body>' in content:
        content = content.replace('</body>', toc_js + '\n</body>', 1)
        changed = True

    if changed:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {filename}")
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
            
print("Mobile TOC script completed.")
