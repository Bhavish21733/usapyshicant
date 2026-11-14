#!/usr/bin/env python3
"""
9th Chakra Psychic — Master Static Site Builder
Generates all 18+ pages, clean URL directories, XML Sitemap, and robots.txt.
"""

import os
import sys

# Ensure pages package can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pages.home import render_home
from pages.about import render_about
from pages.services_index import render_services_index
from pages.services_detail import render_service_page, get_service_data
from pages.blog import render_blog_index, render_article_1, render_article_2, render_article_3
from pages.gallery import render_gallery
from pages.contact import render_contact
from pages.legal import render_privacy_policy, render_disclaimer
from pages.not_found import render_404

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://9thchakropsychic.com"  # Canonical production domain

def get_header(current_page, depth=0):
    rel = "../" * depth
    logo_src = f"{rel}assets/images/logo.png"

    # Active states (Neutral navigation without page status indicators)
    is_home = ""
    is_about = ""
    is_services = ""
    is_blog = ""
    is_gallery = ""
    is_contact = ""

    home_href = f"{rel}index.html"
    about_href = f"{rel}about.html"
    services_href = f"{rel}services.html"
    blog_href = f"{rel}blog.html"
    gallery_href = f"{rel}gallery.html"
    contact_href = f"{rel}contact.html"

    s_tarot = f"{rel}services/tarot-reading.html"
    s_psychic = f"{rel}services/psychic-reading.html"
    s_medium = f"{rel}services/medium-reading.html"
    s_energy = f"{rel}services/energy-healing.html"
    s_chakra = f"{rel}services/chakra-balancing-aura-cleansing.html"
    s_holistic = f"{rel}services/holistic-counseling.html"
    s_meditation = f"{rel}services/meditation.html"

    return f"""
  <header class="site-header" role="banner">
    <div class="container header-container">
      <a href="{home_href}" class="brand-link" aria-label="9th Chakra Psychic Homepage">
        <img src="{logo_src}" alt="9th Chakra Psychic — Spiritual Guidance &amp; Readings" class="brand-logo" width="220" height="73" />
      </a>

      <nav class="nav-desktop" role="navigation" aria-label="Main Navigation">
        <ul class="nav-desktop-list">
          <li class="nav-item">
            <a href="{home_href}" class="nav-link {is_home}">Home</a>
          </li>
          <li class="nav-item">
            <a href="{about_href}" class="nav-link {is_about}">About Us</a>
          </li>
          <li class="nav-item has-dropdown">
            <a href="{services_href}" class="nav-link {is_services}" aria-haspopup="true" aria-expanded="false">
              Services
              <svg class="dropdown-chevron" viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">
                <path d="M1 1l4 4 4-4" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </a>
            <ul class="dropdown-menu" role="menu" aria-label="Services Submenu">
              <li role="none"><a href="{s_tarot}" class="dropdown-link" role="menuitem"><span class="dropdown-link-badge"></span>Tarot Reading</a></li>
              <li role="none"><a href="{s_psychic}" class="dropdown-link" role="menuitem"><span class="dropdown-link-badge"></span>Psychic Reading</a></li>
              <li role="none"><a href="{s_medium}" class="dropdown-link" role="menuitem"><span class="dropdown-link-badge"></span>Medium Reading</a></li>
              <li role="none"><a href="{s_energy}" class="dropdown-link" role="menuitem"><span class="dropdown-link-badge"></span>Reiki &amp; Seichim Healing</a></li>
              <li role="none"><a href="{s_chakra}" class="dropdown-link" role="menuitem"><span class="dropdown-link-badge"></span>Chakra Balancing &amp; Aura Cleansing</a></li>
              <li role="none"><a href="{s_holistic}" class="dropdown-link" role="menuitem"><span class="dropdown-link-badge"></span>Holistic Guidance</a></li>
              <li role="none"><a href="{s_meditation}" class="dropdown-link" role="menuitem"><span class="dropdown-link-badge"></span>Meditation</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a href="{blog_href}" class="nav-link {is_blog}">Blog</a>
          </li>
          <li class="nav-item">
            <a href="{gallery_href}" class="nav-link {is_gallery}">Gallery</a>
          </li>
          <li class="nav-item">
            <a href="{contact_href}" class="nav-link {is_contact}">Contact Us</a>
          </li>
        </ul>
      </nav>

      <div class="header-actions">
        <a href="tel:+12148998311" class="header-phone-btn" title="Call for a Private Reading">
          <svg class="header-phone-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
          </svg>
          <span>+1 (214) 899-8311</span>
        </a>
      </div>

      <button type="button" class="menu-toggle" aria-label="Toggle Navigation Menu" aria-expanded="false" aria-controls="mobileDrawer">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
    </div>

    <!-- Mobile Drawer Overlay -->
    <div class="mobile-nav-overlay" id="mobileOverlay" aria-hidden="true"></div>
    <div class="mobile-nav-drawer" id="mobileDrawer" role="dialog" aria-modal="true" aria-label="Mobile Navigation" aria-hidden="true">
      <div class="mobile-nav-header">
        <img src="{logo_src}" alt="9th Chakra Psychic" style="height:36px; width:auto;" />
        <button type="button" class="mobile-close-btn" aria-label="Close Navigation Menu">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
      </div>

      <ul class="mobile-nav-list">
        <li><a href="{home_href}" class="mobile-nav-link {is_home}">Home</a></li>
        <li><a href="{about_href}" class="mobile-nav-link {is_about}">About Us</a></li>
        <li>
          <a href="{services_href}" class="mobile-nav-link mobile-services-trigger {is_services}" aria-expanded="false">
            Services
            <svg width="12" height="12" viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M1 1l4 4 4-4" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
          <ul class="mobile-services-accordion">
            <li><a href="{s_tarot}" class="mobile-sub-link">Tarot Reading</a></li>
            <li><a href="{s_psychic}" class="mobile-sub-link">Psychic Reading</a></li>
            <li><a href="{s_medium}" class="mobile-sub-link">Medium Reading</a></li>
            <li><a href="{s_energy}" class="mobile-sub-link">Reiki &amp; Seichim Healing</a></li>
            <li><a href="{s_chakra}" class="mobile-sub-link">Chakra Balancing &amp; Aura Cleansing</a></li>
            <li><a href="{s_holistic}" class="mobile-sub-link">Holistic Guidance</a></li>
            <li><a href="{s_meditation}" class="mobile-sub-link">Meditation</a></li>
          </ul>
        </li>
        <li><a href="{blog_href}" class="mobile-nav-link {is_blog}">Blog</a></li>
        <li><a href="{gallery_href}" class="mobile-nav-link {is_gallery}">Gallery</a></li>
        <li><a href="{contact_href}" class="mobile-nav-link {is_contact}">Contact Us</a></li>
      </ul>

      <div class="mobile-nav-footer">
        <a href="tel:+12148998311" class="mobile-phone-cta">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
          </svg>
          Call +1 (214) 899-8311
        </a>
      </div>
    </div>
  </header>
"""

