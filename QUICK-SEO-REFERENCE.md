# ⚡ Quick SEO Reference Guide

**For**: EncarbonSys Website  
**Updated**: January 12, 2026

---

## 🚨 TOP 5 PRIORITY ACTIONS (Do First!)

### 1. Submit Sitemap to Google Search Console (5 minutes)
```
1. Go to: https://search.google.com/search-console
2. Add property: encarbonsys.com
3. Verify ownership
4. Go to Sitemaps → Add new sitemap
5. Enter: sitemap.xml
6. Click Submit
```

### 2. Add Organization Schema to Homepage (30 minutes)
```html
<!-- Copy from schema-templates.html and paste in index.html <head> -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "EncarbonSys",
  "url": "https://encarbonsys.com",
  "logo": "https://encarbonsys.com/favicon.png"
}
</script>
```

### 3. Optimize Homepage Meta Tags (30 minutes)
```html
<title>EncarbonSys - CBAM Compliance Software for Indian Exporters</title>
<meta name="description" content="Simplify EU carbon border tax compliance with EnCBAM Pro. Automated CBAM reporting for Indian exporters. Start free trial.">
```

### 4. Install Google Analytics (15 minutes)
```
1. Create GA4 property at analytics.google.com
2. Get tracking code
3. Add to all pages in <head>
4. Test with Real-Time reports
```

### 5. Create Homepage OG Image (1 hour)
```
Size: 1200x630px
Include: Logo + "CBAM Compliance Made Simple"
Save as: og-images/homepage-og.jpg
Add to meta tags
```

---

## 📋 DAILY SEO CHECKLIST

### Every Day (10 minutes)
- [ ] Check Google Search Console for errors
- [ ] Monitor organic traffic in Analytics
- [ ] Share 1 blog post on LinkedIn
- [ ] Respond to any comments/questions

### Every Week (1 hour)
- [ ] Review top performing pages
- [ ] Check keyword rankings
- [ ] Update 1 old blog post
- [ ] Build 2-3 backlinks

### Every Month (3 hours)
- [ ] Publish 2 new blog posts
- [ ] Full SEO audit
- [ ] Competitor analysis
- [ ] Update sitemap if needed

---

## 🎯 KEYWORD TARGETS

### Primary Keywords (Focus on these)
1. **CBAM compliance India** - Volume: High, Difficulty: Medium
2. **Carbon border tax exporters** - Volume: Medium, Difficulty: Low
3. **CBAM software India** - Volume: Medium, Difficulty: Low
4. **EU carbon border adjustment** - Volume: High, Difficulty: High
5. **CBAM reporting requirements** - Volume: Medium, Difficulty: Medium

### Long-tail Keywords (Easier to rank)
1. "How to comply with CBAM in India"
2. "CBAM impact on steel exporters"
3. "CBAM verification requirements 2026"
4. "CBAM calculator for Indian companies"
5. "CBAM compliance cost India"

### Where to Use Keywords
- **Title tag**: Primary keyword at the beginning
- **H1 tag**: Primary keyword (only one H1 per page)
- **First paragraph**: Primary keyword in first 100 words
- **Meta description**: Primary keyword naturally
- **URL**: Primary keyword (if possible)
- **Image alt text**: Related keywords
- **Throughout content**: 1-2% density (natural)

---

## 📝 CONTENT WRITING FORMULA

### Blog Post Structure (SEO-Optimized)
```
1. Title (H1): Include primary keyword (50-60 chars)
2. Introduction: Hook + primary keyword in first 100 words
3. Table of Contents: For posts > 1500 words
4. Main Content:
   - H2 sections with secondary keywords
   - H3 subsections
   - Short paragraphs (2-3 sentences)
   - Bullet points and lists
   - Images with alt text
5. Internal Links: 3-5 links to related articles
6. External Links: 2-3 authoritative sources
7. Conclusion: Summary + CTA
8. Related Articles: 3-5 suggestions
9. FAQ Section: With FAQ schema
```

### Ideal Content Length
- **Homepage**: 500-800 words
- **Product pages**: 800-1200 words
- **Blog posts**: 1500-2500 words
- **Guides**: 2500-4000 words

---

## 🔗 INTERNAL LINKING MAP

### Homepage Links To:
- EnCBAM_pro.html (main product)
- pricing.html (conversion)
- cbam-blog/ (content hub)
- Top 3 blog posts (featured)

### EnCBAM_pro.html Links To:
- pricing.html (CTA)
- Related blog posts (3-5)
- client_resource.html (case studies)

### Blog Posts Link To:
- Related articles (3-5)
- EnCBAM_pro.html (product mention)
- Homepage (breadcrumb)
- Other relevant posts

### Anchor Text Best Practices
✅ "Learn about CBAM compliance requirements"  
✅ "EnCBAM Pro software features"  
✅ "Complete CBAM guide for Indian exporters"  

❌ "Click here"  
❌ "Read more"  
❌ "This link"

---

## 🖼️ IMAGE OPTIMIZATION

### Image Sizes
- **OG Images**: 1200x630px (Facebook, LinkedIn)
- **Twitter Cards**: 1200x675px (16:9)
- **Blog Featured**: 1200x630px
- **In-content**: 800x450px max
- **Icons**: 512x512px

### Image Checklist
- [ ] Compress (use TinyPNG or WebP format)
- [ ] Descriptive filename (cbam-compliance-guide.jpg)
- [ ] Alt text with keywords
- [ ] Proper dimensions
- [ ] Fast loading (< 200KB)

### Alt Text Formula
```
Good: "CBAM compliance workflow diagram for Indian steel exporters"
Bad: "image1.jpg" or "diagram"
```

---

