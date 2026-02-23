import os
import re

root_dir = r'c:\Users\ASUS\Desktop\ENCARBONSYS\WEBSITE\WEBSIT GIT CLONE REPO\encarbonsys.github.io'

GA_SNIPPET = '''    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-5KSFR9S0QX"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-5KSFR9S0QX');
    </script>
'''

# Article schema for each blog page: url -> {datePublished, dateModified, headline, description, keywords}
ARTICLE_META = {
    'authorised-declarant-guide.html': {
        'url': 'https://encarbonsys.com/cbam-blog/authorised-declarant-guide.html',
        'headline': 'Your Roadmap to Becoming an Authorised CBAM Declarant',
        'datePublished': '2025-03-21',
        'dateModified': '2026-02-23',
        'description': 'Complete guide to becoming a CBAM Authorised Declarant. Learn the application process, requirements, and deadlines to maintain EU market access.',
        'keywords': 'CBAM authorised declarant, CBAM declarant application, CBAM 2026 compliance, EU CBAM',
    },
    'cbam-2026-definitive-phase-guide.html': {
        'url': 'https://encarbonsys.com/cbam-blog/cbam-2026-definitive-phase-guide.html',
        'headline': 'CBAM 2026 Definitive Phase: Your Complete Compliance Roadmap',
        'datePublished': '2025-01-10',
        'dateModified': '2026-02-23',
        'description': 'Everything EU importers need to know about the 2026 CBAM definitive phase: authorization, certificate management, and compliance deadlines.',
        'keywords': 'CBAM 2026, CBAM definitive phase, CBAM certificates, EU carbon border adjustment 2026',
    },
    'cbam-developing-countries-impact.html': {
        'url': 'https://encarbonsys.com/cbam-blog/cbam-developing-countries-impact.html',
        'headline': 'The Global South vs CBAM: Trade Barriers or Climate Justice?',
        'datePublished': '2024-12-16',
        'dateModified': '2026-02-23',
        'description': "Examining CBAM's impact on developing nations including India, Turkey, and African countries. Explore challenges, equity concerns, and strategic responses.",
        'keywords': 'CBAM developing countries, CBAM India impact, CBAM Global South, carbon border tax exporters',
    },
    'cbam-impact-steel-industry.html': {
        'url': 'https://encarbonsys.com/cbam-blog/cbam-impact-steel-industry.html',
        'headline': "Steel Under Pressure: CBAM's Impact on Global Metal Markets",
        'datePublished': '2024-12-16',
        'dateModified': '2026-02-23',
        'description': 'CBAM is transforming global steel trade. From cost implications to advantages for green steel producers, here is how the industry is adapting.',
        'keywords': 'CBAM steel, CBAM aluminum, carbon border adjustment steel, EU steel exports compliance',
    },
    'cbam-india-exporters-guide-2026.html': {
        'url': 'https://encarbonsys.com/cbam-blog/cbam-india-exporters-guide-2026.html',
        'headline': 'CBAM 2026 for Indian Exporters: Your Complete Compliance Roadmap',
        'datePublished': '2025-01-15',
        'dateModified': '2026-02-23',
        'description': 'Comprehensive CBAM guide for Indian manufacturers exporting steel, aluminum, cement, and fertilizers to the EU. Data collection, verification, cost implications.',
        'keywords': 'CBAM India, CBAM Indian exporters, CBAM steel India, carbon compliance India EU, CBAM 2026 India',
    },
    'cbam-omnibus-new-rules.html': {
        'url': 'https://encarbonsys.com/cbam-blog/cbam-omnibus-new-rules.html',
        'headline': 'CBAM Omnibus Explained: Simpler Rules, Same Climate Goals',
        'datePublished': '2025-04-30',
        'dateModified': '2026-02-23',
        'description': 'The European Parliament approved major CBAM Omnibus simplifications reducing admin burden while keeping climate goals intact. What importers need to know.',
        'keywords': 'CBAM Omnibus, CBAM simplification 2025, EU CBAM new rules, CBAM regulatory update',
    },
    'cbam-six-pains-predictions.html': {
        'url': 'https://encarbonsys.com/cbam-blog/cbam-six-pains-predictions.html',
        'headline': 'Six CBAM Myths Debunked: What is Real, What is Hype',
        'datePublished': '2024-05-29',
        'dateModified': '2026-02-23',
        'description': 'Will the EU water down CBAM requirements? Will compliance cost too much? We assess six key claims about CBAM implementation and separate fact from fiction.',
        'keywords': 'CBAM myths, CBAM predictions, CBAM compliance cost, is CBAM real, CBAM 2026 fears',
    },
    'cbam-updates-april-2025.html': {
        'url': 'https://encarbonsys.com/cbam-blog/cbam-updates-april-2025.html',
        'headline': 'April 2025 CBAM Update: New Thresholds, New Rules, New Reality',
        'datePublished': '2025-04-15',
        'dateModified': '2026-02-23',
        'description': 'April 2025 brings critical CBAM updates. From reporting deadlines to new compliance requirements, here is everything you need to stay on track.',
        'keywords': 'CBAM April 2025, CBAM updates 2025, CBAM quarterly reporting, CBAM new thresholds',
    },
    'cbam-verification-requirements-2026.html': {
        'url': 'https://encarbonsys.com/cbam-blog/cbam-verification-requirements-2026.html',
        'headline': '2026 CBAM Verification: Everything You Need to Pass the Audit',
        'datePublished': '2024-12-17',
        'dateModified': '2026-02-23',
        'description': 'Starting January 2026, CBAM enters its definitive phase with mandatory verification requirements. Everything importers need to know about accredited verifiers.',
        'keywords': 'CBAM verification 2026, CBAM accredited verifier, CBAM audit, CBAM site visit',
    },
    'hs-hsn-cn-taric-codes-complete-guide.html': {
        'url': 'https://encarbonsys.com/cbam-blog/hs-hsn-cn-taric-codes-complete-guide.html',
        'headline': 'HS vs HSN vs CN vs TARIC Codes: Complete CBAM Guide for Indian Exporters',
        'datePublished': '2025-05-10',
        'dateModified': '2026-02-23',
        'description': 'Confused about customs codes for CBAM? This definitive guide clears up HS, HSN, CN, and TARIC codes for Indian exporters navigating EU CBAM compliance.',
        'keywords': 'HS code CBAM, CN code CBAM, TARIC code CBAM, HSN code EU export, CBAM product codes India',
    },
    'navigating-cbam-changes.html': {
        'url': 'https://encarbonsys.com/cbam-blog/navigating-cbam-changes.html',
        'headline': 'Navigating CBAM Changes: What Importers Must Prepare For',
        'datePublished': '2025-02-26',
        'dateModified': '2026-02-23',
        'description': "The European Commission's CBAM updates introduce key simplifications. Learn what importers and manufacturers need to prepare for the 2026 definitive phase.",
        'keywords': 'CBAM changes 2025, CBAM importer preparation, CBAM regulatory changes, EU CBAM update',
    },
    'supplier-data-management.html': {
        'url': 'https://encarbonsys.com/cbam-blog/supplier-data-management.html',
        'headline': 'From Data Chaos to CBAM Compliance: A Supplier Management Blueprint',
        'datePublished': '2025-03-10',
        'dateModified': '2026-02-23',
        'description': 'Managing supplier emissions data for CBAM does not have to be chaotic. Learn how to streamline data collection and ensure compliance with our practical guide.',
        'keywords': 'CBAM supplier data, CBAM data management, carbon data collection EU, CBAM supplier catalogue',
    },
}

