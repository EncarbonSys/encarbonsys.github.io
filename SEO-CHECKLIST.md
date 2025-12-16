# 🚀 EnCarbonSys Blog SEO Checklist

## ✅ **1. Article Optimization (Every Article Must Have)**

### Meta Tags
- [ ] **Title Tag** (50-60 characters)
  - Include primary keyword
  - Include year (2025, 2026) for freshness
  - Format: `Primary Keyword | EnCarbonSys`
  
- [ ] **Meta Description** (150-160 characters)
  - Compelling summary with CTA
  - Include primary keyword naturally
  - Mention key benefit or statistic

- [ ] **Keywords Meta** (5-10 relevant keywords)
  - Primary keyword
  - Secondary keywords
  - Long-tail variations
  - Related terms

- [ ] **Canonical URL** (prevent duplicate content)
  - `<link rel="canonical" href="https://encarbonsys.com/cbam-blog/article-name.html">`

### Open Graph & Social Media
- [ ] **OG Tags** (Facebook, LinkedIn)
  - `og:title`
  - `og:description`
  - `og:image` (1200x630px recommended)
  - `og:url`
  - `og:type` = "article"
  - `article:published_time`
  - `article:modified_time`
  - `article:author`
  - `article:section`
  - `article:tag`

- [ ] **Twitter Card**
  - `twitter:card` = "summary_large_image"
  - `twitter:title`
  - `twitter:description`
  - `twitter:image`

### Schema Markup (JSON-LD)
- [ ] **Article Schema**
  ```json
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "Article Title",
    "description": "Article description",
    "image": "image-url",
    "author": {...},
    "publisher": {...},
    "datePublished": "2024-12-16",
    "dateModified": "2024-12-16",
    "mainEntityOfPage": {...}
  }
  ```

- [ ] **Breadcrumb Schema**
  ```json
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [...]
  }
  ```

### Content Structure
- [ ] **H1 Tag** (Only ONE per page)
  - Include primary keyword
  - Compelling and descriptive
  - 50-70 characters

- [ ] **H2 Tags** (Section headers)
  - Include secondary keywords
  - Descriptive and scannable
  - 3-6 H2s per article

- [ ] **H3 Tags** (Subsections)
  - Support H2 structure
  - Include long-tail keywords
  - Clear hierarchy

- [ ] **Paragraph Length**
  - 2-4 sentences per paragraph
  - White space for readability
  - Mix short and long paragraphs

- [ ] **Lists** (Bullets & Numbers)
  - Break up text
  - Easy to scan
  - Highlight key points

### Images
- [ ] **Alt Text** (Every image)
  - Descriptive and keyword-rich
  - 125 characters max
  - Format: "Descriptive text with keyword"

- [ ] **File Names**
  - Descriptive, not "IMG_1234.jpg"
  - Use hyphens: "cbam-steel-industry.jpg"
  - Include keywords

- [ ] **Image Optimization**
  - Compressed (use TinyPNG, ImageOptim)
  - WebP format when possible
  - Lazy loading enabled
  - Responsive sizes

### Internal Links
- [ ] **Link to Main Site**
  - Homepage
  - Pricing page
  - About page
  - Contact page

- [ ] **Link to Related Articles** (3-5 links)
  - Contextual anchor text
  - Relevant articles
  - Natural placement

- [ ] **Link to Resources**
  - Client Hub
  - Tools
  - Guides

### External Links
- [ ] **Authoritative Sources** (2-3 per article)
  - Government sites (.gov)
  - Research institutions (.edu)
  - Industry publications
  - Official EU CBAM resources

- [ ] **Link Attributes**
  - `rel="nofollow"` for untrusted sources
  - `target="_blank"` for external links
  - `rel="noopener noreferrer"` for security

---

## ✅ **2. Content Strategy**

### Publishing Schedule
- [ ] **Consistency** (1-2 articles per week)
  - Monday or Wednesday (best engagement)
  - Same time each week
  - Plan 4 weeks ahead

### Content Mix
- [ ] **Beginner Content** (30%)
  - "What is CBAM?"
  - "CBAM Basics"
  - "Getting Started"

- [ ] **Intermediate Content** (40%)
  - "How to Calculate Emissions"
  - "CBAM Reporting Guide"
  - "Compliance Strategies"

