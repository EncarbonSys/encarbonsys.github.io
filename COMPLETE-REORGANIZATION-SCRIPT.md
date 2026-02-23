# 🚀 Complete Repository Reorganization Script

## ✅ What's Already Done

### Folders Created:
- ✅ `assets/css/`
- ✅ `assets/js/`
- ✅ `assets/images/`
- ✅ `assets/pdf/`
- ✅ `pages/`
- ✅ `components/`
- ✅ `docs/guides/`
- ✅ `docs/templates/`
- ✅ `scripts/`

### Navbar Fixed:
- ✅ Get Started button is now MUCH wider (`padding: 0.9rem 3.5rem`)
- ✅ Minimum width set to 160px
- ✅ Better spacing and gradient

---

## 📋 Step-by-Step Reorganization (Using GitHub Web Interface - FREE)

### Phase 1: Add Favicons to Blog Pages (10 minutes)

**Files that need favicon:**
1. `cbam-blog/index.html`
2. `cbam-blog/authorised-declarant-guide.html`
3. `cbam-blog/cbam-developing-countries-impact.html`
4. `cbam-blog/cbam-impact-steel-industry.html`
5. `cbam-blog/cbam-omnibus-new-rules.html`
6. `cbam-blog/cbam-six-pains-predictions.html`
7. `cbam-blog/cbam-updates-april-2025.html`
8. `cbam-blog/cbam-verification-requirements-2026.html`
9. `cbam-blog/hs-hsn-cn-taric-codes-complete-guide.html`
10. `cbam-blog/navigating-cbam-changes.html`
11. `cbam-blog/supplier-data-management.html`

**Favicon code to add (after `<meta name="viewport">` line):**
```html
    <!-- Favicon -->
    <link rel="icon" type="image/png" href="/favicon.png">
    <link rel="shortcut icon" type="image/png" href="/favicon.png">
```

**How to add:**
1. Go to each file on GitHub
2. Click "Edit" (pencil icon)
3. Find the line: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
4. Add the favicon code right after it
5. Commit with message: "Add favicon to [filename]"

---

### Phase 2: Move CSS Files (5 minutes)

**Files to move to `assets/css/`:**
1. `style1.css` → `assets/css/style1.css`
2. `navbar.css` → `assets/css/navbar.css`
3. `CSS-TOC-ADDITION.css` → `assets/css/toc-addition.css` (rename)

**How to move using GitHub Web:**
1. Go to file (e.g., `style1.css`)
2. Click "..." (three dots) → "Move file"
3. Change path to: `assets/css/style1.css`
4. Commit with message: "Move CSS files to assets/css/"

---

### Phase 3: Move JavaScript Files (2 minutes)

**Files to move to `assets/js/`:**
1. `main.js` → `assets/js/main.js`
2. `JS-TOC-ADDITION.js` → `assets/js/toc-addition.js` (rename)

**How to move:**
1. Same process as CSS files
2. Change path to: `assets/js/[filename]`

---

### Phase 4: Move Images (2 minutes)

**Files to move to `assets/images/`:**
1. `favicon.png` → `assets/images/favicon.png`

---

### Phase 5: Move PDF Files (5 minutes)

**Files to move to `assets/pdf/` (and rename to remove spaces):**
1. `brochure.pdf` → `assets/pdf/brochure.pdf`
2. `EnCarbonSys PRIVACY POLICY.pdf` → `assets/pdf/privacy-policy.pdf`
3. `Refund & Cancellation Policy (1).pdf` → `assets/pdf/refund-cancellation-policy.pdf`
4. `Terms & Conditions.pdf` → `assets/pdf/terms-conditions.pdf`

---

### Phase 6: Move HTML Pages (5 minutes)

**Files to move to `pages/`:**
1. `client _resource.html` → `pages/client-resource.html` (rename - remove space)
2. `pricing` → `pages/pricing.html` (add .html extension)
3. `EnCBAM_pro.html` → `pages/encbam-pro.html` (rename to lowercase)
4. `october.html` → `pages/october.html`

---

### Phase 7: Move Components (3 minutes)

**Files to move to `components/`:**
1. `navbar.html` → `components/navbar.html`
2. `blog-widget.html` → `components/blog-widget.html`
3. `meta-tags-template.html` → `components/meta-tags-template.html`

---

### Phase 8: Move Documentation (10 minutes)

