@echo off
REM EnCarbonSys Repository Reorganization Script (Windows)
REM This script moves files to their proper locations

echo.
echo 🚀 Starting repository reorganization...
echo.

REM Check if we're in the right directory
if not exist "index.html" (
    echo ❌ Error: index.html not found. Please run this script from the repository root.
    pause
    exit /b 1
)

echo ✅ Found repository root
echo.

REM CSS Files
echo 📁 Moving CSS files...
if exist "style1.css" (
    git mv "style1.css" "assets/css/style1.css" 2>nul || move "style1.css" "assets\css\style1.css"
    echo ✅ Moved: style1.css
)
if exist "navbar.css" (
    git mv "navbar.css" "assets/css/navbar.css" 2>nul || move "navbar.css" "assets\css\navbar.css"
    echo ✅ Moved: navbar.css
)
if exist "CSS-TOC-ADDITION.css" (
    git mv "CSS-TOC-ADDITION.css" "assets/css/toc-addition.css" 2>nul || move "CSS-TOC-ADDITION.css" "assets\css\toc-addition.css"
    echo ✅ Moved: CSS-TOC-ADDITION.css
)
echo.

REM JavaScript Files
echo 📁 Moving JavaScript files...
if exist "main.js" (
    git mv "main.js" "assets/js/main.js" 2>nul || move "main.js" "assets\js\main.js"
    echo ✅ Moved: main.js
)
if exist "JS-TOC-ADDITION.js" (
    git mv "JS-TOC-ADDITION.js" "assets/js/toc-addition.js" 2>nul || move "JS-TOC-ADDITION.js" "assets\js\toc-addition.js"
    echo ✅ Moved: JS-TOC-ADDITION.js
)
echo.

REM Images
echo 📁 Moving images...
if exist "favicon.png" (
    git mv "favicon.png" "assets/images/favicon.png" 2>nul || move "favicon.png" "assets\images\favicon.png"
    echo ✅ Moved: favicon.png
)
echo.

REM PDF Files
echo 📁 Moving PDF files...
if exist "brochure.pdf" (
    git mv "brochure.pdf" "assets/pdf/brochure.pdf" 2>nul || move "brochure.pdf" "assets\pdf\brochure.pdf"
    echo ✅ Moved: brochure.pdf
)
if exist "EnCarbonSys PRIVACY POLICY.pdf" (
    git mv "EnCarbonSys PRIVACY POLICY.pdf" "assets/pdf/privacy-policy.pdf" 2>nul || move "EnCarbonSys PRIVACY POLICY.pdf" "assets\pdf\privacy-policy.pdf"
    echo ✅ Moved: EnCarbonSys PRIVACY POLICY.pdf
)
if exist "Refund & Cancellation Policy (1).pdf" (
    git mv "Refund & Cancellation Policy (1).pdf" "assets/pdf/refund-cancellation-policy.pdf" 2>nul || move "Refund & Cancellation Policy (1).pdf" "assets\pdf\refund-cancellation-policy.pdf"
    echo ✅ Moved: Refund ^& Cancellation Policy (1).pdf
)
if exist "Terms & Conditions.pdf" (
    git mv "Terms & Conditions.pdf" "assets/pdf/terms-conditions.pdf" 2>nul || move "Terms & Conditions.pdf" "assets\pdf\terms-conditions.pdf"
    echo ✅ Moved: Terms ^& Conditions.pdf
)
echo.

REM HTML Pages
echo 📁 Moving HTML pages...
if exist "client _resource.html" (
    git mv "client _resource.html" "pages/client-resource.html" 2>nul || move "client _resource.html" "pages\client-resource.html"
    echo ✅ Moved: client _resource.html
)
if exist "pricing" (
    git mv "pricing" "pages/pricing.html" 2>nul || move "pricing" "pages\pricing.html"
    echo ✅ Moved: pricing
)
if exist "EnCBAM_pro.html" (
    git mv "EnCBAM_pro.html" "pages/encbam-pro.html" 2>nul || move "EnCBAM_pro.html" "pages\encbam-pro.html"
    echo ✅ Moved: EnCBAM_pro.html
)
if exist "october.html" (
    git mv "october.html" "pages/october.html" 2>nul || move "october.html" "pages\october.html"
    echo ✅ Moved: october.html
)
echo.