- [ ] **Advanced Content** (30%)
  - "Industry-Specific Analysis"
  - "Technical Deep Dives"
  - "Future Predictions"

### Content Types
- [ ] **How-To Guides**
  - Step-by-step instructions
  - Actionable advice
  - Screenshots/examples

- [ ] **Industry Analysis**
  - Data-driven insights
  - Market trends
  - Competitive analysis

- [ ] **News & Updates**
  - Regulatory changes
  - Industry news
  - Timely commentary

- [ ] **Case Studies**
  - Real-world examples
  - Success stories
  - Lessons learned

### Keyword Research
- [ ] **Primary Keyword** (1 per article)
  - Search volume: 100-1000/month
  - Low-medium competition
  - Relevant to audience

- [ ] **Secondary Keywords** (2-3 per article)
  - Related to primary
  - Natural variations
  - Long-tail opportunities

- [ ] **LSI Keywords** (Latent Semantic Indexing)
  - Related terms
  - Synonyms
  - Context words

### Content Quality
- [ ] **Word Count** (1500-2500 words)
  - Comprehensive coverage
  - Not fluff
  - Value-packed

- [ ] **Readability**
  - Flesch Reading Ease: 60-70
  - Grade Level: 8-10
  - Short sentences
  - Simple language

- [ ] **Originality**
  - 100% unique content
  - No plagiarism
  - Original insights

- [ ] **Data & Statistics**
  - Cite sources
  - Use recent data
  - Include charts/graphs

---

## ✅ **3. Technical SEO**

### Site Speed
- [ ] **Page Load Time** (<3 seconds)
  - Compress images
  - Minify CSS/JS
  - Enable browser caching
  - Use CDN

- [ ] **Core Web Vitals**
  - LCP (Largest Contentful Paint) <2.5s
  - FID (First Input Delay) <100ms
  - CLS (Cumulative Layout Shift) <0.1

### Mobile Optimization
- [ ] **Responsive Design**
  - Mobile-first approach
  - Touch-friendly buttons
  - Readable font sizes (16px+)

- [ ] **Mobile Speed**
  - Test on real devices
  - Optimize for 3G/4G
  - Reduce mobile payload

### URL Structure
- [ ] **Clean URLs**
  - `/cbam-blog/article-name.html`
  - Lowercase only
  - Hyphens, not underscores
  - Include keywords

- [ ] **URL Length**
  - <60 characters
  - Descriptive
  - No parameters

### Breadcrumbs
- [ ] **Visual Breadcrumbs**
  - Home > Blog > Article
  - Clickable links
  - Styled clearly

- [ ] **Breadcrumb Schema**
  - JSON-LD markup
  - Proper hierarchy
  - All levels linked

### Sitemap
- [ ] **XML Sitemap** (sitemap-blog.xml)
  - All blog articles
  - Priority values (0.7-1.0)
  - Change frequency
  - Last modified dates

- [ ] **Submit to Search Engines**
  - Google Search Console
  - Bing Webmaster Tools
  - Update regularly

### Robots.txt
- [ ] **Allow Crawling**
  - `Allow: /cbam-blog/`
  - Sitemap reference
  - No blocking rules

### HTTPS
- [ ] **SSL Certificate**
  - Valid certificate
  - No mixed content
  - HTTPS everywhere

### Structured Data
- [ ] **Test with Google**
  - Rich Results Test
  - No errors
  - All properties valid

---

## ✅ **4. Link Building**

### Internal Linking Strategy
- [ ] **Hub & Spoke Model**
  - Main blog index = Hub
  - Articles = Spokes
  - Link back to hub

- [ ] **Related Articles**
  - 3-5 related links per article
  - Contextual placement
  - Descriptive anchor text

- [ ] **Link to Main Site**
  - Every article links to:
    - Pricing page
    - Contact page
    - Homepage
    - Relevant service pages

- [ ] **Link Depth**
  - All pages <3 clicks from homepage
  - No orphan pages
  - Clear navigation

### External Link Building
- [ ] **Guest Posting**
  - Industry blogs
  - Trade publications
  - Partner sites

- [ ] **Resource Pages**
  - Industry directories
  - CBAM resource lists
  - Compliance guides

- [ ] **Social Sharing**
  - LinkedIn posts
  - Twitter threads
  - Facebook groups
  - Reddit (r/sustainability)