def get_footer(depth=0):
    rel = "../" * depth
    logo_src = f"{rel}assets/images/logo.png"

    home_href = f"{rel}index.html"
    about_href = f"{rel}about.html"
    services_href = f"{rel}services.html"
    blog_href = f"{rel}blog.html"
    gallery_href = f"{rel}gallery.html"
    contact_href = f"{rel}contact.html"
    privacy_href = f"{rel}privacy-policy.html"
    disclaimer_href = f"{rel}disclaimer.html"

    s_tarot = f"{rel}services/tarot-reading.html"
    s_psychic = f"{rel}services/psychic-reading.html"
    s_medium = f"{rel}services/medium-reading.html"
    s_energy = f"{rel}services/energy-healing.html"
    s_chakra = f"{rel}services/chakra-balancing-aura-cleansing.html"
    s_holistic = f"{rel}services/holistic-counseling.html"
    s_meditation = f"{rel}services/meditation.html"

    return f"""
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-top-grid">
        <div class="footer-brand">
          <a href="{home_href}" aria-label="9th Chakra Psychic">
            <img src="{logo_src}" alt="9th Chakra Psychic" class="footer-logo" width="220" height="73" />
          </a>
          <p>
            Private spiritual guidance and personal counsel for more than 30 years. Serving clients in Dallas, Texas, and worldwide with discretion, warmth, and intuitive clarity.
          </p>
          <a href="tel:+12148998311" class="footer-phone-cta">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
            </svg>
            +1 (214) 899-8311
          </a>
        </div>

        <div class="footer-col">
          <h4>Navigation</h4>
          <ul class="footer-links">
            <li><a href="{home_href}">Home</a></li>
            <li><a href="{about_href}">About Us</a></li>
            <li><a href="{services_href}">All Services</a></li>
            <li><a href="{blog_href}">Spiritual Journal</a></li>
            <li><a href="{gallery_href}">Sanctuary Gallery</a></li>
            <li><a href="{contact_href}">Contact Practice</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Spiritual Services</h4>
          <ul class="footer-links">
            <li><a href="{s_tarot}">Tarot Reading</a></li>
            <li><a href="{s_psychic}">Psychic Reading</a></li>
            <li><a href="{s_medium}">Medium Reading</a></li>
            <li><a href="{s_energy}">Reiki &amp; Seichim Healing</a></li>
            <li><a href="{s_chakra}">Chakra Balancing</a></li>
            <li><a href="{s_holistic}">Holistic Guidance</a></li>
            <li><a href="{s_meditation}">Meditation Practice</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Practice &amp; Reach</h4>
          <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.6; margin-bottom:12px;">
            Based in Dallas, Texas, with private spiritual counsel extended to an international clientele across North America, Europe, and worldwide.
          </p>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">
            By direct appointment. Inquiries and scheduling are arranged personally by telephone.
          </p>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          &copy; 2026 9th Chakra Psychic. All rights reserved. Dallas, Texas &amp; International.
        </div>
        <div class="footer-bottom-links">
          <a href="{privacy_href}">Privacy Policy</a>
          <a href="{disclaimer_href}">Spiritual Services Disclaimer</a>
        </div>
      </div>
    </div>
  </footer>
"""

