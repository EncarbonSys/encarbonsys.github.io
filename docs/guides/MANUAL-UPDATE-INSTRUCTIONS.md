# 📝 MANUAL UPDATE INSTRUCTIONS

## ⚠️ Important Note

The article files are too large (30+ KB) for automated batch updates through the GitHub API. 

**Two options:**

### **Option 1: Manual Updates (Recommended - 100% Free)**
Follow the step-by-step guide below. Takes 10-15 min per article.

### **Option 2: Local Git Clone (Fastest)**
Clone the repo locally, make changes, push back. Takes 30 min total for all articles.

---

## 🎯 OPTION 1: Manual Update Guide

### **For Each Article:**

#### **STEP 1: Open Article in GitHub**
1. Go to: `https://github.com/EncarbonSys/encarbonsys.github.io`
2. Navigate to `cbam-blog/[article-name].html`
3. Click the **pencil icon** (Edit this file)

#### **STEP 2: Add CSS**
Find the line with `</style>` and ADD THIS BEFORE IT:

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

.article-container {
    flex: 1;
    max-width: 900px;
}

.article-content h2 {
    scroll-margin-top: 100px;
}

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

.cta-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(45, 245, 109, 0.3);
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
    }
}

@media (max-width: 768px) {
    .toc-sidebar {
        display: none;
    }
}
```

Also CHANGE this line:
```css
.breadcrumb {
    max-width: 900px;  /* CHANGE TO: max-width: 1400px; */
```

#### **STEP 3: Update HTML Structure**

**FIND:**
```html
<div class="article-container">
    <a href="/cbam-blog/" class="back-link">
```

**REPLACE WITH:**
```html
<div class="article-layout">
    <aside class="toc-sidebar">
        <div class="toc-sticky">
            <div class="toc-title">ON THIS PAGE</div>
            <ul class="toc-list">
                <!-- ADD ARTICLE-SPECIFIC LINKS HERE - See below -->
            </ul>
        </div>
    </aside>
    <div class="article-container">
        <a href="/cbam-blog/" class="back-link">
```

**AT THE END, FIND:**
```html
    </div>

    <script>
        fetch('/navbar.html')
```

**REPLACE WITH:**
```html
        </div> <!-- Close article-container -->
    </div> <!-- Close article-layout -->

    <script>
        fetch('/navbar.html')
```

#### **STEP 4: Add TOC Links**

See `FINAL-IMPLEMENTATION-GUIDE.md` for article-specific TOC links.

#### **STEP 5: Add IDs to H2 Tags**

For each `<h2>` heading, add an `id` attribute matching the TOC links.

**Example:**
```html
<h2 id="disruption">The Disruption: How CBAM Changes Everything</h2>
```

#### **STEP 6: Fix CTA Button**

**FIND:**
```html
<a href="mailto:contact@encarbonsys.com" class="cta-button"></a>
```

**REPLACE WITH:**
```html
<a href="mailto:contact@encarbonsys.com" class="cta-button">Get Expert Guidance</a>
```

#### **STEP 7: Add JavaScript**

**FIND:**
```html
    <script>
        fetch('/navbar.html')
            .then(response => response.text())
            .then(data => {
                document.getElementById('navbar-placeholder').innerHTML = data;
            });
    </script>
</body>
```

**REPLACE WITH:**
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
</body>
```

#### **STEP 8: Commit Changes**

1. Scroll to bottom
2. Add commit message: "Add TOC sidebar and fix CTA button"
3. Click **Commit changes**

---

## 🎯 OPTION 2: Local Git Clone (Fastest)

```bash
# Clone the repository
git clone https://github.com/EncarbonSys/encarbonsys.github.io.git
cd encarbonsys.github.io

# Make changes to all files locally using your favorite editor

# Commit and push
git add cbam-blog/*.html
git commit -m "Add TOC sidebar and fix CTA buttons to all blog articles"
git push origin main
```

---

## 📋 Article-Specific TOC Links

### **cbam-impact-steel-industry.html**
```html
<li><a href="#disruption"><i class="fas fa-chevron-right"></i> The Disruption</a></li>
<li><a href="#cost-implications"><i class="fas fa-chevron-right"></i> Cost Implications</a></li>
<li><a href="#green-steel"><i class="fas fa-chevron-right"></i> Green Steel Advantage</a></li>
<li><a href="#industry-adaptation"><i class="fas fa-chevron-right"></i> Industry Adaptation</a></li>
<li><a href="#automotive-construction"><i class="fas fa-chevron-right"></i> Automotive & Construction</a></li>
<li><a href="#regional-responses"><i class="fas fa-chevron-right"></i> Regional Responses</a></li>
<li><a href="#future"><i class="fas fa-chevron-right"></i> Future Outlook</a></li>
```

### **cbam-verification-requirements-2026.html**
```html
<li><a href="#2026-mandate"><i class="fas fa-chevron-right"></i> 2026 Verification Mandate</a></li>
<li><a href="#site-visits"><i class="fas fa-chevron-right"></i> Physical Site Visits</a></li>
<li><a href="#accredited-verifiers"><i class="fas fa-chevron-right"></i> Accredited Verifiers</a></li>
<li><a href="#verification-standards"><i class="fas fa-chevron-right"></i> Verification Standards</a></li>
<li><a href="#documentation"><i class="fas fa-chevron-right"></i> Documentation Required</a></li>
<li><a href="#penalties"><i class="fas fa-chevron-right"></i> Penalties & Consequences</a></li>
```

(See `FINAL-IMPLEMENTATION-GUIDE.md` for all other articles)

---

## ✅ Verification Checklist

After updating each article:

- [ ] CSS added before `</style>`
- [ ] Breadcrumb max-width changed to 1400px
- [ ] HTML structure wrapped with `article-layout`
- [ ] TOC sidebar added with article-specific links
- [ ] All H2 tags have `id` attributes
- [ ] CTA button has visible text
- [ ] JavaScript added before `</body>`
- [ ] File saved and committed

---

## 🚀 Alternative: I Can Create Individual PRs

If you prefer, I can:
1. Create a branch for each article
2. Make the changes
3. Create pull requests
4. You review and merge

**Would you like me to try this approach instead?**

---

**Time Estimate:**
- Manual: 10-15 min per article = 90-135 min total
- Local Git: 30-45 min total
- PR approach: 60-90 min total

**Which method would you prefer?** 🤔