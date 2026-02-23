#!/bin/bash

# EnCarbonSys Repository Reorganization Script
# This script moves files to their proper locations

echo "🚀 Starting repository reorganization..."
echo ""

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found. Please run this script from the repository root."
    exit 1
fi

echo "✅ Found repository root"
echo ""

# Function to move file with confirmation
move_file() {
    local src=$1
    local dest=$2
    
    if [ -f "$src" ]; then
        mkdir -p "$(dirname "$dest")"
        git mv "$src" "$dest" 2>/dev/null || mv "$src" "$dest"
        echo "✅ Moved: $src → $dest"
        return 0
    else
        echo "⚠️  Not found: $src"
        return 1
    fi
}

# CSS Files
echo "📁 Moving CSS files..."
move_file "style1.css" "assets/css/style1.css"
move_file "navbar.css" "assets/css/navbar.css"
move_file "CSS-TOC-ADDITION.css" "assets/css/toc-addition.css"
echo ""

# JavaScript Files
echo "📁 Moving JavaScript files..."
move_file "main.js" "assets/js/main.js"
move_file "JS-TOC-ADDITION.js" "assets/js/toc-addition.js"
echo ""

# Images
echo "📁 Moving images..."
move_file "favicon.png" "assets/images/favicon.png"
echo ""

# PDF Files
echo "📁 Moving PDF files..."
move_file "brochure.pdf" "assets/pdf/brochure.pdf"
move_file "EnCarbonSys PRIVACY POLICY.pdf" "assets/pdf/privacy-policy.pdf"
move_file "Refund & Cancellation Policy (1).pdf" "assets/pdf/refund-cancellation-policy.pdf"
move_file "Terms & Conditions.pdf" "assets/pdf/terms-conditions.pdf"
echo ""

# HTML Pages
echo "📁 Moving HTML pages..."
move_file "client _resource.html" "pages/client-resource.html"
move_file "pricing" "pages/pricing.html"
move_file "EnCBAM_pro.html" "pages/encbam-pro.html"
move_file "october.html" "pages/october.html"
echo ""

# Components
echo "📁 Moving components..."
move_file "navbar.html" "components/navbar.html"
move_file "blog-widget.html" "components/blog-widget.html"
move_file "meta-tags-template.html" "components/meta-tags-template.html"
echo ""

# Documentation - Guides
echo "📁 Moving documentation (guides)..."
move_file "ADD-TOC-SIDEBAR-GUIDE.md" "docs/guides/add-toc-sidebar-guide.md"
move_file "APPLY-SEO-TEMPLATE-GUIDE.md" "docs/guides/apply-seo-template-guide.md"
move_file "BATCH-UPDATE-SCRIPT.md" "docs/guides/batch-update-script.md"
move_file "FINAL-IMPLEMENTATION-GUIDE.md" "docs/guides/final-implementation-guide.md"
move_file "GOOGLE-SEARCH-CONSOLE-GUIDE.md" "docs/guides/google-search-console-guide.md"
move_file "MANUAL-UPDATE-INSTRUCTIONS.md" "docs/guides/manual-update-instructions.md"
move_file "QUICK-SEO-REFERENCE.md" "docs/guides/quick-seo-reference.md"
move_file "QUICK-TOC-IMPLEMENTATION.md" "docs/guides/quick-toc-implementation.md"
move_file "NAVBAR-UPDATE-CODE.md" "docs/guides/navbar-update-code.md"
move_file "REPO-REORGANIZATION-PLAN.md" "docs/guides/repo-reorganization-plan.md"
move_file "QUICK-START-GUIDE.md" "docs/guides/quick-start-guide.md"
move_file "COMPLETE-REORGANIZATION-SCRIPT.md" "docs/guides/complete-reorganization-script.md"
move_file "START-HERE.md" "docs/guides/start-here.md"
echo ""

# Documentation - Templates
echo "📁 Moving documentation (templates)..."
move_file "ARTICLE-TEMPLATE.html" "docs/templates/article-template.html"
move_file "schema-templates.html" "docs/templates/schema-templates.html"
echo ""

# Documentation - Checklists
echo "📁 Moving documentation (checklists)..."
mkdir -p "docs/checklists"
move_file "SEO-CHECKLIST.md" "docs/checklists/seo-checklist.md"
move_file "SEO-IMPLEMENTATION-CHECKLIST.md" "docs/checklists/seo-implementation-checklist.md"
move_file "ULTIMATE-SEO-GUIDE.md" "docs/checklists/ultimate-seo-guide.md"
echo ""

# Documentation - Summaries
echo "📁 Moving documentation (summaries)..."
mkdir -p "docs/summaries"
move_file "BLOG-ENHANCEMENTS-SUMMARY.md" "docs/summaries/blog-enhancements-summary.md"
move_file "BLOG-OPTIMIZATION-COMPLETE.md" "docs/summaries/blog-optimization-complete.md"
move_file "PROGRESS-UPDATE.md" "docs/summaries/progress-update.md"
move_file "UPDATE-PLAN-SUMMARY.md" "docs/summaries/update-plan-summary.md"
echo ""

# Scripts
echo "📁 Moving scripts..."
move_file "update_remaining_h1.py" "scripts/update_remaining_h1.py"
echo ""

echo "✅ File reorganization complete!"
echo ""
echo "⚠️  IMPORTANT: You still need to:"
echo "   1. Update file references in index.html"
echo "   2. Update file references in components/navbar.html"
echo "   3. Update file references in all blog pages"
echo "   4. Add favicons to blog pages"
echo ""
echo "📝 See docs/guides/complete-reorganization-script.md for details"
echo ""
echo "🔄 To commit these changes:"
echo "   git add ."
echo "   git commit -m 'Reorganize repository structure'"
echo "   git push origin main"
