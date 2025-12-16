# 📘 Guide: Add TOC Sidebar & Fix CTA Buttons

## 🎯 What We're Adding:

1. **Sticky Table of Contents (TOC)** - Left sidebar with section links
2. **Fixed CTA Button** - Visible text on mailto buttons
3. **Smooth Scrolling** - Click TOC links to jump to sections
4. **Active Highlighting** - Current section highlighted in TOC

---

## 🔧 Step-by-Step Implementation

### **STEP 1: Update CSS Styles**

Find the `<style>` section in your article and **ADD** these new styles:

```css
/* Main Layout with Sidebar */
.article-layout {
    max-width: 1400px;
    margin: 20px auto 60px;
    padding: 0 30px;
    display: flex;
    gap: 40px;
    position: relative;
}

/* Table of Contents Sidebar */
.toc-sidebar {
    width: 280px;
    flex-shrink: 0;
}

.toc-sticky {
    position: sticky;
    top: 100px;
    background: #f8f9fa;
    border-radius: 12px;
    padding: 25px;
    border: 2px solid #e9ecef;
}

.toc-title {
    font-size: 14px;
    font-weight: 700;
    color: #0a0a0a;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 2px solid #2DF56D;
}

.toc-list {
    list-style: none;
    padding: 0;
}

.toc-list li {
    margin-bottom: 8px;
}

.toc-list a {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #495057;
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    padding: 8px 12px;
    border-radius: 6px;
    transition: all 0.3s;
}

.toc-list a:hover {
    background: #2DF56D;
    color: #0a0a0a;
    transform: translateX(5px);
}

.toc-list a.active {
    background: #2DF56D;
    color: #0a0a0a;
}

.toc-list a i {
    font-size: 10px;
    opacity: 0.6;
}

/* Update Article Container */
.article-container {
    flex: 1;
    max-width: 900px;
}

/* Add scroll margin to h2 for smooth scrolling */
.article-content h2 {
    scroll-margin-top: 100px;
}

/* Fix CTA Button Text Visibility */
.cta-section p {
    color: #e0e0e0;
    font-size: 18px;
    margin-bottom: 30px;
}

.cta-button {
    display: inline-block;
    background: #2DF56D;
    color: #0a0a0a;
    padding: 15px 40px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 700;
    font-size: 18px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* Mobile Responsive Updates */
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
    }
}

@media (max-width: 768px) {
    .toc-sidebar {
        display: none;
    }
}
```

Also **UPDATE** the breadcrumb max-width:

```css
.breadcrumb {
    max-width: 1400px;  /* Changed from 900px */
    margin: 90px auto 0;
    padding: 15px 30px;
    font-size: 14px;
}
```

---

### **STEP 2: Update HTML Structure**

**FIND** this line in your HTML:
```html
<div class="article-container">
```

**REPLACE** with:
```html
<div class="article-layout">
    <!-- Table of Contents Sidebar -->
    <aside class="toc-sidebar">
        <div class="toc-sticky">
            <div class="toc-title">ON THIS PAGE</div>
            <ul class="toc-list">
                <!-- ADD YOUR SECTIONS HERE - Example: -->
                <li><a href="#understanding-cbam"><i class="fas fa-chevron-right"></i> Understanding CBAM's Impact</a></li>
                <li><a href="#cost-implications"><i class="fas fa-chevron-right"></i> Cost Implications</a></li>
                <li><a href="#green-steel"><i class="fas fa-chevron-right"></i> Green Steel Advantage</a></li>
                <li><a href="#industry-adaptation"><i class="fas fa-chevron-right"></i> Industry Adaptation</a></li>
                <li><a href="#future-outlook"><i class="fas fa-chevron-right"></i> Future Outlook</a></li>
                <li><a href="#conclusion"><i class="fas fa-chevron-right"></i> Conclusion</a></li>
            </ul>
        </div>
    </aside>

    <!-- Main Article Content -->
    <div class="article-container">
```

**IMPORTANT:** At the END of your article, before the closing tags, add:
```html
    </div> <!-- Close article-container -->
</div> <!-- Close article-layout -->
```

---

### **STEP 3: Add IDs to Your H2 Headings**

For each `<h2>` heading in your article, add an `id` attribute that matches the TOC links:

**BEFORE:**
```html
<h2>Understanding CBAM's Impact on Steel</h2>
```

**AFTER:**
```html
<h2 id="understanding-cbam">Understanding CBAM's Impact on Steel</h2>
```