def build_article_schema(meta):
    return f'''    <!-- JSON-LD Article Schema -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "Article",
          "headline": "{meta['headline']}",
          "description": "{meta['description']}",
          "url": "{meta['url']}",
          "datePublished": "{meta['datePublished']}",
          "dateModified": "{meta['dateModified']}",
          "author": {{
            "@type": "Organization",
            "name": "EnCarbonSys",
            "url": "https://encarbonsys.com"
          }},
          "publisher": {{
            "@type": "Organization",
            "name": "EnCarbonSys",
            "url": "https://encarbonsys.com",
            "logo": {{
              "@type": "ImageObject",
              "url": "https://image2url.com/images/1754762251826-aabbb9f2-5d26-42f3-b2a7-896ce713de40.png"
            }}
          }},
          "keywords": "{meta['keywords']}",
          "inLanguage": "en",
          "isPartOf": {{
            "@type": "Blog",
            "name": "EnCarbonSys CBAM Blog",
            "url": "https://encarbonsys.com/cbam-blog/"
          }}
        }},
        {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://encarbonsys.com/"}},
            {{"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://encarbonsys.com/cbam-blog/"}},
            {{"@type": "ListItem", "position": 3, "name": "{meta['headline']}", "item": "{meta['url']}"}}
          ]
        }}
      ]
    }}
    </script>
'''

blog_dir = os.path.join(root_dir, 'cbam-blog')

for filename, meta in ARTICLE_META.items():
    filepath = os.path.join(blog_dir, filename)
    if not os.path.exists(filepath):
        print(f"SKIP (not found): {filename}")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # 1. Add GA if missing
    if 'G-5KSFR9S0QX' not in content:
        content = content.replace('<meta charset="UTF-8">', GA_SNIPPET + '    <meta charset="UTF-8">', 1)
        changed = True
        print(f"  + GA added to {filename}")

    # 2. Add Article schema if missing
    if 'application/ld+json' not in content:
        schema = build_article_schema(meta)
        # Insert before </head>
        content = content.replace('</head>', schema + '</head>', 1)
        changed = True
        print(f"  + Schema added to {filename}")

    # 3. Add canonical if missing
    canonical = f'    <link rel="canonical" href="{meta["url"]}" />\n'
    if 'rel="canonical"' not in content:
        content = content.replace('</head>', canonical + '</head>', 1)
        changed = True
        print(f"  + Canonical added to {filename}")

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  SAVED: {filename}")
    else:
        print(f"  OK (no changes): {filename}")

print("\nDone.")
