import os
import glob

# Use relative paths for better portability
blog_dir = 'cbam-blog'

BAD_FETCH = '''    <script>
        fetch('/components/navbar.html')
            .then(r => r.text())
            .then(html => document.getElementById('navbar').innerHTML = html);
    </script>'''

GOOD_FETCH = '''    <script>
        fetch('/components/navbar.html')
            .then(r => r.text())
            .then(html => {
                const navbarContainer = document.getElementById('navbar');
                navbarContainer.innerHTML = html;
                
                // Extract and execute scripts from the injected HTML
                const scripts = navbarContainer.getElementsByTagName('script');
                for (let i = 0; i < scripts.length; i++) {
                    const newScript = document.createElement('script');
                    if (scripts[i].src) {
                        newScript.src = scripts[i].src;
                    } else {
                        newScript.textContent = scripts[i].textContent;
                    }
                    document.body.appendChild(newScript);
                }
            });
    </script>'''

# Find all HTML files in the blog directory
for filepath in glob.glob(os.path.join(blog_dir, '*.html')):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        if BAD_FETCH in content:
            content = content.replace(BAD_FETCH, GOOD_FETCH)
            changed = True

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")

print("Navbar JS execution fix completed.")
