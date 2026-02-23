# 🚀 How To Reorganize Your Repository (AUTOMATED)

## ✅ I've Created Automated Scripts For You!

You have **2 scripts** that will do ALL the file moving for you:
- `reorganize.sh` - For Mac/Linux
- `reorganize.bat` - For Windows

---

## 🎯 Quick Start (Choose Your Method)

### Method 1: Using GitHub Desktop (EASIEST - Recommended)

1. **Download GitHub Desktop** (if you don't have it):
   - Go to: https://desktop.github.com/
   - Install it

2. **Clone your repository**:
   - Open GitHub Desktop
   - Click "File" → "Clone Repository"
   - Select "EncarbonSys/encarbonsys.github.io"
   - Choose a folder on your computer
   - Click "Clone"

3. **Run the script**:
   
   **On Windows:**
   - Open the cloned folder
   - Double-click `reorganize.bat`
   - Wait for it to finish
   
   **On Mac/Linux:**
   - Open Terminal
   - Navigate to the cloned folder: `cd path/to/encarbonsys.github.io`
   - Make script executable: `chmod +x reorganize.sh`
   - Run it: `./reorganize.sh`

4. **Commit and push**:
   - Go back to GitHub Desktop
   - You'll see all the file changes
   - Add commit message: "Reorganize repository structure"
   - Click "Commit to main"
   - Click "Push origin"

5. **Done!** ✅

---

### Method 2: Using Git Command Line

1. **Clone the repository**:
   ```bash
   git clone https://github.com/EncarbonSys/encarbonsys.github.io.git
   cd encarbonsys.github.io
   ```

2. **Run the script**:
   
   **On Windows:**
   ```cmd
   reorganize.bat
   ```
   
   **On Mac/Linux:**
   ```bash
   chmod +x reorganize.sh
   ./reorganize.sh
   ```

3. **Commit and push**:
   ```bash
   git add .
   git commit -m "Reorganize repository structure"
   git push origin main
   ```

4. **Done!** ✅

---

## 📋 What The Script Does

The script automatically moves:

✅ **CSS files** → `assets/css/`
- style1.css
- navbar.css
- CSS-TOC-ADDITION.css (renamed to toc-addition.css)

✅ **JavaScript files** → `assets/js/`
- main.js
- JS-TOC-ADDITION.js (renamed to toc-addition.js)

✅ **Images** → `assets/images/`
- favicon.png

✅ **PDF files** → `assets/pdf/`
- brochure.pdf
- EnCarbonSys PRIVACY POLICY.pdf (renamed to privacy-policy.pdf)
- Refund & Cancellation Policy (1).pdf (renamed to refund-cancellation-policy.pdf)
- Terms & Conditions.pdf (renamed to terms-conditions.pdf)

✅ **HTML pages** → `pages/`
- client _resource.html (renamed to client-resource.html)
- pricing (renamed to pricing.html)
- EnCBAM_pro.html (renamed to encbam-pro.html)
- october.html

✅ **Components** → `components/`
- navbar.html
- blog-widget.html
- meta-tags-template.html

✅ **Documentation** → `docs/`
- All .md guides → `docs/guides/`
- Templates → `docs/templates/`
- Checklists → `docs/checklists/`
- Summaries → `docs/summaries/`

✅ **Scripts** → `scripts/`
- update_remaining_h1.py

---

## ⚠️ After Running The Script

The script moves files but **doesn't update references**. You still need to:

### 1. Update `index.html` (5 minutes)

Find and replace:
```html
<!-- OLD -->
<link rel="stylesheet" href="style1.css">
<link rel="icon" href="/favicon.png">
<script src="main.js"></script>
<a href="/client _resource.html">
href="brochure.pdf"
href="EnCarbonSys PRIVACY POLICY.pdf"

<!-- NEW -->
<link rel="stylesheet" href="assets/css/style1.css">
<link rel="icon" href="/assets/images/favicon.png">
<script src="assets/js/main.js"></script>
<a href="/pages/client-resource.html">
href="assets/pdf/brochure.pdf"
href="assets/pdf/privacy-policy.pdf"
```

### 2. Update `components/navbar.html` (1 minute)

Find and replace:
```html
<!-- OLD -->
<a href="/client _resource.html">Client Hub</a>

<!-- NEW -->
<a href="/pages/client-resource.html">Client Hub</a>
```

### 3. Update ALL blog pages (10 minutes)

In every file in `cbam-blog/` folder, find and replace:
```html
<!-- OLD -->
<link rel="stylesheet" href="/navbar.css">
<link rel="icon" type="image/png" href="/favicon.png">
<script>
    fetch('/navbar.html')

<!-- NEW -->
<link rel="stylesheet" href="/assets/css/navbar.css">
<link rel="icon" type="image/png" href="/assets/images/favicon.png">
<script>
    fetch('/components/navbar.html')
```

### 4. Add Favicons (10 minutes)

Add this code to blog pages that don't have favicon:
```html
<!-- Add after <meta name="viewport"> line -->
    <!-- Favicon -->
    <link rel="icon" type="image/png" href="/assets/images/favicon.png">
    <link rel="shortcut icon" type="image/png" href="/assets/images/favicon.png">
```

Files that need it:
- cbam-blog/index.html
- cbam-blog/authorised-declarant-guide.html
- cbam-blog/cbam-developing-countries-impact.html
- cbam-blog/cbam-impact-steel-industry.html
- cbam-blog/cbam-omnibus-new-rules.html
- cbam-blog/cbam-six-pains-predictions.html
- cbam-blog/cbam-updates-april-2025.html
- cbam-blog/cbam-verification-requirements-2026.html
- cbam-blog/hs-hsn-cn-taric-codes-complete-guide.html
- cbam-blog/navigating-cbam-changes.html
- cbam-blog/supplier-data-management.html

---

## ✅ Testing Checklist

After updating references, test:

- [ ] Homepage loads (index.html)
- [ ] CSS styles work
- [ ] JavaScript works
- [ ] Images display
- [ ] PDFs download
- [ ] Page links work (Client Hub, etc.)
- [ ] Blog pages load
- [ ] Navbar appears on blog pages
- [ ] Favicons show in browser tabs

---

## 🆘 Troubleshooting

**Problem**: Script won't run on Mac/Linux  
**Solution**: Make it executable: `chmod +x reorganize.sh`

**Problem**: "Permission denied" error  
**Solution**: Run with sudo: `sudo ./reorganize.sh`

**Problem**: Files didn't move  
**Solution**: Make sure you're in the repository root folder

**Problem**: CSS not loading after update  
**Solution**: Clear browser cache (Ctrl+Shift+R)

**Problem**: 404 errors  
**Solution**: Check file paths in HTML match new locations

---

## ⏱️ Total Time

| Task | Time |
|------|------|
| Clone repo | 2 min |
| Run script | 1 min |
| Update index.html | 5 min |
| Update navbar.html | 1 min |
| Update blog pages | 10 min |
| Add favicons | 10 min |
| Test everything | 5 min |
| Commit & push | 2 min |
| **Total** | **~35 min** |

---

## 🎉 What You'll Have

### Before:
```
42 files cluttering root directory
Messy, unprofessional structure
```

### After:
```
Clean, organized structure:
├── index.html
├── README.md
├── CNAME
├── robots.txt
├── sitemap.xml
├── assets/
├── pages/
├── components/
├── docs/
├── cbam-blog/
└── scripts/
```

---

## 💡 Pro Tips

1. **Backup first**: The script uses `git mv` which is safe, but you can always revert
2. **Test locally**: Use Live Server or Python HTTP server to test before pushing
3. **One step at a time**: Run script, test, update references, test again
4. **Use Find & Replace**: Most code editors have "Find in Files" feature
5. **Clear cache**: Always test in incognito mode after changes

---

## 🔗 Need More Help?

- **Detailed guide**: See `docs/guides/complete-reorganization-script.md`
- **Quick reference**: See `docs/guides/start-here.md`
- **Navbar update**: See `docs/guides/navbar-update-code.md`

---

**Ready? Just run the script and follow the steps above! 🚀**