**Move to `docs/guides/`:**
1. `ADD-TOC-SIDEBAR-GUIDE.md`
2. `APPLY-SEO-TEMPLATE-GUIDE.md`
3. `BATCH-UPDATE-SCRIPT.md`
4. `FINAL-IMPLEMENTATION-GUIDE.md`
5. `GOOGLE-SEARCH-CONSOLE-GUIDE.md`
6. `MANUAL-UPDATE-INSTRUCTIONS.md`
7. `QUICK-SEO-REFERENCE.md`
8. `QUICK-TOC-IMPLEMENTATION.md`
9. `NAVBAR-UPDATE-CODE.md`
10. `REPO-REORGANIZATION-PLAN.md`
11. `QUICK-START-GUIDE.md`

**Move to `docs/templates/`:**
1. `ARTICLE-TEMPLATE.html`
2. `schema-templates.html`

**Move to `docs/checklists/`:**
Create folder first: `docs/checklists/.gitkeep`
Then move:
1. `SEO-CHECKLIST.md`
2. `SEO-IMPLEMENTATION-CHECKLIST.md`
3. `ULTIMATE-SEO-GUIDE.md`

**Move to `docs/summaries/`:**
Create folder first: `docs/summaries/.gitkeep`
Then move:
1. `BLOG-ENHANCEMENTS-SUMMARY.md`
2. `BLOG-OPTIMIZATION-COMPLETE.md`
3. `PROGRESS-UPDATE.md`
4. `UPDATE-PLAN-SUMMARY.md`

---

### Phase 9: Move Scripts (2 minutes)

**Files to move to `scripts/`:**
1. `update_remaining_h1.py` → `scripts/update_remaining_h1.py`

---

### Phase 10: Update File References (15 minutes)

#### In `index.html`:

**Find and replace:**
```html
<!-- OLD -->
<link rel="stylesheet" href="style1.css">
<link rel="icon" href="/favicon.png">
<script src="main.js"></script>
<a href="/client _resource.html">

<!-- NEW -->
<link rel="stylesheet" href="assets/css/style1.css">
<link rel="icon" href="/assets/images/favicon.png">
<script src="assets/js/main.js"></script>
<a href="/pages/client-resource.html">
```

**PDF links:**
```html
<!-- OLD -->
href="brochure.pdf"
href="EnCarbonSys PRIVACY POLICY.pdf"
href="Refund & Cancellation Policy (1).pdf"
href="Terms & Conditions.pdf"

<!-- NEW -->
href="assets/pdf/brochure.pdf"
href="assets/pdf/privacy-policy.pdf"
href="assets/pdf/refund-cancellation-policy.pdf"
href="assets/pdf/terms-conditions.pdf"
```

#### In `components/navbar.html`:

**Find and replace:**
```html
<!-- OLD -->
<a href="/client _resource.html">Client Hub</a>

<!-- NEW -->
<a href="/pages/client-resource.html">Client Hub</a>
```

#### In ALL blog pages (`cbam-blog/*.html`):

**Find and replace:**
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

---

## 🤖 Automated Script (Optional - For Advanced Users)

If you want to automate this, here's a Python script:

```python
import os
import shutil

# File mappings
moves = {
    # CSS
    'style1.css': 'assets/css/style1.css',
    'navbar.css': 'assets/css/navbar.css',
    'CSS-TOC-ADDITION.css': 'assets/css/toc-addition.css',
    
    # JS
    'main.js': 'assets/js/main.js',
    'JS-TOC-ADDITION.js': 'assets/js/toc-addition.js',
    
    # Images
    'favicon.png': 'assets/images/favicon.png',
    
    # PDFs
    'brochure.pdf': 'assets/pdf/brochure.pdf',
    'EnCarbonSys PRIVACY POLICY.pdf': 'assets/pdf/privacy-policy.pdf',
    'Refund & Cancellation Policy (1).pdf': 'assets/pdf/refund-cancellation-policy.pdf',
    'Terms & Conditions.pdf': 'assets/pdf/terms-conditions.pdf',
    
    # Pages
    'client _resource.html': 'pages/client-resource.html',
    'pricing': 'pages/pricing.html',
    'EnCBAM_pro.html': 'pages/encbam-pro.html',
    'october.html': 'pages/october.html',
    
    # Components
    'navbar.html': 'components/navbar.html',
    'blog-widget.html': 'components/blog-widget.html',
    'meta-tags-template.html': 'components/meta-tags-template.html',
    
    # Scripts
    'update_remaining_h1.py': 'scripts/update_remaining_h1.py',
}

# Move files
for old_path, new_path in moves.items():
    if os.path.exists(old_path):
        os.makedirs(os.path.dirname(new_path), exist_ok=True)
        shutil.move(old_path, new_path)
        print(f"✅ Moved: {old_path} → {new_path}")
    else:
        print(f"⚠️  Not found: {old_path}")

print("\n✅ All files moved!")
print("\n⚠️  Don't forget to update file references in:")
print("   - index.html")
print("   - components/navbar.html")
print("   - All blog pages")
```