**Example IDs for common sections:**
- `id="understanding-cbam"`
- `id="cost-implications"`
- `id="green-steel"`
- `id="industry-adaptation"`
- `id="future-outlook"`
- `id="conclusion"`

---

### **STEP 4: Fix CTA Button**

**FIND** your CTA section (usually looks like this):
```html
<div class="cta-section">
    <h2>Need Help with CBAM Compliance?</h2>
    <p style="margin-bottom: 30px;">EnCarbonSys provides...</p>
    <a href="mailto:contact@encarbonsys.com" class="cta-button"></a>
</div>
```

**UPDATE** to:
```html
<div class="cta-section">
    <h2>Need Help with CBAM Compliance?</h2>
    <p>EnCarbonSys provides comprehensive CBAM compliance solutions. <a href="/pricing.html" style="color: #2DF56D; border-bottom: 2px solid #2DF56D;">View our affordable pricing plans</a>.</p>
    <a href="mailto:contact@encarbonsys.com" class="cta-button">Get Expert Guidance</a>
</div>
```

**Key Changes:**
1. Removed inline `style="margin-bottom: 30px;"` from `<p>` tag
2. Added visible button text: **"Get Expert Guidance"**
3. Made button text bold with `font-weight: 700` in CSS

---

### **STEP 5: Add JavaScript for Smooth Scrolling**

**FIND** the closing `</body>` tag and **ADD** this JavaScript BEFORE it:

```html
<script>
    fetch('/navbar.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('navbar-placeholder').innerHTML = data;
        });

    // Smooth scroll for TOC links
    document.querySelectorAll('.toc-list a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Highlight active section in TOC
    window.addEventListener('scroll', () => {
        const sections = document.querySelectorAll('.article-content h2[id]');
        const tocLinks = document.querySelectorAll('.toc-list a');
        
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (window.pageYOffset >= sectionTop - 150) {
                current = section.getAttribute('id');
            }
        });

        tocLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
</script>
```

---

## 📋 Quick Checklist

For each article, verify:

- [ ] CSS styles added (TOC sidebar, layout, responsive)
- [ ] Breadcrumb max-width updated to 1400px
- [ ] HTML structure wrapped with `article-layout` and `toc-sidebar`
- [ ] TOC links match your article's H2 sections
- [ ] All H2 headings have `id` attributes
- [ ] CTA button has visible text ("Get Expert Guidance")
- [ ] CTA paragraph styling fixed
- [ ] JavaScript added for smooth scrolling and active highlighting
- [ ] Mobile responsive (TOC hidden on mobile)
- [ ] Tested on desktop and mobile

---

## 🎨 Customizing TOC for Each Article

### **Example 1: CBAM Verification Requirements 2026**

```html
<ul class="toc-list">
    <li><a href="#2026-mandate"><i class="fas fa-chevron-right"></i> The 2026 Verification Mandate</a></li>
    <li><a href="#site-visits"><i class="fas fa-chevron-right"></i> Mandatory Physical Site Visits</a></li>
    <li><a href="#accredited-verifiers"><i class="fas fa-chevron-right"></i> Accredited Verifiers</a></li>
    <li><a href="#verification-standards"><i class="fas fa-chevron-right"></i> Verification Standards</a></li>
    <li><a href="#documentation"><i class="fas fa-chevron-right"></i> Documentation Requirements</a></li>
    <li><a href="#penalties"><i class="fas fa-chevron-right"></i> Penalties & Consequences</a></li>
    <li><a href="#timeline"><i class="fas fa-chevron-right"></i> Key Dates Timeline</a></li>
    <li><a href="#action-steps"><i class="fas fa-chevron-right"></i> Preparing for Success</a></li>
</ul>
```

Then add matching IDs to H2 tags:
```html
<h2 id="2026-mandate">The 2026 Verification Mandate: What's Changing</h2>
<h2 id="site-visits">Mandatory Physical Site Visits</h2>
<h2 id="accredited-verifiers">Accredited Verifiers: Who Can Verify Your Data?</h2>
<!-- etc. -->
```

---

### **Example 2: CBAM Impact on Steel Industry**

