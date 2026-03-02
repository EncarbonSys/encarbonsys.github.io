import os
import re

# Use relative path derived from the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
blog_dir = os.path.join(root_dir, 'cbam-blog')

TOC_CSS = '''        .toc-sticky {
            max-height: calc(100vh - 140px);
            overflow-y: auto;
            scrollbar-width: thin;
            scrollbar-color: #ccc #f8f9fa;
        }

        /* Custom Scrollbar Styling */
        .toc-sticky::-webkit-scrollbar {
            width: 6px;
        }

        .toc-sticky::-webkit-scrollbar-track {
            background: #f8f9fa;
            border-radius: 10px;
        }

        .toc-sticky::-webkit-scrollbar-thumb {
            background: #ccc;
            border-radius: 10px;
        }

        .toc-sticky::-webkit-scrollbar-thumb:hover {
            background: #2DF56D;
        }

        @media (max-width: 1024px) {
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
                max-height: none; /* No scroll on mobile since it collapses */
                overflow-y: visible;
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

    # 1. Update CSS using regex for more robustness
    # This regex looks for the block starting at @media (max-width: 1024px) and tries to match until the end of the TOC-related media queries
    toc_css_pattern = r'        @media \(max-width: 1024px\) \{.*?@media \(max-width: 768px\) \{.*?\}\s*\}'
    # Wait, the nested braces can be tricky. Let's use a simpler marker if possible.
    # Actually, the TOC_CSS I want to inject is quite specific.
    
    # Let's try to match from @media (max-width: 1024px) until the end of the next block
    # Since we know the structure from previous runs:
    if '@media (max-width: 1024px)' in content and '@media (max-width: 768px)' in content:
        # Simple string replacement for what's likely there in most files
        # We'll try to find the whole block.
        # If it doesn't match exactly, we'll try a regex.
        
        # Let's use a regex that matches the start of the block and looks for the likely end.
        import re
        # This matches from @media (max-width: 1024px) until the closing brace of the 768px block
        # We use a greedy inner match for the 768px block but anchored to the next closing brace at column 8
        pattern = re.compile(r'[ \t]*@media \(max-width: 1024px\) \{.*?@media \(max-width: 768px\) \{.*?\n[ \t]*\}', re.DOTALL)
        # Wait, that's still not quite right for the nested braces. 
        # Let's just find the START and then go until we find the END of the style tag or another known marker.
        # Actually, let's just find the broad block:
        pattern = re.compile(r'\s*@media \(max-width: 1024px\) \{.*?@media \(max-width: 768px\) \{.*?\n\s*\}\s*\}', re.DOTALL)
        
        if pattern.search(content):
            content = pattern.sub('\n' + TOC_CSS, content)
            changed = True
        elif 'max-height: calc(100vh - 140px);' not in content and '.toc-sticky {' in content:
            # If the media query block is missing but toc-sticky is there, let's just add it before the closing </style>
            content = content.replace('</style>', TOC_CSS + '\n    </style>')
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
