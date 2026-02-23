# 📁 Repository Reorganization Plan

## Current Issues
- ❌ Too many files in root directory (42 items)
- ❌ Documentation files mixed with website files
- ❌ No clear folder structure
- ❌ Hard to find specific files

## Proposed Structure
```
encarbonsys.github.io/
├── index.html                    # Main homepage (KEEP IN ROOT)
├── README.md                     # Project overview
├── CNAME                         # GitHub Pages domain
├── robots.txt                    # SEO
├── sitemap.xml                   # SEO
├── sitemap-blog.xml              # Blog SEO
│
├── assets/                       # All static assets
│   ├── css/
│   │   ├── style1.css
│   │   ├── navbar.css
│   │   └── CSS-TOC-ADDITION.css
│   ├── js/
│   │   ├── main.js
│   │   └── JS-TOC-ADDITION.js
│   ├── images/
│   │   └── favicon.png
│   └── pdf/
│       ├── brochure.pdf
│       ├── EnCarbonSys-PRIVACY-POLICY.pdf
│       ├── Refund-Cancellation-Policy.pdf
│       └── Terms-Conditions.pdf
│
├── pages/                        # Additional HTML pages
│   ├── client-resource.html      # Renamed from "client _resource.html"
│   ├── pricing.html
│   ├── EnCBAM_pro.html
│   └── october.html
│
├── tools/                        # Interactive tools (CREATE THIS)
│   ├── cn-code-checker.html
│   ├── emissions-calculator.html
│   └── cbam-cost-estimator.html
│
├── components/                   # Reusable components
│   ├── navbar.html
│   ├── blog-widget.html
│   └── meta-tags-template.html
│
├── cbam-blog/                    # Blog section (EXISTING)
│   └── [existing blog structure]
│
├── docs/                         # Documentation & guides
│   ├── guides/
│   │   ├── ADD-TOC-SIDEBAR-GUIDE.md
│   │   ├── APPLY-SEO-TEMPLATE-GUIDE.md
│   │   ├── BATCH-UPDATE-SCRIPT.md
│   │   ├── FINAL-IMPLEMENTATION-GUIDE.md
│   │   ├── GOOGLE-SEARCH-CONSOLE-GUIDE.md
│   │   ├── MANUAL-UPDATE-INSTRUCTIONS.md
│   │   ├── QUICK-SEO-REFERENCE.md
│   │   └── QUICK-TOC-IMPLEMENTATION.md
│   ├── templates/
│   │   ├── ARTICLE-TEMPLATE.html
│   │   └── schema-templates.html
│   ├── checklists/
│   │   ├── SEO-CHECKLIST.md
│   │   ├── SEO-IMPLEMENTATION-CHECKLIST.md
│   │   └── ULTIMATE-SEO-GUIDE.md
│   └── summaries/
│       ├── BLOG-ENHANCEMENTS-SUMMARY.md
│       ├── BLOG-OPTIMIZATION-COMPLETE.md
│       ├── PROGRESS-UPDATE.md
│       └── UPDATE-PLAN-SUMMARY.md
│
└── scripts/                      # Build/utility scripts
    └── update_remaining_h1.py
```

## Migration Steps (NO FUNCTIONALITY CHANGES)

### Phase 1: Create Folder Structure
1. Create `assets/` with subfolders: `css/`, `js/`, `images/`, `pdf/`
2. Create `pages/`
3. Create `tools/`
4. Create `components/`
5. Create `docs/` with subfolders: `guides/`, `templates/`, `checklists/`, `summaries/`
6. Create `scripts/`

### Phase 2: Move Files (Using GitHub Web Interface - FREE)
**Assets:**
- Move `style1.css`, `navbar.css`, `CSS-TOC-ADDITION.css` → `assets/css/`
- Move `main.js`, `JS-TOC-ADDITION.js` → `assets/js/`
- Move `favicon.png` → `assets/images/`
- Move all PDFs → `assets/pdf/` (rename to remove spaces)

**Pages:**
- Move `client _resource.html` → `pages/client-resource.html` (rename)
- Move `pricing`, `EnCBAM_pro.html`, `october.html` → `pages/`

**Components:**
- Move `navbar.html`, `blog-widget.html`, `meta-tags-template.html` → `components/`

**Documentation:**
- Move all guide `.md` files → `docs/guides/`
- Move template `.html` files → `docs/templates/`
- Move checklist `.md` files → `docs/checklists/`
- Move summary `.md` files → `docs/summaries/`

**Scripts:**
- Move `update_remaining_h1.py` → `scripts/`

### Phase 3: Update File References
**In `index.html`:**
- Update CSS links: `style1.css` → `assets/css/style1.css`
- Update JS links: `main.js` → `assets/js/main.js`
- Update favicon: `favicon.png` → `assets/images/favicon.png`
- Update PDF links: `brochure.pdf` → `assets/pdf/brochure.pdf`
- Update navbar link: `/client _resource.html` → `/pages/client-resource.html`

**In `navbar.html`:**
- Update Client Hub link: `/client _resource.html` → `/pages/client-resource.html`

**In blog pages:**
- Update navbar include path if needed

### Phase 4: Test Everything
- ✅ Homepage loads correctly
- ✅ All CSS/JS files load
- ✅ All links work
- ✅ Blog pages work
- ✅ PDFs download correctly
- ✅ Navbar appears on all pages

## Benefits
✅ **Cleaner root directory** - Only essential files visible
✅ **Better organization** - Easy to find files by category
✅ **Professional structure** - Follows GitHub Pages best practices
✅ **Easier maintenance** - Clear separation of concerns
✅ **Better collaboration** - New team members can navigate easily
✅ **Scalability** - Easy to add new pages/tools/docs

## Tools Used (All FREE)
- ✅ GitHub Web Interface - Move/rename files
- ✅ GitHub Desktop (optional) - Bulk operations
- ✅ Text editor - Update file references

## Timeline
- **Phase 1**: 5 minutes (create folders)
- **Phase 2**: 15 minutes (move files)
- **Phase 3**: 10 minutes (update references)
- **Phase 4**: 10 minutes (testing)
- **Total**: ~40 minutes

## Notes
- ⚠️ **BACKUP FIRST**: Clone repo or download ZIP before starting
- ⚠️ **Test locally**: Use GitHub Pages preview or local server
- ⚠️ **One phase at a time**: Don't rush, test after each phase
- ✅ **No functionality changes**: Website works exactly the same
- ✅ **SEO preserved**: All URLs remain the same (redirects if needed)