REM Components
echo 📁 Moving components...
if exist "navbar.html" (
    git mv "navbar.html" "components/navbar.html" 2>nul || move "navbar.html" "components\navbar.html"
    echo ✅ Moved: navbar.html
)
if exist "blog-widget.html" (
    git mv "blog-widget.html" "components/blog-widget.html" 2>nul || move "blog-widget.html" "components\blog-widget.html"
    echo ✅ Moved: blog-widget.html
)
if exist "meta-tags-template.html" (
    git mv "meta-tags-template.html" "components/meta-tags-template.html" 2>nul || move "meta-tags-template.html" "components\meta-tags-template.html"
    echo ✅ Moved: meta-tags-template.html
)
echo.

REM Create subdirectories
if not exist "docs\checklists" mkdir "docs\checklists"
if not exist "docs\summaries" mkdir "docs\summaries"

REM Documentation - Guides
echo 📁 Moving documentation...
for %%f in (
    "ADD-TOC-SIDEBAR-GUIDE.md"
    "APPLY-SEO-TEMPLATE-GUIDE.md"
    "BATCH-UPDATE-SCRIPT.md"
    "FINAL-IMPLEMENTATION-GUIDE.md"
    "GOOGLE-SEARCH-CONSOLE-GUIDE.md"
    "MANUAL-UPDATE-INSTRUCTIONS.md"
    "QUICK-SEO-REFERENCE.md"
    "QUICK-TOC-IMPLEMENTATION.md"
    "NAVBAR-UPDATE-CODE.md"
    "REPO-REORGANIZATION-PLAN.md"
    "QUICK-START-GUIDE.md"
    "COMPLETE-REORGANIZATION-SCRIPT.md"
    "START-HERE.md"
) do (
    if exist %%f (
        git mv %%f "docs/guides/%%~nxf" 2>nul || move %%f "docs\guides\%%~nxf"
        echo ✅ Moved: %%f
    )
)

REM Templates
for %%f in (
    "ARTICLE-TEMPLATE.html"
    "schema-templates.html"
) do (
    if exist %%f (
        git mv %%f "docs/templates/%%~nxf" 2>nul || move %%f "docs\templates\%%~nxf"
        echo ✅ Moved: %%f
    )
)

REM Checklists
for %%f in (
    "SEO-CHECKLIST.md"
    "SEO-IMPLEMENTATION-CHECKLIST.md"
    "ULTIMATE-SEO-GUIDE.md"
) do (
    if exist %%f (
        git mv %%f "docs/checklists/%%~nxf" 2>nul || move %%f "docs\checklists\%%~nxf"
        echo ✅ Moved: %%f
    )
)

REM Summaries
for %%f in (
    "BLOG-ENHANCEMENTS-SUMMARY.md"
    "BLOG-OPTIMIZATION-COMPLETE.md"
    "PROGRESS-UPDATE.md"
    "UPDATE-PLAN-SUMMARY.md"
) do (
    if exist %%f (
        git mv %%f "docs/summaries/%%~nxf" 2>nul || move %%f "docs\summaries\%%~nxf"
        echo ✅ Moved: %%f
    )
)
echo.

REM Scripts
echo 📁 Moving scripts...
if exist "update_remaining_h1.py" (
    git mv "update_remaining_h1.py" "scripts/update_remaining_h1.py" 2>nul || move "update_remaining_h1.py" "scripts\update_remaining_h1.py"
    echo ✅ Moved: update_remaining_h1.py
)
echo.

echo ✅ File reorganization complete!
echo.
echo ⚠️  IMPORTANT: You still need to:
echo    1. Update file references in index.html
echo    2. Update file references in components/navbar.html
echo    3. Update file references in all blog pages
echo    4. Add favicons to blog pages
echo.
echo 📝 See docs/guides/complete-reorganization-script.md for details
echo.
echo 🔄 To commit these changes:
echo    git add .
echo    git commit -m "Reorganize repository structure"
echo    git push origin main
echo.
pause
