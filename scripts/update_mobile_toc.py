import os
import re

root_dir = r'c:\Users\ASUS\Desktop\ENCARBONSYS\WEBSITE\WEBSIT GIT CLONE REPO\encarbonsys.github.io'
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

# Replace the old @media rules
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

# Update the TOC Title HTML to include the chevron icon for mobile
old_toc_title = '<div class="toc-title">ON THIS PAGE</div>'
new_toc_title = '<div class="toc-title" id="mobileTocToggle">ON THIS PAGE <i class="fas fa-chevron-down mobile-only-icon" style="display:none;"></i></div>'

# Add mobile icon display rule
mobile_icon_css = '''
        @media (max-width: 768px) {
            .mobile-only-icon { display: inline-block !important; }
'''

# New JS to handle TOC toggle
toc_js = '''
        // Mobile TOC Toggle
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
        }
'''


for filename in os.listdir(blog_dir):
    if not filename.endswith('.html'):
        continue

    filepath = os.path.join(blog_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # 1. Update CSS
    if old_media_query in content:
        content = content.replace(old_media_query, TOC_CSS, 1)
        # add the mobile icon rule inside the new 768px block if possible. The TOC_CSS above handles the icon but we need the generic rule just in case, but let's just make the inline style display:none and we override it.
        # Actually in TOC_CSS: `.toc-title i` is there. We also need to add `.mobile-only-icon` display block
        content = content.replace('.toc-title i {', '.mobile-only-icon { display: none; }\n            @media (max-width: 768px) { .mobile-only-icon { display: inline-block !important; } }\n            .toc-title i {')
        changed = True

    # 2. Update HTML
    if old_toc_title in content:
        content = content.replace(old_toc_title, new_toc_title, 1)
        changed = True

    # 3. Update JS
    if 'Mobile TOC Toggle' not in content and '</script>\n</body>' in content:
        content = content.replace('</script>\n</body>', toc_js + '</script>\n</body>', 1)
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filename}")
        
print("Mobile TOC script completed.")