**To use:**
1. Clone your repo locally
2. Save script as `reorganize.py`
3. Run: `python reorganize.py`
4. Commit and push all changes

---

## ✅ Final Checklist

After reorganization:

### Files Moved:
- [ ] All CSS files in `assets/css/`
- [ ] All JS files in `assets/js/`
- [ ] All images in `assets/images/`
- [ ] All PDFs in `assets/pdf/`
- [ ] All pages in `pages/`
- [ ] All components in `components/`
- [ ] All docs organized in `docs/`
- [ ] All scripts in `scripts/`

### Favicons Added:
- [ ] `cbam-blog/index.html`
- [ ] All 11 blog article pages

### References Updated:
- [ ] `index.html` - CSS, JS, images, PDFs, page links
- [ ] `components/navbar.html` - page links
- [ ] All blog pages - navbar.css, favicon, navbar.html

### Testing:
- [ ] Homepage loads correctly
- [ ] All CSS styles work
- [ ] All JavaScript works
- [ ] All images display
- [ ] All PDFs download
- [ ] All page links work
- [ ] Blog pages load correctly
- [ ] Navbar appears on all pages
- [ ] Favicons show in browser tabs

---

## 📊 Before vs After

### Before (42 files in root):
```
encarbonsys.github.io/
├── index.html
├── style1.css
├── main.js
├── favicon.png
├── brochure.pdf
├── navbar.html
├── ADD-TOC-SIDEBAR-GUIDE.md
├── ... (35 more files)
└── cbam-blog/
```

### After (Clean structure):
```
encarbonsys.github.io/
├── index.html                    ← ONLY ESSENTIAL FILES IN ROOT
├── README.md
├── CNAME
├── robots.txt
├── sitemap.xml
├── sitemap-blog.xml
│
├── assets/                       ← ALL STATIC ASSETS
│   ├── css/
│   ├── js/
│   ├── images/
│   └── pdf/
│
├── pages/                        ← ADDITIONAL PAGES
├── components/                   ← REUSABLE COMPONENTS
├── docs/                         ← DOCUMENTATION
├── cbam-blog/                    ← BLOG (UNCHANGED)
└── scripts/                      ← UTILITY SCRIPTS
```

---

## 🎯 Benefits

✅ **Cleaner root** - Only 6 essential files visible  
✅ **Professional structure** - Follows GitHub Pages best practices  
✅ **Easy navigation** - Find files by category  
✅ **Better SEO** - Favicons on all pages  
✅ **Scalable** - Easy to add new content  
✅ **Maintainable** - Clear organization  

---

## ⏱️ Time Estimate

| Phase | Time | Difficulty |
|-------|------|------------|
| Add favicons | 10 min | Easy |
| Move CSS files | 5 min | Easy |
| Move JS files | 2 min | Easy |
| Move images | 2 min | Easy |
| Move PDFs | 5 min | Easy |
| Move pages | 5 min | Easy |
| Move components | 3 min | Easy |
| Move docs | 10 min | Easy |
| Move scripts | 2 min | Easy |
| Update references | 15 min | Medium |
| Testing | 10 min | Easy |
| **Total** | **~70 min** | **Easy** |

---

## 🆘 Need Help?

**Common Issues:**

1. **File not found after move**: Check the new path is correct
2. **CSS not loading**: Update `<link>` tags in HTML
3. **Images broken**: Update `src` attributes
4. **404 errors**: Clear browser cache (Ctrl+Shift+R)
5. **Navbar missing**: Update `fetch('/navbar.html')` to `fetch('/components/navbar.html')`

**Testing Tips:**
- Test locally before pushing to GitHub
- Use browser DevTools to check for errors
- Test in incognito mode to avoid cache
- Check both desktop and mobile views

---

**You've got this! Take it one phase at a time. 💪**