## 📊 SCHEMA MARKUP QUICK REFERENCE

### Homepage
```html
Organization + Website Schema
```

### EnCBAM_pro.html
```html
SoftwareApplication + Service Schema
```

### Blog Posts
```html
Article + Breadcrumb Schema
```

### FAQ Sections
```html
FAQPage Schema
```

### How-To Guides
```html
HowTo Schema
```

### Test Schema
```
https://validator.schema.org/
https://search.google.com/test/rich-results
```

---

## 🎨 META TAGS TEMPLATE (Copy-Paste)

```html
<!-- Essential Meta Tags -->
<title>[Page Title] - EncarbonSys | CBAM Compliance</title>
<meta name="description" content="[150-160 character description with keyword and CTA]">
<meta name="keywords" content="CBAM, carbon border tax, [specific keywords]">
<link rel="canonical" href="https://encarbonsys.com/[page-url].html">

<!-- Open Graph -->
<meta property="og:title" content="[Page Title] - EncarbonSys">
<meta property="og:description" content="[Description]">
<meta property="og:url" content="https://encarbonsys.com/[page-url].html">
<meta property="og:image" content="https://encarbonsys.com/og-images/[page]-og.jpg">
<meta property="og:type" content="website">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Page Title]">
<meta name="twitter:description" content="[Description]">
<meta name="twitter:image" content="https://encarbonsys.com/og-images/[page]-og.jpg">
```

---

## 🔍 SEO TESTING TOOLS

### Before Publishing
1. **Schema Validator**: https://validator.schema.org/
2. **Meta Tags Preview**: https://metatags.io/
3. **PageSpeed Test**: https://pagespeed.web.dev/
4. **Mobile-Friendly**: https://search.google.com/test/mobile-friendly

### After Publishing
1. **Google Search Console**: Check indexing
2. **Facebook Debugger**: https://developers.facebook.com/tools/debug/
3. **Twitter Validator**: https://cards-dev.twitter.com/validator
4. **LinkedIn Inspector**: https://www.linkedin.com/post-inspector/

---

## 📈 PERFORMANCE BENCHMARKS

### Page Speed Targets
- **Desktop**: 90+ score
- **Mobile**: 80+ score
- **Load Time**: < 3 seconds
- **First Contentful Paint**: < 1.8s

### SEO Health Targets
- **Indexed Pages**: 50+ (Month 1)
- **Organic Traffic**: 500+ visitors/month (Month 3)
- **Keyword Rankings**: 10+ in top 20 (Month 3)
- **Backlinks**: 20+ quality links (Month 6)
- **Domain Authority**: 20+ (Month 6)

---

## 🚀 QUICK WINS (Easy SEO Improvements)

### 1-Hour Tasks
- [ ] Add alt text to all images
- [ ] Fix broken internal links
- [ ] Add meta descriptions to all pages
- [ ] Create and submit sitemap
- [ ] Add schema to homepage

### 2-Hour Tasks
- [ ] Optimize all title tags
- [ ] Create OG images for top 5 pages
- [ ] Add internal links throughout site
- [ ] Write and publish 1 blog post
- [ ] Set up Google Analytics

### 1-Day Tasks
- [ ] Complete schema for all pages
- [ ] Optimize all blog posts
- [ ] Create content calendar
- [ ] Build 10 backlinks
- [ ] Full technical SEO audit

---

## 💡 SEO TIPS & TRICKS

### Content Tips
1. **Answer questions**: Use "What", "How", "Why" in titles
2. **Use numbers**: "7 Ways to...", "Top 10..."
3. **Update dates**: Keep content fresh
4. **Add examples**: Real-world case studies
5. **Include data**: Statistics and research

### Technical Tips
1. **Use HTTPS**: Always secure
2. **Mobile-first**: Design for mobile
3. **Fast loading**: Compress everything
4. **Clean URLs**: Descriptive and short
5. **Fix 404s**: Redirect broken links

### Link Building Tips
1. **Guest posting**: Write for industry blogs
2. **Resource pages**: Get listed in directories
3. **Broken link building**: Find and replace dead links
4. **Competitor backlinks**: Analyze and replicate
5. **Social sharing**: Promote on LinkedIn, Twitter

---

## 📞 HELP & RESOURCES

### Official Documentation
- **Google Search Central**: https://developers.google.com/search
- **Schema.org**: https://schema.org/
- **Google Analytics**: https://analytics.google.com/

### Learning Resources
- **Moz SEO Guide**: https://moz.com/beginners-guide-to-seo
- **Ahrefs Blog**: https://ahrefs.com/blog/
- **Search Engine Journal**: https://www.searchenginejournal.com/

### Tools
- **Google Search Console**: https://search.google.com/search-console
- **Google Analytics**: https://analytics.google.com/
- **PageSpeed Insights**: https://pagespeed.web.dev/
- **Schema Validator**: https://validator.schema.org/

---

## 🎯 THIS WEEK'S FOCUS

**Priority 1**: Submit sitemap to Google Search Console  
**Priority 2**: Add Organization Schema to homepage  
**Priority 3**: Optimize homepage meta tags  
**Priority 4**: Create homepage OG image  
**Priority 5**: Install Google Analytics

---

## 📝 NOTES

**Remember**:
- SEO takes 3-6 months to show results
- Focus on quality over quantity
- User experience comes first
- Monitor and adapt regularly
- Be patient and consistent

**Quick Contact**:
- Google Search Console Help: https://support.google.com/webmasters
- Schema Help: https://schema.org/docs/gs.html

---

*Keep this guide handy for quick reference. Update as you learn and improve!*

**Last Updated**: January 12, 2026  
**Next Review**: February 12, 2026