def wrap_page(title, description, canonical_url, current_page, content, depth=0, json_ld=None, extra_scripts=""):
    rel = "../" * depth
    css_href = f"{rel}assets/css/style.css?v=20261114_clean"
    main_js_href = f"{rel}assets/js/main.js?v=20261114_clean"
    header_html = get_header(current_page, depth)
    footer_html = get_footer(depth)

    json_ld_script = ""
    if json_ld:
        json_ld_script = f"""
  <script type="application/ld+json">
{json_ld}
  </script>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph / Social Sharing -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{rel}assets/images/logo.png">
  <meta property="og:site_name" content="9th Chakra Psychic">

  <!-- Twitter Meta -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{rel}assets/images/logo.png">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="{rel}assets/images/logo.png">

  <!-- Core Stylesheet -->
  <link rel="stylesheet" href="{css_href}">
{json_ld_script}
</head>
<body>
  <a href="#mainContent" class="skip-link">Skip to main content</a>
  {header_html}
  <main id="mainContent" role="main">
    {content}
  </main>
  {footer_html}

  <script src="{main_js_href}" defer></script>
  {extra_scripts}
</body>
</html>
"""

def main():
    print("Building 9th Chakra Psychic multi-page website in:", BASE_DIR)

    def save_page(rel_path, html_content):
        abs_path = os.path.join(BASE_DIR, rel_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Generated: {rel_path}")

    # 1. Home Page
    home_ld = """{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "9th Chakra Psychic",
  "url": "https://9thchakropsychic.com/",
  "logo": "https://9thchakropsychic.com/assets/images/logo.png",
  "telephone": "+12148998311",
  "priceRange": "$$",
  "areaServed": ["Dallas, TX", "United States", "International"],
  "description": "Private spiritual guidance, tarot readings, psychic readings, energy healing, and chakra balancing with over 30 years of experience in Dallas, TX."
}"""
    home_html = wrap_page(
        title="9th Chakra Psychic | Spiritual Guidance & Tarot Readings Dallas, TX",
        description="Private spiritual guidance and intuitive counsel for over 30 years. Tarot readings, psychic readings, energy healing, and chakra balancing in Dallas, TX & worldwide.",
        canonical_url=f"{SITE_URL}/",
        current_page="home",
        content=render_home(""),
        depth=0,
        json_ld=home_ld
    )
    save_page("index.html", home_html)

    # 2. About Us
    about_ld = """{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "About 9th Chakra Psychic",
  "description": "More than 30 years of private spiritual guidance and personal counsel to individuals, professionals, and families in Dallas, TX and internationally.",
  "publisher": {
    "@type": "Organization",
    "name": "9th Chakra Psychic",
    "telephone": "+12148998311"
  }
}"""
    about_html = wrap_page(
        title="About Us | 30+ Years of Intuitive Guidance | 9th Chakra Psychic",
        description="Learn about 9th Chakra Psychic. For over 30 years, offering private spiritual counsel, intuition, and personal guidance to individuals, professionals, and families.",
        canonical_url=f"{SITE_URL}/about",
        current_page="about",
        content=render_about(""),
        depth=0,
        json_ld=about_ld
    )
    save_page("about.html", about_html)
    about_html_d1 = wrap_page(
        title="About Us | 30+ Years of Intuitive Guidance | 9th Chakra Psychic",
        description="Learn about 9th Chakra Psychic. For over 30 years, offering private spiritual counsel, intuition, and personal guidance to individuals, professionals, and families.",
        canonical_url=f"{SITE_URL}/about",
        current_page="about",
        content=render_about("../"),
        depth=1,
        json_ld=about_ld
    )
    save_page("about/index.html", about_html_d1)

    # 3. Services Main Page
    services_ld = """{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Spiritual Guidance & Reading Services",
  "description": "Comprehensive spiritual guidance services including tarot, psychic readings, mediumship, energy healing, chakra balancing, and meditation.",
  "publisher": {
    "@type": "Organization",
    "name": "9th Chakra Psychic"
  }
}"""
    services_html = wrap_page(
        title="Spiritual Reading & Guidance Services Dallas | 9th Chakra Psychic",
        description="Explore spiritual guidance services: tarot reading, psychic readings, medium readings, Reiki & Seichim energy healing, chakra balancing, and meditation in Dallas, TX.",
        canonical_url=f"{SITE_URL}/services",
        current_page="services",
        content=render_services_index(""),
        depth=0,
        json_ld=services_ld
    )
    save_page("services.html", services_html)
    services_html_d1 = wrap_page(
        title="Spiritual Reading & Guidance Services Dallas | 9th Chakra Psychic",
        description="Explore spiritual guidance services: tarot reading, psychic readings, medium readings, Reiki & Seichim energy healing, chakra balancing, and meditation in Dallas, TX.",
        canonical_url=f"{SITE_URL}/services",
        current_page="services",
        content=render_services_index("../"),
        depth=1,
        json_ld=services_ld
    )
    save_page("services/index.html", services_html_d1)

    # 4. Seven Individual Service Pages
    service_slugs = [
        "tarot-reading",
        "psychic-reading",
        "medium-reading",
        "energy-healing",
        "chakra-balancing-aura-cleansing",
        "holistic-counseling",
        "meditation"
    ]
    s_data = get_service_data()
    for slug in service_slugs:
        item = s_data[slug]
        s_ld = f"""{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "{item['service_name']}",
  "serviceType": "Spiritual Reading & Guidance",
  "provider": {{
    "@type": "ProfessionalService",
    "name": "9th Chakra Psychic",
    "telephone": "+12148998311"
  }},
  "areaServed": "Dallas, TX & International",
  "description": "{item['meta_desc']}"
}}"""
        s_html_d1 = wrap_page(
            title=item["title"],
            description=item["meta_desc"],
            canonical_url=f"{SITE_URL}/services/{slug}",
            current_page=f"service-{slug}",
            content=render_service_page(slug, "../"),
            depth=1,
            json_ld=s_ld
        )
        save_page(f"services/{slug}.html", s_html_d1)

        s_html_d2 = wrap_page(
            title=item["title"],
            description=item["meta_desc"],
            canonical_url=f"{SITE_URL}/services/{slug}",
            current_page=f"service-{slug}",
            content=render_service_page(slug, "../../"),
            depth=2,
            json_ld=s_ld
        )
        save_page(f"services/{slug}/index.html", s_html_d2)

    # 5. Blog Index
    blog_ld = """{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "9th Chakra Spiritual Journal",
  "description": "Reflective essays, practical guides, and grounded spiritual wisdom developed over three decades of private intuitive counsel."
}"""
    blog_html = wrap_page(
        title="Spiritual Journal & Blog | 9th Chakra Psychic Dallas",
        description="Read articles on preparing for tarot readings, understanding the seven chakras, and navigating relationship uncertainty with personal clarity.",
        canonical_url=f"{SITE_URL}/blog",
        current_page="blog",
        content=render_blog_index(""),
        depth=0,
        json_ld=blog_ld
    )
    save_page("blog.html", blog_html)
    blog_html_d1 = wrap_page(
        title="Spiritual Journal & Blog | 9th Chakra Psychic Dallas",
        description="Read articles on preparing for tarot readings, understanding the seven chakras, and navigating relationship uncertainty with personal clarity.",
        canonical_url=f"{SITE_URL}/blog",
        current_page="blog",
        content=render_blog_index("../"),
        depth=1,
        json_ld=blog_ld
    )
    save_page("blog/index.html", blog_html_d1)

    # 6. Three Blog Articles
    # Article 1
    art1_ld = """{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "How to Prepare for a Tarot Reading: Questions, Intentions, and Expectations",
  "description": "Learn how setting clear intentions and formulating thoughtful inquiries elevates your reading from mere curiosity into a deeply reflective tool.",
  "publisher": {
    "@type": "Organization",
    "name": "9th Chakra Psychic"
  }
}"""
    art1_slug = "how-to-prepare-for-a-tarot-reading"
    art1_html_d1 = wrap_page(
        title="How to Prepare for a Tarot Reading | 9th Chakra Psychic Blog",
        description="Learn how to formulate open-ended questions, set clear intentions, and understand card symbolism for a transformative tarot reading experience.",
        canonical_url=f"{SITE_URL}/blog/{art1_slug}",
        current_page="blog-tarot",
        content=render_article_1("../"),
        depth=1,
        json_ld=art1_ld
    )
    save_page(f"blog/{art1_slug}.html", art1_html_d1)
    art1_html_d2 = wrap_page(
        title="How to Prepare for a Tarot Reading | 9th Chakra Psychic Blog",
        description="Learn how to formulate open-ended questions, set clear intentions, and understand card symbolism for a transformative tarot reading experience.",
        canonical_url=f"{SITE_URL}/blog/{art1_slug}",
        current_page="blog-tarot",
        content=render_article_1("../../"),
        depth=2,
        json_ld=art1_ld
    )
    save_page(f"blog/{art1_slug}/index.html", art1_html_d2)

    # Article 2
    art2_ld = """{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Understanding the Seven Chakras: A Gentle Guide to Energy Centers",
  "description": "A grounded introduction to the human energetic framework, from the grounding root to the expansive crown center.",
  "publisher": {
    "@type": "Organization",
    "name": "9th Chakra Psychic"
  }
}"""
    art2_slug = "understanding-the-seven-chakras"
    art2_html_d1 = wrap_page(
        title="Understanding the Seven Chakras: Gentle Energy Guide | 9th Chakra",
        description="Explore the spiritual tradition of the seven chakras—Root, Sacral, Solar Plexus, Heart, Throat, Third Eye, and Crown—and their roles in inner balance.",
        canonical_url=f"{SITE_URL}/blog/{art2_slug}",
        current_page="blog-chakras",
        content=render_article_2("../"),
        depth=1,
        json_ld=art2_ld
    )
    save_page(f"blog/{art2_slug}.html", art2_html_d1)
    art2_html_d2 = wrap_page(
        title="Understanding the Seven Chakras: Gentle Energy Guide | 9th Chakra",
        description="Explore the spiritual tradition of the seven chakras—Root, Sacral, Solar Plexus, Heart, Throat, Third Eye, and Crown—and their roles in inner balance.",
        canonical_url=f"{SITE_URL}/blog/{art2_slug}",
        current_page="blog-chakras",
        content=render_article_2("../../"),
        depth=2,
        json_ld=art2_ld
    )
    save_page(f"blog/{art2_slug}/index.html", art2_html_d2)

    # Article 3
    art3_ld = """{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Navigating Relationship Uncertainty: Reflection, Boundaries, and Personal Clarity",
  "description": "Practical wisdom on recognizing recurring dynamics, honoring boundaries, and finding clarity during emotional transitions.",
  "publisher": {
    "@type": "Organization",
    "name": "9th Chakra Psychic"
  }
}"""
    art3_slug = "navigating-relationship-uncertainty"
    art3_html_d1 = wrap_page(
        title="Navigating Relationship Uncertainty & Boundaries | 9th Chakra Psychic",
        description="Insightful spiritual perspective on navigating relationship crossroads, recognizing patterns, upholding boundaries, and finding personal clarity.",
        canonical_url=f"{SITE_URL}/blog/{art3_slug}",
        current_page="blog-relationships",
        content=render_article_3("../"),
        depth=1,
        json_ld=art3_ld
    )
    save_page(f"blog/{art3_slug}.html", art3_html_d1)
    art3_html_d2 = wrap_page(
        title="Navigating Relationship Uncertainty & Boundaries | 9th Chakra Psychic",
        description="Insightful spiritual perspective on navigating relationship crossroads, recognizing patterns, upholding boundaries, and finding personal clarity.",
        canonical_url=f"{SITE_URL}/blog/{art3_slug}",
        current_page="blog-relationships",
        content=render_article_3("../../"),
        depth=2,
        json_ld=art3_ld
    )
    save_page(f"blog/{art3_slug}/index.html", art3_html_d2)

    # 7. Gallery
    gallery_scripts = '<script src="assets/js/lightbox.js" defer></script>'
    gallery_html = wrap_page(
        title="Sanctuary Gallery | 9th Chakra Psychic Dallas, TX",
        description="Explore our Dallas consultation sanctuary gallery featuring reading spaces, crystal arrangements, celestial symbolism, and sacred tools.",
        canonical_url=f"{SITE_URL}/gallery",
        current_page="gallery",
        content=render_gallery(""),
        depth=0,
        extra_scripts=gallery_scripts
    )
    save_page("gallery.html", gallery_html)
    gallery_scripts_d1 = '<script src="../assets/js/lightbox.js" defer></script>'
    gallery_html_d1 = wrap_page(
        title="Sanctuary Gallery | 9th Chakra Psychic Dallas, TX",
        description="Explore our Dallas consultation sanctuary gallery featuring reading spaces, crystal arrangements, celestial symbolism, and sacred tools.",
        canonical_url=f"{SITE_URL}/gallery",
        current_page="gallery",
        content=render_gallery("../"),
        depth=1,
        extra_scripts=gallery_scripts_d1
    )
    save_page("gallery/index.html", gallery_html_d1)

    # 8. Contact Us
    contact_ld = """{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "name": "Contact 9th Chakra Psychic",
  "telephone": "+12148998311",
  "description": "Reach out directly by phone at +1 (214) 899-8311 to inquire about private spiritual readings and schedule a consultation in Dallas or internationally."
}"""
    contact_html = wrap_page(
        title="Contact Us & Schedule a Private Reading | 9th Chakra Psychic Dallas",
        description="Contact 9th Chakra Psychic for private spiritual guidance. Call directly at +1 (214) 899-8311. Serving clients in Dallas, TX and internationally.",
        canonical_url=f"{SITE_URL}/contact",
        current_page="contact",
        content=render_contact(""),
        depth=0,
        json_ld=contact_ld
    )
    save_page("contact.html", contact_html)
    contact_html_d1 = wrap_page(
        title="Contact Us & Schedule a Private Reading | 9th Chakra Psychic Dallas",
        description="Contact 9th Chakra Psychic for private spiritual guidance. Call directly at +1 (214) 899-8311. Serving clients in Dallas, TX and internationally.",
        canonical_url=f"{SITE_URL}/contact",
        current_page="contact",
        content=render_contact("../"),
        depth=1,
        json_ld=contact_ld
    )
    save_page("contact/index.html", contact_html_d1)

    # 9. Privacy Policy
    privacy_html = wrap_page(
        title="Privacy Policy | 9th Chakra Psychic",
        description="Privacy policy and client confidentiality practices of 9th Chakra Psychic.",
        canonical_url=f"{SITE_URL}/privacy-policy",
        current_page="privacy",
        content=render_privacy_policy(""),
        depth=0
    )
    save_page("privacy-policy.html", privacy_html)
    privacy_html_d1 = wrap_page(
        title="Privacy Policy | 9th Chakra Psychic",
        description="Privacy policy and client confidentiality practices of 9th Chakra Psychic.",
        canonical_url=f"{SITE_URL}/privacy-policy",
        current_page="privacy",
        content=render_privacy_policy("../"),
        depth=1
    )
    save_page("privacy-policy/index.html", privacy_html_d1)

    # 10. Disclaimer
    disclaimer_html = wrap_page(
        title="Spiritual Services Disclaimer | 9th Chakra Psychic",
        description="Spiritual services disclaimer for 9th Chakra Psychic. Please review our service scope, free will policy, and personal responsibility statement.",
        canonical_url=f"{SITE_URL}/disclaimer",
        current_page="disclaimer",
        content=render_disclaimer(""),
        depth=0
    )
    save_page("disclaimer.html", disclaimer_html)
    disclaimer_html_d1 = wrap_page(
        title="Spiritual Services Disclaimer | 9th Chakra Psychic",
        description="Spiritual services disclaimer for 9th Chakra Psychic. Please review our service scope, free will policy, and personal responsibility statement.",
        canonical_url=f"{SITE_URL}/disclaimer",
        current_page="disclaimer",
        content=render_disclaimer("../"),
        depth=1
    )
    save_page("disclaimer/index.html", disclaimer_html_d1)

    # 11. 404 Error Page
    not_found_html = wrap_page(
        title="404 Page Not Found | 9th Chakra Psychic",
        description="The page you are seeking could not be found. Return to 9th Chakra Psychic homepage or explore our services.",
        canonical_url=f"{SITE_URL}/404.html",
        current_page="404",
        content=render_404(""),
        depth=0
    )
    save_page("404.html", not_found_html)

    # 12. XML Sitemap
    all_urls = [
        "",
        "/about",
        "/services",
        "/blog",
        "/gallery",
        "/contact",
        "/services/tarot-reading",
        "/services/psychic-reading",
        "/services/medium-reading",
        "/services/energy-healing",
        "/services/chakra-balancing-aura-cleansing",
        "/services/holistic-counseling",
        "/services/meditation",
        "/blog/how-to-prepare-for-a-tarot-reading",
        "/blog/understanding-the-seven-chakras",
        "/blog/navigating-relationship-uncertainty",
        "/privacy-policy",
        "/disclaimer"
    ]
    sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in all_urls:
        prio = "1.0" if u == "" else ("0.9" if u in ["/services", "/contact", "/about"] else "0.8")
        sitemap_xml.append(f"""  <url>
    <loc>{SITE_URL}{u}</loc>
    <changefreq>monthly</changefreq>
    <priority>{prio}</priority>
  </url>""")
    sitemap_xml.append('</urlset>')
    with open(os.path.join(BASE_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write("\n".join(sitemap_xml))
    print("Generated: sitemap.xml")

    # 13. robots.txt
    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    with open(os.path.join(BASE_DIR, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(robots_txt)
    print("Generated: robots.txt")

    print("\nAll 18+ website pages, assets, and SEO files generated successfully!")

if __name__ == "__main__":
    main()
