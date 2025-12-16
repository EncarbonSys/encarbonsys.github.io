# 🔍 Google Search Console Setup & Submission Guide

## 📋 **Quick Setup Checklist**

### Step 1: Verify Your Site (One-Time Setup)
1. Go to [Google Search Console](https://search.google.com/search-console)
2. Click "Add Property"
3. Enter: `https://encarbonsys.com`
4. Choose verification method:
   - **Recommended:** HTML file upload
   - **Alternative:** HTML tag in `<head>`
   - **Alternative:** Google Analytics (if already installed ✅)

### Step 2: Submit Sitemaps (One-Time Setup)
1. In Search Console, go to "Sitemaps" (left sidebar)
2. Submit these sitemaps:
   - `https://encarbonsys.com/sitemap.xml` (main site)
   - `https://encarbonsys.com/sitemap-blog.xml` (blog)
3. Click "Submit"
4. Wait 24-48 hours for indexing

---

## 🚀 **After Publishing Each New Article**

### Immediate Actions (Within 1 Hour)
1. **Submit URL for Indexing**
   - Go to Search Console
   - Click "URL Inspection" (top bar)
   - Paste article URL: `https://encarbonsys.com/cbam-blog/your-article.html`
   - Click "Request Indexing"
   - Wait for confirmation

2. **Update Sitemap**
   - Edit `sitemap-blog.xml`
   - Add new article entry:
   ```xml
   <url>
       <loc>https://encarbonsys.com/cbam-blog/your-article.html</loc>
       <lastmod>2024-12-16</lastmod>
       <changefreq>monthly</changefreq>
       <priority>0.8</priority>
   </url>
   ```
   - Commit changes to GitHub
   - Resubmit sitemap in Search Console

3. **Test Rich Results**
   - Go to [Rich Results Test](https://search.google.com/test/rich-results)
   - Enter article URL
   - Verify no errors
   - Check Article schema appears

---

## 📊 **Weekly Monitoring (Every Monday)**

### Performance Tracking
1. **Check Impressions & Clicks**
   - Search Console → Performance
   - Filter: Last 7 days
   - Look for:
     - Total clicks
     - Total impressions
     - Average CTR
     - Average position

2. **Identify Top Queries**
   - Performance → Queries tab
   - Sort by impressions
   - Note queries ranking 11-20 (page 2)
   - Optimize content for these

3. **Check Coverage**
   - Search Console → Coverage
   - Look for:
     - Valid pages (should increase)
     - Errors (fix immediately)
     - Warnings (investigate)

4. **Monitor Mobile Usability**
   - Search Console → Mobile Usability
   - Fix any errors immediately
   - Test on real devices

---

## 🔧 **Monthly Deep Dive (First Monday of Month)**

### 1. Performance Analysis
- [ ] Export performance data (CSV)
- [ ] Compare to previous month
- [ ] Identify growth trends
- [ ] Note declining pages

### 2. Keyword Opportunities
- [ ] Find queries with high impressions, low clicks
- [ ] Optimize meta descriptions for these
- [ ] Update content to better match intent

### 3. Technical Health Check
- [ ] Core Web Vitals report
- [ ] Page Experience report
- [ ] Security Issues check
- [ ] Manual Actions check (should be none)

### 4. Backlink Analysis
- [ ] Links → Top linking sites
- [ ] Note new backlinks
- [ ] Identify link opportunities
- [ ] Disavow spammy links (if any)

---

## 🎯 **Key Metrics to Track**

### Success Indicators
| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Total Clicks | +50% MoM | - | 📊 |
| Total Impressions | +100% MoM | - | 📊 |
| Average CTR | >3% | - | 📊 |
| Average Position | <10 | - | 📊 |
| Indexed Pages | All published | - | 📊 |
| Mobile Usability | 0 errors | - | ✅ |
| Core Web Vitals | All green | - | ✅ |

---

## 🚨 **Common Issues & Fixes**

### Issue: "URL is not on Google"
**Fix:**
1. Check robots.txt isn't blocking
2. Verify sitemap includes URL
3. Request indexing manually
4. Wait 3-7 days
5. Check for noindex tag

### Issue: "Crawled - currently not indexed"
**Fix:**
1. Improve content quality (add 500+ words)
2. Add more internal links to page
3. Get external backlinks
4. Update content with fresh info
5. Resubmit for indexing

### Issue: "Duplicate content"
**Fix:**
1. Add canonical tag
2. Use 301 redirects
3. Consolidate similar pages
4. Add unique content

### Issue: "Mobile usability errors"
**Fix:**
1. Test on real mobile devices
2. Fix viewport settings
3. Increase font sizes (16px+)
4. Make buttons touch-friendly (48px+)
5. Remove horizontal scrolling

---

## 📱 **Mobile-First Indexing Checklist**

Google uses mobile version for indexing. Ensure:
- [ ] Mobile site has same content as desktop
- [ ] Images are optimized for mobile
- [ ] Text is readable without zooming
- [ ] Buttons are easy to tap
- [ ] No intrusive interstitials
- [ ] Fast loading on 3G/4G

---

## 🔗 **Important Links**

### Google Tools
- [Search Console](https://search.google.com/search-console)
- [Rich Results Test](https://search.google.com/test/rich-results)
- [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Structured Data Testing Tool](https://validator.schema.org/)

### Documentation
- [Search Console Help](https://support.google.com/webmasters)
- [SEO Starter Guide](https://developers.google.com/search/docs/beginner/seo-starter-guide)
- [Schema.org](https://schema.org/)

---

## 📝 **Quick Reference: URL Submission**

### For New Articles
```
1. Open Search Console
2. Click "URL Inspection" (top)
3. Paste: https://encarbonsys.com/cbam-blog/article-name.html
4. Click "Request Indexing"
5. Wait 1-3 days for indexing
```

### For Updated Articles
```
1. Same as above
2. Google will recrawl within 24-48 hours
3. Check "Last crawl" date to confirm
```

---

## 🎓 **Pro Tips**

1. **Submit URLs Immediately**
   - Don't wait for Google to discover
   - Manual submission = faster indexing

2. **Update Sitemap Weekly**
   - Keep it current
   - Remove deleted pages
   - Update lastmod dates

3. **Monitor Core Web Vitals**
   - Affects rankings directly
   - Fix issues ASAP
   - Test on real devices

4. **Optimize for Featured Snippets**
   - Use clear H2/H3 structure
   - Answer questions directly
   - Use lists and tables

5. **Track Competitors**
   - Search your target keywords
   - See who ranks #1-3
   - Analyze their content
   - Create better content

---

## 📅 **Monthly Reporting Template**

### Blog SEO Performance - [Month Year]

**Traffic**
- Organic Sessions: [number] (+/- X% vs last month)
- Page Views: [number] (+/- X% vs last month)
- Avg. Session Duration: [time]
- Bounce Rate: [percentage]

**Search Console**
- Total Clicks: [number] (+/- X% vs last month)
- Total Impressions: [number] (+/- X% vs last month)
- Average CTR: [percentage]
- Average Position: [number]

**Content**
- New Articles Published: [number]
- Total Articles: [number]
- Articles Indexed: [number]
- Articles Ranking Top 10: [number]

**Top Performing Articles**
1. [Article Title] - [clicks] clicks
2. [Article Title] - [clicks] clicks
3. [Article Title] - [clicks] clicks

**Top Keywords**
1. [Keyword] - Position [X]
2. [Keyword] - Position [X]
3. [Keyword] - Position [X]

**Issues & Actions**
- [Issue]: [Action taken]
- [Issue]: [Action taken]

**Next Month Goals**
- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

---

## ✅ **Setup Complete Checklist**

- [ ] Google Search Console verified
- [ ] Main sitemap submitted
- [ ] Blog sitemap submitted
- [ ] First article indexed
- [ ] Rich results validated
- [ ] Mobile usability checked
- [ ] Core Web Vitals reviewed
- [ ] Analytics connected
- [ ] Weekly monitoring scheduled
- [ ] Monthly reporting template ready

---

**Last Updated:** December 16, 2024  
**Next Review:** January 16, 2025

---

Need help? Contact the EnCarbonSys team!