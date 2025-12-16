# ⚡ Quick TOC Implementation (5-Minute Guide)

## 🎯 Goal: Add TOC Sidebar + Fix CTA Button

---

## Step 1: Add CSS (Copy-Paste)

Find `</style>` tag and add BEFORE it:

```css
.article-layout { max-width: 1400px; margin: 20px auto 60px; padding: 0 30px; display: flex; gap: 40px; }
.toc-sidebar { width: 280px; flex-shrink: 0; }
.toc-sticky { position: sticky; top: 100px; background: #f8f9fa; border-radius: 12px; padding: 25px; border: 2px solid #e9ecef; }
.toc-title { font-size: 14px; font-weight: 700; color: #0a0a0a; text-transform: uppercase; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 2px solid #2DF56D; }
.toc-list { list-style: none; padding: 0; }
.toc-list li { margin-bottom: 8px; }
.toc-list a { display: flex; align-items: center; gap: 8px; color: #495057; text-decoration: none; font-size: 14px; font-weight: 500; padding: 8px 12px; border-radius: 6px; transition: all 0.3s; }
.toc-list a:hover { background: #2DF56D; color: #0a0a0a; transform: translateX(5px); }
.toc-list a.active { background: #2DF56D; color: #0a0a0a; }
.article-container { flex: 1; max-width: 900px; }
.article-content h2 { scroll-margin-top: 100px; }
.cta-section p { color: #e0e0e0; font-size: 18px; margin-bottom: 30px; }
.cta-button { display: inline-block; background: #2DF56D; color: #0a0a0a; padding: 15px 40px; border-radius: 8px; text-decoration: none; font-weight: 700; font-size: 18px; }
@media (max-width: 1024px) { .article-layout { flex-direction: column; } .toc-sidebar { width: 100%; order: -1; } .toc-sticky { position: relative; top: 0; } }
@media (max-width: 768px) { .toc-sidebar { display: none; } }
```

Also update breadcrumb:
```css
.breadcrumb { max-width: 1400px; /* Changed from 900px */ }
```

---

## Step 2: Add HTML Structure

**FIND:**
```html
<div class="article-container">
```

**REPLACE WITH:**
```html
<div class="article-layout">
    <aside class="toc-sidebar">
        <div class="toc-sticky">
            <div class="toc-title">ON THIS PAGE</div>
            <ul class="toc-list">
                <li><a href="#section1"><i class="fas fa-chevron-right"></i> Section 1</a></li>
                <li><a href="#section2"><i class="fas fa-chevron-right"></i> Section 2</a></li>
                <li><a href="#section3"><i class="fas fa-chevron-right"></i> Section 3</a></li>
                <li><a href="#section4"><i class="fas fa-chevron-right"></i> Section 4</a></li>
                <li><a href="#section5"><i class="fas fa-chevron-right"></i> Section 5</a></li>
            </ul>
        </div>
    </aside>
    <div class="article-container">
```

**At the END, add:**
```html
    </div> <!-- Close article-container -->
</div> <!-- Close article-layout -->
```

---

## Step 3: Add IDs to H2 Tags

**BEFORE:**
```html
<h2>Your Section Title</h2>
```

**AFTER:**
```html
<h2 id="section1">Your Section Title</h2>
```

Do this for ALL H2 headings. Match IDs with TOC links.

---

## Step 4: Fix CTA Button

**FIND:**
```html
<a href="mailto:contact@encarbonsys.com" class="cta-button"></a>
```

**REPLACE WITH:**
```html
<a href="mailto:contact@encarbonsys.com" class="cta-button">Get Expert Guidance</a>
```

---

## Step 5: Add JavaScript

**BEFORE `</body>` tag, add:**

```html
<script>
document.querySelectorAll('.toc-list a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
});
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('.article-content h2[id]');
    const tocLinks = document.querySelectorAll('.toc-list a');
    let current = '';
    sections.forEach(section => {
        if (window.pageYOffset >= section.offsetTop - 150) current = section.getAttribute('id');
    });
    tocLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) link.classList.add('active');
    });
});
</script>
```

---

## ✅ Done! Test It:

1. Desktop: TOC on left, smooth scrolling works
2. Mobile: TOC hidden, article full width
3. CTA button: Text visible and clickable

---

## 📋 Checklist:

- [ ] CSS added
- [ ] HTML structure updated
- [ ] H2 tags have IDs
- [ ] TOC links match H2 IDs
- [ ] CTA button has text
- [ ] JavaScript added
- [ ] Tested on desktop
- [ ] Tested on mobile

---

**Time: 5-10 minutes per article**

**For detailed guide, see:** `ADD-TOC-SIDEBAR-GUIDE.md`