```html
<ul class="toc-list">
    <li><a href="#understanding-cbam"><i class="fas fa-chevron-right"></i> Understanding CBAM's Impact</a></li>
    <li><a href="#cost-implications"><i class="fas fa-chevron-right"></i> Cost Implications</a></li>
    <li><a href="#green-steel"><i class="fas fa-chevron-right"></i> Green Steel Advantage</a></li>
    <li><a href="#industry-adaptation"><i class="fas fa-chevron-right"></i> Industry Adaptation</a></li>
    <li><a href="#regional-impact"><i class="fas fa-chevron-right"></i> Regional Impact</a></li>
    <li><a href="#future-outlook"><i class="fas fa-chevron-right"></i> Future Outlook</a></li>
</ul>
```

---

### **Example 3: Authorised Declarant Guide**

```html
<ul class="toc-list">
    <li><a href="#why-needed"><i class="fas fa-chevron-right"></i> Why You Need This Status</a></li>
    <li><a href="#application-process"><i class="fas fa-chevron-right"></i> Application Process</a></li>
    <li><a href="#compliance-checks"><i class="fas fa-chevron-right"></i> Compliance Checks</a></li>
    <li><a href="#key-deadlines"><i class="fas fa-chevron-right"></i> Key Deadlines</a></li>
    <li><a href="#rejection-handling"><i class="fas fa-chevron-right"></i> If Application Rejected</a></li>
    <li><a href="#preparation"><i class="fas fa-chevron-right"></i> How to Prepare Now</a></li>
</ul>
```

---

## 🚀 Benefits of TOC Sidebar

1. **Better UX** - Easy navigation to specific sections
2. **Lower Bounce Rate** - Users can quickly find what they need
3. **Increased Time on Page** - Encourages exploration
4. **SEO Boost** - Better user engagement signals
5. **Professional Look** - Matches industry-leading blogs
6. **Mobile-Friendly** - Automatically hidden on small screens

---

## 🎯 Testing Your Implementation

1. **Desktop View:**
   - TOC sidebar visible on left
   - Clicking TOC links smoothly scrolls to sections
   - Active section highlighted in green
   - CTA button text visible

2. **Tablet View (1024px):**
   - TOC moves to top of article
   - Still functional and visible

3. **Mobile View (768px):**
   - TOC completely hidden
   - Article takes full width
   - CTA button still visible and clickable

---

## 📊 Before & After Comparison

### **BEFORE:**
- ❌ No quick navigation
- ❌ Users scroll endlessly
- ❌ CTA button text invisible
- ❌ Basic article layout

### **AFTER:**
- ✅ Sticky TOC sidebar
- ✅ One-click section navigation
- ✅ CTA button clearly visible
- ✅ Professional blog layout
- ✅ Active section highlighting
- ✅ Smooth scrolling
- ✅ Mobile-responsive

---

## 💡 Pro Tips

1. **Keep TOC Short** - Max 6-8 items for best UX
2. **Use Clear Labels** - Make section names descriptive
3. **Match H2 Headings** - TOC should mirror article structure
4. **Test Scrolling** - Ensure smooth scroll works on all browsers
5. **Check Mobile** - Verify TOC hidden on small screens

---

## 🔧 Troubleshooting

**Problem:** TOC not sticking
- **Solution:** Check `position: sticky` and `top: 100px` in CSS

**Problem:** Smooth scroll not working
- **Solution:** Verify JavaScript is before `</body>` tag

**Problem:** Active highlighting not working
- **Solution:** Ensure all H2 tags have `id` attributes

**Problem:** CTA button text still invisible
- **Solution:** Check button has text content and `font-weight: 700`

**Problem:** TOC showing on mobile
- **Solution:** Verify media query `@media (max-width: 768px)` hides TOC

---

## 📁 Files to Update

Apply these changes to:

1. ✅ `ARTICLE-TEMPLATE.html` - **DONE**
2. ⏳ `cbam-impact-steel-industry.html`
3. ⏳ `cbam-verification-requirements-2026.html`
4. ⏳ `cbam-developing-countries-impact.html`
5. ⏳ `authorised-declarant-guide.html`
6. ⏳ `cbam-omnibus-new-rules.html`
7. ⏳ `cbam-six-pains-predictions.html`
8. ⏳ `cbam-updates-april-2025.html`
9. ⏳ `navigating-cbam-changes.html`
10. ⏳ `supplier-data-management.html`

---

**Time Required:** 15-20 minutes per article

**Difficulty:** Easy (copy-paste with minor customization)

**Impact:** High (significantly improves UX and engagement)

---

**Ready to implement? Start with one article and test thoroughly before applying to all!** 🚀