# pages/about.py
"""About Us page template and content — Luxury editorial redesign with concise, scannable copy."""

def render_about(rel=""):
    return f"""
    <!-- Section 1: About Hero -->
    <section class="about-hero" aria-labelledby="aboutHeroHeading">
      <div class="services-hero-bg-overlay" aria-hidden="true">
        <img src="{rel}assets/images/sanctuary-crystal-altar.jpg" alt="" class="services-hero-bg-img" loading="eager" />
        <div class="services-hero-gradient-scrim"></div>
      </div>
      <div class="container" style="position:relative; z-index:2;">
        <div class="services-hero-content">
          <div class="eyebrow">
            <span class="eyebrow-dot"></span>
            Private Spiritual Practice &middot; 30+ Years Experience
          </div>
          <h1 id="aboutHeroHeading" class="services-hero-title">
            Guidance. Personal Insight. A Deeper Perspective.
          </h1>
          <p class="services-hero-description">
            For more than 30 years, The Reader has provided private guidance and personal counsel to individuals, accomplished professionals, business owners, and families.
          </p>

          <div style="margin-top:28px; display:flex; flex-wrap:wrap; gap:16px;">
            <a href="tel:+12148998311" class="btn btn-gold">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              Call +1 (214) 899-8311
            </a>
            <a href="{rel}services.html" class="btn btn-outline">
              Explore Offerings &rarr;
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Balanced Split Story (Concise Narrative + Photography) -->
    <section class="section" aria-labelledby="storyHeading">
      <div class="container">
        <div class="about-story-grid">
          <div class="about-story-text">
            <div class="eyebrow">Personal Background &amp; Practice</div>
            <h2 id="storyHeading" style="font-size:clamp(2rem, 3.2vw, 2.7rem); line-height:1.2; margin-bottom:20px;">
              A Journey Dedicated to Clarity and Human Insight.
            </h2>
            <div class="article-quote" style="margin:0 0 24px 0; font-size:1.05rem;">
              &ldquo;Life presents moments when analytical reasoning feels exhausted. What is needed is a deeper, more perceptive lens.&rdquo;
            </div>
            <p style="font-size:1.02rem; color:var(--text-secondary); line-height:1.7; margin-bottom:18px;">
              Over three decades of private practice, The Reader has cultivated an intuitive sensitivity that bridges ancient esoteric symbolism, energetic awareness, and a sophisticated understanding of human nature.
            </p>
            <p style="font-size:1.02rem; color:var(--text-secondary); line-height:1.7; margin-bottom:0;">
              Unlike commercialized entertainment, every consultation is treated as an intimate and confidential counsel. Sessions illuminate subtle emotional currents and potential horizons, strengthening your personal agency to navigate life with poise.
            </p>
          </div>

          <div class="about-story-photo">
            <img src="{rel}assets/images/sanctuary-chakras-room-crop.jpg" alt="Sanctuary room displaying seven aligned chakra colors" width="600" height="450" loading="lazy" />
            <div class="sanctuary-showcase-badge">
              <span class="chakra-badge-dot" style="background:var(--gold-primary);"></span>
              <span>The Dallas Sanctuary</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 3: Three Core Pillars (Concise, Uncluttered Cards) -->
    <section class="section section-alt" aria-labelledby="philosophyHeading">
      <div class="container">
        <div class="section-header" style="max-width:720px;">
          <div class="eyebrow">Core Philosophy</div>
          <h2 id="philosophyHeading">Principles That Guide Every Consultation.</h2>
          <p>
            A grounded, ethical framework ensuring every client feels respected, supported, and personally empowered.
          </p>
        </div>

        <div class="about-pillars-grid">
          <div class="service-card" style="padding:32px 28px;">
            <div class="service-card-top" style="margin-bottom:18px;">
              <div class="service-card-icon" style="width:44px; height:44px;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              </div>
              <span class="service-tag">Discretion</span>
            </div>
            <h3 style="font-size:1.35rem; margin-bottom:12px;">Absolute Privacy</h3>
            <p style="font-size:0.95rem; color:var(--text-secondary); line-height:1.65; margin:0;">
              Every consultation is strictly confidential. Personal circumstances, family dynamics, and executive matters are treated with dignity and discretion.
            </p>
          </div>

          <div class="service-card" style="padding:32px 28px;">
            <div class="service-card-top" style="margin-bottom:18px;">
              <div class="service-card-icon" style="width:44px; height:44px;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
              </div>
              <span class="service-tag">Sovereignty</span>
            </div>
            <h3 style="font-size:1.35rem; margin-bottom:12px;">Personal Empowerment</h3>
            <p style="font-size:0.95rem; color:var(--text-secondary); line-height:1.65; margin:0;">
              We never foster dependence. Our purpose is to illuminate clarity, providing insight so you can make informed decisions with independent confidence.
            </p>
          </div>

          <div class="service-card" style="padding:32px 28px;">
            <div class="service-card-top" style="margin-bottom:18px;">
              <div class="service-card-icon" style="width:44px; height:44px;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 8v8M8 12h8"></path></svg>
              </div>
              <span class="service-tag">Sanctuary</span>
            </div>
            <h3 style="font-size:1.35rem; margin-bottom:12px;">Compassionate Presence</h3>
            <p style="font-size:0.95rem; color:var(--text-secondary); line-height:1.65; margin:0;">
              A calm, unhurried space free from theatrical judgment. Guidance is shared with warmth, active listening, and sincere care for your emotional peace.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Who We Work With (Balanced 4-Column Compact Grid) -->
    <section class="section" aria-labelledby="clienteleHeading">
      <div class="container">
        <div class="section-header" style="max-width:720px;">
          <div class="eyebrow">Client Relationships</div>
          <h2 id="clienteleHeading">Who We Counsel.</h2>
          <p>
            Serving thoughtful individuals seeking genuine perspective across all walks of life.
          </p>
        </div>

        <div class="about-clientele-grid">
          <div class="service-card" style="padding:28px 24px;">
            <div style="font-size:1.5rem; color:var(--gold-primary); margin-bottom:12px;">✦</div>
            <h4 style="font-size:1.15rem; margin-bottom:8px;">Individuals</h4>
            <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.6; margin:0;">
              Those at personal crossroads seeking direction, self-understanding, and spiritual reflection.
            </p>
          </div>

          <div class="service-card" style="padding:28px 24px;">
            <div style="font-size:1.5rem; color:var(--chakra-heart); margin-bottom:12px;">✦</div>
            <h4 style="font-size:1.15rem; margin-bottom:8px;">Couples &amp; Partners</h4>
            <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.6; margin:0;">
              Partners navigating relationship communication, emotional crossroads, or thoughtful closure.
            </p>
          </div>

          <div class="service-card" style="padding:28px 24px;">
            <div style="font-size:1.5rem; color:var(--chakra-solar); margin-bottom:12px;">✦</div>
            <h4 style="font-size:1.15rem; margin-bottom:8px;">Executives &amp; Leaders</h4>
            <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.6; margin:0;">
              Accomplished professionals seeking confidential perspective outside their standard circles.
            </p>
          </div>

          <div class="service-card" style="padding:28px 24px;">
            <div style="font-size:1.5rem; color:var(--chakra-third-eye); margin-bottom:12px;">✦</div>
            <h4 style="font-size:1.15rem; margin-bottom:8px;">Global Seekers</h4>
            <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.6; margin:0;">
              Clients connecting worldwide via remote telephone consultations with seasoned understanding.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 5: Sanctuary Ambiance Showcase -->
    <section class="section section-alt" aria-labelledby="sanctuaryAboutHeading">
      <div class="container">
        <div class="section-header" style="max-width:720px;">
          <div class="eyebrow">The Environment</div>
          <h2 id="sanctuaryAboutHeading">A Calm Sanctuary in Dallas.</h2>
          <p>
            Designed to foster stillness, reflection, and focused intuitive attunement.
          </p>
        </div>

        <div class="about-sanctuary-showcase">
          <div class="sanctuary-showcase-card">
            <img src="{rel}assets/images/sanctuary-reading-table-crop.jpg" alt="Private consultation reading table with tarot and zodiac rug" loading="lazy" />
            <div class="sanctuary-showcase-badge">
              <span>Consultation Sanctuary &middot; Dallas, TX</span>
            </div>
          </div>
          <div class="sanctuary-showcase-card">
            <img src="{rel}assets/images/sanctuary-palmistry-neon-crop.jpg" alt="Intuitive palmistry art and ambient cobalt sanctuary lighting" loading="lazy" />
            <div class="sanctuary-showcase-badge">
              <span>Intuitive Palmistry &middot; Ambient Light</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: Centered Consultation Invitation Card -->
    <section class="section" aria-labelledby="aboutContactHeading">
      <div class="container">
        <div class="consultation-invitation-card">
          <div class="invitation-eyebrow">
            <span>✦</span>
            <span>Confidential Private Counsel</span>
            <span>✦</span>
          </div>
          <h2 id="aboutContactHeading" class="invitation-heading">
            Ready for Personal Clarity &amp; Perspective?
          </h2>
          <p class="invitation-lead">
            Connect directly by telephone for confidential scheduling, session availability, and personal spiritual counsel tailored to your circumstances. More than 30 years of private practice serving Dallas and an international clientele.
          </p>
          <div class="invitation-actions">
            <a href="tel:+12148998311" class="btn btn-gold btn-lg">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              Call +1 (214) 899-8311
            </a>
            <a href="{rel}services.html" class="btn btn-outline btn-lg">
              Explore All Offerings &rarr;
            </a>
          </div>
        </div>
      </div>
    </section>
    """
