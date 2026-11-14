# pages/services_index.py
"""
Redesigned Services Landing Page
Visual-first, editorial luxury presentation, uncluttered, interactive category filtering.
"""

def render_services_index(rel=""):
    return f"""
    <!-- Services Master Hero Section -->
    <section class="services-index-hero" aria-labelledby="servicesMainHeading">
      <div class="services-hero-bg-overlay" aria-hidden="true">
        <img src="{rel}assets/images/sanctuary-reading-table.jpg" alt="" class="services-hero-bg-img" loading="eager" />
        <div class="services-hero-gradient-scrim"></div>
      </div>
      <div class="container" style="position:relative; z-index:2;">
        <div class="services-hero-content">
          <div class="eyebrow">
            <span class="eyebrow-dot"></span>
            Private Spiritual Practice &middot; 30+ Years Experience
          </div>
          <h1 id="servicesMainHeading" class="services-hero-title">
            Spiritual Guidance &amp; Reading Services.
          </h1>
          <p class="services-hero-description">
            Refined private counsel, intuitive readings, and subtle energy practices designed to bring focus, emotional balance, and clarity to life&rsquo;s defining crossroads.
          </p>
          <div style="margin-top:28px; display:flex; flex-wrap:wrap; gap:16px;">
            <a href="tel:+12148998311" class="btn btn-gold">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              Call +1 (214) 899-8311
            </a>
            <a href="#servicesGrid" class="btn btn-outline">
              Explore All Services &darr;
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Main Showcase Grid Section -->
    <section class="section" style="padding-top:clamp(44px, 6vw, 68px); padding-bottom:70px;" aria-label="Services Catalog">
      <div class="container">
        <!-- Interactive Category Switcher (Centered cleanly above cards) -->
        <div class="service-filter-nav" role="tablist" aria-label="Service Category Filters" style="margin:0 auto 44px auto;">
          <button type="button" class="service-filter-btn active" data-filter="all" role="tab" aria-selected="true">
            All Offerings
          </button>
          <button type="button" class="service-filter-btn" data-filter="readings" role="tab" aria-selected="false">
            Intuitive Readings
          </button>
          <button type="button" class="service-filter-btn" data-filter="energy" role="tab" aria-selected="false">
            Energy &amp; Healing
          </button>
          <button type="button" class="service-filter-btn" data-filter="guidance" role="tab" aria-selected="false">
            Counsel &amp; Stillness
          </button>
        </div>
        <!-- Visual Luxury Showcase Grid (7 Core Services) -->
        <div class="service-luxury-grid" id="servicesGrid">
          
          <!-- 1. Tarot Reading -->
          <article class="service-luxury-card" data-category="readings">
            <div class="service-card-visual">
              <img src="{rel}assets/images/services/tarot-reading/content.jpg" alt="Tarot Reading cards spread and candlelight" loading="lazy" width="400" height="220" />
              <div class="service-card-visual-overlay"></div>
              <span class="service-floating-badge">
                <span class="chakra-badge-dot" style="background:var(--gold-primary);"></span>
                Perspective
              </span>
            </div>
            <div class="service-card-body">
              <h3>Tarot Reading</h3>
              <p class="service-card-tagline">
                A structured, symbolic exploration examining your current dynamics, relationship choices, and emerging horizons through archetypal imagery.
              </p>
              <div class="service-focus-pills">
                <span class="service-focus-pill">Relationships &middot; Love</span>
                <span class="service-focus-pill">Career Crossroads</span>
                <span class="service-focus-pill">Symbolic Clarity</span>
              </div>
              <div class="service-card-footer">
                <a href="{rel}services/tarot-reading.html" class="btn btn-gold btn-sm">Explore Reading &rarr;</a>
                <a href="tel:+12148998311" class="link-arrow" style="font-size:0.86rem;">Call to Book</a>
              </div>
            </div>
          </article>

          <!-- 2. Psychic Reading -->
          <article class="service-luxury-card" data-category="readings">
            <div class="service-card-visual">
              <img src="{rel}assets/images/services/psychic-reading/hero.jpg" alt="Psychic Reading sanctuary ambiance" loading="lazy" width="400" height="220" />
              <div class="service-card-visual-overlay"></div>
              <span class="service-floating-badge">
                <span class="chakra-badge-dot" style="background:var(--chakra-third-eye);"></span>
                Intuition
              </span>
            </div>
            <div class="service-card-body">
              <h3>Psychic Reading</h3>
              <p class="service-card-tagline">
                Direct intuitive perception uncovering subtle emotional currents, interpersonal dynamics, and unseen energetic influences shaping your situation.
              </p>
              <div class="service-focus-pills">
                <span class="service-focus-pill">Intuitive Impressions</span>
                <span class="service-focus-pill">Emotional Dynamics</span>
                <span class="service-focus-pill">Life Transitions</span>
              </div>
              <div class="service-card-footer">
                <a href="{rel}services/psychic-reading.html" class="btn btn-gold btn-sm">Explore Reading &rarr;</a>
                <a href="tel:+12148998311" class="link-arrow" style="font-size:0.86rem;">Call to Book</a>
              </div>
            </div>
          </article>

          <!-- 3. Medium Reading -->
          <article class="service-luxury-card" data-category="readings guidance">
            <div class="service-card-visual">
              <img src="{rel}assets/images/services/medium-reading/content.jpg" alt="Medium Reading spiritual connection atmosphere" loading="lazy" width="400" height="220" />
              <div class="service-card-visual-overlay"></div>
              <span class="service-floating-badge">
                <span class="chakra-badge-dot" style="background:var(--chakra-crown);"></span>
                Connection
              </span>
            </div>
            <div class="service-card-body">
              <h3>Medium Reading</h3>
              <p class="service-card-tagline">
                A compassionate, sacred consultation interpreting memories, impressions, and messages from loved ones who have transitioned beyond the physical plane.
              </p>
              <div class="service-focus-pills">
                <span class="service-focus-pill">Spiritual Solace</span>
                <span class="service-focus-pill">Cherished Memories</span>
                <span class="service-focus-pill">Heartfelt Closure</span>
              </div>
              <div class="service-card-footer">
                <a href="{rel}services/medium-reading.html" class="btn btn-gold btn-sm">Explore Reading &rarr;</a>
                <a href="tel:+12148998311" class="link-arrow" style="font-size:0.86rem;">Call to Book</a>
              </div>
            </div>
          </article>

          <!-- 4. Reiki & Seichim Energy Healing -->
          <article class="service-luxury-card" data-category="energy">
            <div class="service-card-visual">
              <img src="{rel}assets/images/services/energy-healing/content.jpg" alt="Reiki and Seichim vibrational energy healing wellness setting" loading="lazy" width="400" height="220" />
              <div class="service-card-visual-overlay"></div>
              <span class="service-floating-badge">
                <span class="chakra-badge-dot" style="background:var(--chakra-heart);"></span>
                Renewal
              </span>
            </div>
            <div class="service-card-body">
              <h3>Reiki &amp; Seichim Healing</h3>
              <p class="service-card-tagline">
                Ancient vibrational energy traditions facilitating profound nervous system relaxation, stress release, and subtle energetic alignment.
              </p>
              <div class="service-focus-pills">
                <span class="service-focus-pill">Deep Relaxation</span>
                <span class="service-focus-pill">Vibrational Harmony</span>
                <span class="service-focus-pill">Stress Release</span>
              </div>
              <div class="service-card-footer">
                <a href="{rel}services/energy-healing.html" class="btn btn-gold btn-sm">Explore Healing &rarr;</a>
                <a href="tel:+12148998311" class="link-arrow" style="font-size:0.86rem;">Call to Book</a>
              </div>
            </div>
          </article>

          <!-- 5. Chakra Balancing & Aura Cleansing -->
          <article class="service-luxury-card" data-category="energy">
            <div class="service-card-visual">
              <img src="{rel}assets/images/services/chakra-balancing/content.jpg" alt="Chakra balancing seven gemstones aligned" loading="lazy" width="400" height="220" />
              <div class="service-card-visual-overlay"></div>
              <span class="service-floating-badge">
                <span class="chakra-badge-dot" style="background:var(--chakra-solar);"></span>
                Harmonize
              </span>
            </div>
            <div class="service-card-body">
              <h3>Chakra Balancing &amp; Aura Cleansing</h3>
              <p class="service-card-tagline">
                Harmonizing the seven vertical energy centers to clear accumulated emotional density and restore luminous spiritual vitality.
              </p>
              <div class="service-focus-pills">
                <span class="service-focus-pill">Seven Centers</span>
                <span class="service-focus-pill">Aura Clearing</span>
                <span class="service-focus-pill">Grounded Equilibrium</span>
              </div>
              <div class="service-card-footer">
                <a href="{rel}services/chakra-balancing-aura-cleansing.html" class="btn btn-gold btn-sm">Explore Balancing &rarr;</a>
                <a href="tel:+12148998311" class="link-arrow" style="font-size:0.86rem;">Call to Book</a>
              </div>
            </div>
          </article>

          <!-- 6. Holistic Counseling & Guidance -->
          <article class="service-luxury-card" data-category="guidance">
            <div class="service-card-visual">
              <img src="{rel}assets/images/services/holistic-counseling/content.jpg" alt="Holistic counseling peaceful reflection space" loading="lazy" width="400" height="220" />
              <div class="service-card-visual-overlay"></div>
              <span class="service-floating-badge">
                <span class="chakra-badge-dot" style="background:var(--chakra-throat);"></span>
                Insight
              </span>
            </div>
            <div class="service-card-body">
              <h3>Holistic Guidance &amp; Counsel</h3>
              <p class="service-card-tagline">
                Integrative personal counsel addressing the emotional, spiritual, and relational layers of recurring life patterns for wise decision-making.
              </p>
              <div class="service-focus-pills">
                <span class="service-focus-pill">Pattern Recognition</span>
                <span class="service-focus-pill">Self-Awareness</span>
                <span class="service-focus-pill">Sovereign Choices</span>
              </div>
              <div class="service-card-footer">
                <a href="{rel}services/holistic-counseling.html" class="btn btn-gold btn-sm">Explore Counsel &rarr;</a>
                <a href="tel:+12148998311" class="link-arrow" style="font-size:0.86rem;">Call to Book</a>
              </div>
            </div>
          </article>

          <!-- 7. Meditation Guidance -->
          <article class="service-luxury-card" data-category="guidance energy">
            <div class="service-card-visual">
              <img src="{rel}assets/images/services/meditation/content.jpg" alt="Meditation and mindfulness serene atmosphere" loading="lazy" width="400" height="220" />
              <div class="service-card-visual-overlay"></div>
              <span class="service-floating-badge">
                <span class="chakra-badge-dot" style="background:var(--champagne);"></span>
                Stillness
              </span>
            </div>
            <div class="service-card-body">
              <h3>Meditation Guidance</h3>
              <p class="service-card-tagline">
                Personalized guided stillness, breathwork (Pranayama), and visualization to quiet mental chatter and foster deep inner composure.
              </p>
              <div class="service-focus-pills">
                <span class="service-focus-pill">Breath Awareness</span>
                <span class="service-focus-pill">Mindful Presence</span>
                <span class="service-focus-pill">Somatic Peace</span>
              </div>
              <div class="service-card-footer">
                <a href="{rel}services/meditation.html" class="btn btn-gold btn-sm">Explore Meditation &rarr;</a>
                <a href="tel:+12148998311" class="link-arrow" style="font-size:0.86rem;">Call to Book</a>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Section 2: Modality Compass / Experience Matcher -->
    <section class="section section-alt" aria-labelledby="compassHeading">
      <div class="container">
        <div class="section-header">
          <div class="eyebrow">Selection Compass</div>
          <h2 id="compassHeading">Where Would You Like to Begin?</h2>
          <p>
            Choose the area of focus that speaks most closely to what you are currently experiencing:
          </p>
        </div>

        <div class="compass-grid">
          <!-- Compass Pillar 1 -->
          <div class="compass-card">
            <div class="compass-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                <circle cx="12" cy="12" r="10"></circle>
                <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon>
              </svg>
            </div>
            <h3>Seeking Clarity &amp; Answers</h3>
            <p>For navigating relationship crossroads, marriage questions, or career decisions where you need clear, objective perspective.</p>
            <div class="compass-links">
              <a href="{rel}services/tarot-reading.html" class="compass-link-chip">Tarot Reading</a>
              <a href="{rel}services/psychic-reading.html" class="compass-link-chip">Psychic Reading</a>
            </div>
          </div>

          <!-- Compass Pillar 2 -->
          <div class="compass-card">
            <div class="compass-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
              </svg>
            </div>
            <h3>Seeking Balance &amp; Vitality</h3>
            <p>For releasing emotional fatigue, burnout, or empathic overload through subtle vibrational restoration and energetic alignment.</p>
            <div class="compass-links">
              <a href="{rel}services/energy-healing.html" class="compass-link-chip">Reiki &amp; Seichim</a>
              <a href="{rel}services/chakra-balancing-aura-cleansing.html" class="compass-link-chip">Chakra Balancing</a>
            </div>
          </div>

          <!-- Compass Pillar 3 -->
          <div class="compass-card">
            <div class="compass-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M8 12a4 4 0 0 1 8 0"></path>
              </svg>
            </div>
            <h3>Seeking Meaning &amp; Solace</h3>
            <p>For honoring transitioned loved ones, finding direction through life transitions, and cultivating lasting mindful tranquility.</p>
            <div class="compass-links">
              <a href="{rel}services/medium-reading.html" class="compass-link-chip">Mediumship</a>
              <a href="{rel}services/holistic-counseling.html" class="compass-link-chip">Holistic Guidance</a>
              <a href="{rel}services/meditation.html" class="compass-link-chip">Meditation</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 3: Specialized Complementary Modalities -->
    <section class="section" aria-labelledby="specializedHeading">
      <div class="container">
        <div class="section-header">
          <div class="eyebrow">Esoteric Heritage</div>
          <h2 id="specializedHeading">Specialized Readings Upon Request.</h2>
          <p>
            Traditional modalities that can be incorporated into private consultations:
          </p>
        </div>

        <div class="secondary-modality-grid">
          <div class="secondary-modality-item">
            <div class="s-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 11V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v0"></path><path d="M14 10V4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v2"></path><path d="M10 10.5V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v8"></path></svg></div>
            <div>
              <h4>Palm Reading</h4>
              <span>Chiromancy Insights</span>
            </div>
          </div>

          <div class="secondary-modality-item">
            <div class="s-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
            <div>
              <h4>Crystal Reading</h4>
              <span>Mineral Resonances</span>
            </div>
          </div>

          <div class="secondary-modality-item">
            <div class="s-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 8 14"></polyline></svg></div>
            <div>
              <h4>Past-Life Reflection</h4>
              <span>Karmic Pattern Awareness</span>
            </div>
          </div>

          <div class="secondary-modality-item">
            <div class="s-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg></div>
            <div>
              <h4>Dream Interpretation</h4>
              <span>Subconscious Symbolism</span>
            </div>
          </div>

          <div class="secondary-modality-item">
            <div class="s-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="9" x2="15" y2="15"></line></svg></div>
            <div>
              <h4>Numerology</h4>
              <span>Life Path Cycles</span>
            </div>
          </div>

          <div class="secondary-modality-item">
            <div class="s-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path></svg></div>
            <div>
              <h4>Astrology Perspective</h4>
              <span>Planetary Archetypes</span>
            </div>
          </div>

          <div class="secondary-modality-item">
            <div class="s-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"></path><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path></svg></div>
            <div>
              <h4>Tea-Leaf Reading</h4>
              <span>Botanical Symbolism</span>
            </div>
          </div>

          <div class="secondary-modality-item">
            <div class="s-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 8v8M8 12h8"></path></svg></div>
            <div>
              <h4>Energy Reading</h4>
              <span>Subtle Biofield Attunement</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Streamlined FAQs -->
    <section class="section section-alt" aria-labelledby="serviceFaqHeading">
      <div class="container container-narrow">
        <div class="section-header">
          <div class="eyebrow">Essential Information</div>
          <h2 id="serviceFaqHeading">Consultation Questions.</h2>
        </div>

        <div class="accordion">
          <div class="accordion-item">
            <button type="button" class="accordion-header" aria-expanded="false">
              <span>How are private consultations scheduled and conducted?</span>
              <span class="accordion-icon" aria-hidden="true">
                <svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 1l4 4 4-4" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </span>
            </button>
            <div class="accordion-body">
              <p>
                Consultations are arranged directly by phone at <strong>+1 (214) 899-8311</strong>. During your initial call, you can discuss your questions, determine the best modality, and coordinate timing. Consultations are available to clients locally in Dallas and across the world.
              </p>
            </div>
          </div>

          <div class="accordion-item">
            <button type="button" class="accordion-header" aria-expanded="false">
              <span>Can multiple modalities be combined in a single session?</span>
              <span class="accordion-icon" aria-hidden="true">
                <svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 1l4 4 4-4" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </span>
            </button>
            <div class="accordion-body">
              <p>
                Yes. Many clients pair Tarot with an intuitive psychic reading, or combine an intuitive consultation with restorative chakra balancing. Modality combinations can be tailored to your goals.
              </p>
            </div>
          </div>

          <div class="accordion-item">
            <button type="button" class="accordion-header" aria-expanded="false">
              <span>What should I do to prepare for my reading?</span>
              <span class="accordion-icon" aria-hidden="true">
                <svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 1l4 4 4-4" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </span>
            </button>
            <div class="accordion-body">
              <p>
                Bring a calm, receptive mindset and consider the life areas or questions where you seek perspective. Open-ended inquiries yield the deepest intuitive clarity.
              </p>
            </div>
          </div>
        </div>

        <div class="service-cta-box" style="margin-top:48px;">
          <div class="service-cta-text">
            <h4>Ready to Begin Your Consultation?</h4>
            <p>Connect directly with The Reader to arrange your private session.</p>
          </div>
          <a href="tel:+12148998311" class="btn btn-gold" style="flex-shrink:0;">
            Call +1 (214) 899-8311
          </a>
        </div>
      </div>
    </section>
    """