- [ ] **Email Outreach**
  - Industry contacts
  - Journalists
  - Bloggers
  - Influencers

### Social Signals
- [ ] **Share Buttons**
  - Twitter
  - LinkedIn
  - Facebook
  - Email

- [ ] **Social Promotion**
  - Post on LinkedIn
  - Share in groups
  - Tag relevant people
  - Use hashtags

### Backlink Monitoring
- [ ] **Track Backlinks**
  - Google Search Console
  - Ahrefs (free version)
  - Ubersuggest
  - Monitor monthly

---

## 🎯 **Quick Pre-Publish Checklist**

Before publishing ANY article, verify:

1. [ ] Title tag optimized (50-60 chars, keyword included)
2. [ ] Meta description compelling (150-160 chars)
3. [ ] H1 tag present (only one)
4. [ ] H2/H3 structure logical
5. [ ] Images have alt text
6. [ ] Internal links added (3-5)
7. [ ] External links to authoritative sources (2-3)
8. [ ] Schema markup added (Article + Breadcrumb)
9. [ ] Social share buttons present
10. [ ] Related articles section included
11. [ ] Breadcrumb navigation visible
12. [ ] Mobile responsive tested
13. [ ] Page speed <3 seconds
14. [ ] No broken links
15. [ ] Spell check passed
16. [ ] Readability score 60+
17. [ ] Word count 1500-2500
18. [ ] CTA included (contact, pricing, etc.)
19. [ ] Sitemap updated
20. [ ] Submitted to Google Search Console

---

## 📊 **Post-Publish Actions**

After publishing:

1. [ ] Submit URL to Google Search Console
2. [ ] Share on LinkedIn (personal + company page)
3. [ ] Share on Twitter with hashtags
4. [ ] Post in relevant Facebook groups
5. [ ] Send to email newsletter subscribers
6. [ ] Add to content calendar
7. [ ] Monitor Google Analytics
8. [ ] Track keyword rankings
9. [ ] Respond to comments
10. [ ] Update internal links from other articles

---

## 🔧 **Free SEO Tools to Use**

### Keyword Research
- Google Keyword Planner (free)
- Ubersuggest (limited free)
- AnswerThePublic (free)
- Google Trends (free)
- Keywords Everywhere (freemium)

### Content Optimization
- Hemingway Editor (free)
- Grammarly (free version)
- Yoast SEO (WordPress, free)
- Google Docs (free)

### Technical SEO
- Google Search Console (free)
- Google Analytics (free)
- Google PageSpeed Insights (free)
- GTmetrix (free)
- Mobile-Friendly Test (free)

### Schema Markup
- Google Rich Results Test (free)
- Schema.org (free)
- JSON-LD Generator (free)

### Link Building
- Google Search Console (backlinks)
- Ubersuggest (limited free)
- Hunter.io (limited free)
- LinkedIn (free)

### Image Optimization
- TinyPNG (free)
- Squoosh (free)
- ImageOptim (free, Mac)
- GIMP (free)

---

## 📈 **Success Metrics to Track**

### Monthly Tracking
- [ ] Organic traffic (Google Analytics)
- [ ] Keyword rankings (Google Search Console)
- [ ] Backlinks (Google Search Console)
- [ ] Page views per article
- [ ] Average time on page
- [ ] Bounce rate
- [ ] Conversion rate (contact form, pricing page)

### Quarterly Goals
- [ ] 50% increase in organic traffic
- [ ] 10 new ranking keywords
- [ ] 5 new backlinks
- [ ] 1000+ page views per article
- [ ] 3+ minute average time on page
- [ ] <50% bounce rate

---

## 🎓 **SEO Best Practices Summary**

1. **Content is King** - Write for humans first, search engines second
2. **Consistency Matters** - Publish regularly (1-2x per week)
3. **Quality Over Quantity** - One great article > five mediocre ones
4. **Internal Linking** - Connect your content strategically
5. **Mobile First** - Most traffic is mobile
6. **Speed Matters** - Fast sites rank better
7. **User Experience** - Easy to read, navigate, and share
8. **Data-Driven** - Use analytics to improve
9. **Long-Term Game** - SEO takes 3-6 months to show results
10. **Keep Learning** - SEO evolves constantly

---

**Last Updated:** December 16, 2024  
**Next Review:** March 16, 2025

---

Need help with SEO? Contact the EnCarbonSys team!