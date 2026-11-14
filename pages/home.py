# pages/home.py
"""Home page template and content."""

def render_home(rel=""):
    return f"""
    <!-- Section 1: Hero Section -->
    <section class="hero" aria-label="Introduction and Guidance">
      <img src="{rel}assets/svg/mandala-bg.svg" class="hero-mandala-bg" alt="" aria-hidden="true" />
      <div class="container hero-grid">
        <div class="hero-content">
          <div class="eyebrow">Private Spiritual Guidance &middot; Over 30 Years of Experience</div>
          <h1>Clarity for Life&rsquo;s Most Important Moments.</h1>
          <p class="hero-description">
            For more than 30 years, I have offered personal guidance and intuitive insight to individuals navigating relationships, emotional challenges, personal transitions, and life&rsquo;s defining decisions.
          </p>
          <div class="hero-subline">
            Private guidance for clients in Dallas and around the world.
          </div>
          <div class="btn-group">
            <a href="{rel}services.html" class="btn btn-gold">Explore Our Services</a>
            <a href="tel:+12148998311" class="btn btn-phone">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
              </svg>
              Call +1 (214) 899-8311
            </a>
          </div>
        </div>

        <div class="hero-visual">
          <div class="hero-frame">
            <img src="{rel}assets/images/sanctuary-reading-table.jpg" alt="9th Chakra Spiritual Consultation Desk featuring crystal sphere, zodiac rug, and white wingback chairs" width="600" height="480" loading="eager" />
            <div class="hero-frame-badge">
              <span class="chakra-badge-dot" style="background:var(--gold-primary);"></span>
              <span>The Private Reading Sanctuary</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Experience and Trust Strip (Continuous Auto-scrolling Marquee) -->
    <section class="trust-strip" aria-label="Key Practice Credentials">
      <div class="trust-marquee-wrapper">
        <div class="trust-marquee-track">
          <!-- Marquee Set 1 -->
          <div class="trust-item">
            <div class="trust-icon-box" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 16 14"></polyline>
              </svg>
            </div>
            <div class="trust-text">
              <h3>30+ Years of Experience</h3>
              <p>Three decades of continuous private spiritual counsel, intuition, and trusted insight.</p>
            </div>
          </div>

          <div class="trust-item">
            <div class="trust-icon-box" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
              </svg>
            </div>
            <div class="trust-text">
              <h3>Private Personal Guidance</h3>
              <p>A quiet, one-on-one environment honoring personal dignity, discretion, and individual choice.</p>
            </div>
          </div>

          <div class="trust-item">
            <div class="trust-icon-box" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="2" y1="12" x2="22" y2="12"></line>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
              </svg>
            </div>
            <div class="trust-text">
              <h3>International Clientele</h3>
              <p>Serving individuals, executives, and families in Dallas, across the US, and internationally.</p>
            </div>
          </div>

          <div class="trust-item">
            <div class="trust-icon-box" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
              </svg>
            </div>
            <div class="trust-text">
              <h3>Strict Discretion &amp; Privacy</h3>
              <p>Uncompromising confidentiality, mutual respect, and dedicated personal attention.</p>
            </div>
          </div>

          <div class="trust-item">
            <div class="trust-icon-box" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
              </svg>
            </div>
            <div class="trust-text">
              <h3>Grounded Perspective</h3>
              <p>Illuminating tendencies and choices while fully honoring your personal free will.</p>
            </div>
          </div>

          <!-- Marquee Set 2 (Duplicate for Seamless Continuous Loop) -->
          <div class="trust-item" aria-hidden="true">
            <div class="trust-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 16 14"></polyline>
              </svg>
            </div>
            <div class="trust-text">
              <h3>30+ Years of Experience</h3>
              <p>Three decades of continuous private spiritual counsel, intuition, and trusted insight.</p>
            </div>
          </div>

          <div class="trust-item" aria-hidden="true">
            <div class="trust-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
              </svg>
            </div>
            <div class="trust-text">
              <h3>Private Personal Guidance</h3>
              <p>A quiet, one-on-one environment honoring personal dignity, discretion, and individual choice.</p>
            </div>
          </div>

          <div class="trust-item" aria-hidden="true">
            <div class="trust-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="2" y1="12" x2="22" y2="12"></line>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
              </svg>
            </div>
            <div class="trust-text">
              <h3>International Clientele</h3>
              <p>Serving individuals, executives, and families in Dallas, across the US, and internationally.</p>
            </div>
          </div>

          <div class="trust-item" aria-hidden="true">
            <div class="trust-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
              </svg>
            </div>
            <div class="trust-text">
              <h3>Strict Discretion &amp; Privacy</h3>
              <p>Uncompromising confidentiality, mutual respect, and dedicated personal attention.</p>
            </div>
          </div>

          <div class="trust-item" aria-hidden="true">
            <div class="trust-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
              </svg>
            </div>
            <div class="trust-text">
              <h3>Grounded Perspective</h3>
              <p>Illuminating tendencies and choices while fully honoring your personal free will.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Core Services Overview (Photographic Cards & Mobile Auto-Scroll) -->
    <section class="section section-alt" aria-labelledby="servicesHeading">
      <div class="container">
        <div class="section-header">
          <div class="eyebrow">Personalized Counsel</div>
          <h2 id="servicesHeading">Personal Guidance for Every Chapter of Life.</h2>
          <p>
            Every situation requires a nuanced approach. Explore our dedicated spiritual guidance and energy healing modalities designed to bring focus, balance, and renewed perspective.
          </p>
        </div>

        <div class="services-slider-container">
          <div class="services-slider-track cards-grid-3">
            <!-- 1. Tarot Reading -->
            <article class="service-card service-card-has-img">
              <div class="service-card-thumb-wrap">
                <img src="{rel}assets/images/services/tarot-reading/hero.jpg" alt="Tarot Reading session setting" loading="lazy" width="400" height="250" />
                <span class="service-card-thumb-badge">
                  <span class="chakra-badge-dot" style="background:var(--gold-primary);"></span>
                  Perspective
                </span>
              </div>
              <div class="service-card-body">
                <h3>Tarot Reading</h3>
                <p>
                  A reflective, symbol-rich exploration of past experiences, current dynamics, and emerging choices to illuminate personal clarity.
                </p>
                <a href="{rel}services/tarot-reading.html" class="link-arrow">
                  Learn More
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </a>
              </div>
            </article>

            <!-- 2. Psychic Reading -->
            <article class="service-card service-card-has-img">
              <div class="service-card-thumb-wrap">
                <img src="{rel}assets/images/services/psychic-reading/hero.jpg" alt="Intuitive psychic reading sanctuary setting" loading="lazy" width="400" height="250" />
                <span class="service-card-thumb-badge">
                  <span class="chakra-badge-dot" style="background:var(--chakra-third-eye);"></span>
                  Intuition
                </span>
              </div>
              <div class="service-card-body">
                <h3>Psychic Reading</h3>
                <p>
                  Direct intuitive insight focused on relationships, emotional connections, career transitions, and unseen energetic patterns.
                </p>
                <a href="{rel}services/psychic-reading.html" class="link-arrow">
                  Learn More
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </a>
              </div>
            </article>

            <!-- 3. Medium Reading -->
            <article class="service-card service-card-has-img">
              <div class="service-card-thumb-wrap">
                <img src="{rel}assets/images/services/medium-reading/hero.jpg" alt="Peaceful medium reading sanctuary environment" loading="lazy" width="400" height="250" />
                <span class="service-card-thumb-badge">
                  <span class="chakra-badge-dot" style="background:var(--chakra-crown);"></span>
                  Connection
                </span>
              </div>
              <div class="service-card-body">
                <h3>Medium Reading</h3>
                <p>
                  A compassionate, sacred space for interpreting impressions, memories, and spiritual connection with loved ones who have transitioned.
                </p>
                <a href="{rel}services/medium-reading.html" class="link-arrow">
                  Learn More
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </a>
              </div>
            </article>

            <!-- 4. Reiki & Seichim Energy Healing -->
            <article class="service-card service-card-has-img">
              <div class="service-card-thumb-wrap">
                <img src="{rel}assets/images/services/energy-healing/hero.jpg" alt="Reiki and Seichim energy healing treatment table" loading="lazy" width="400" height="250" />
                <span class="service-card-thumb-badge">
                  <span class="chakra-badge-dot" style="background:var(--chakra-heart);"></span>
                  Renewal
                </span>
              </div>
              <div class="service-card-body">
                <h3>Reiki &amp; Seichim Energy Healing</h3>
                <p>
                  Ancient vibrational energy work facilitating profound relaxation, release of accumulated stress, and spiritual balance.
                </p>
                <a href="{rel}services/energy-healing.html" class="link-arrow">
                  Learn More
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </a>
              </div>
            </article>

            <!-- 5. Chakra Balancing & Aura Cleansing -->
            <article class="service-card service-card-has-img">
              <div class="service-card-thumb-wrap">
                <img src="{rel}assets/images/services/chakra-balancing/hero.jpg" alt="Chakra balancing and aura cleansing meditation space" loading="lazy" width="400" height="250" />
                <span class="service-card-thumb-badge">
                  <span class="chakra-badge-dot" style="background:var(--chakra-solar);"></span>
                  Harmonize
                </span>
              </div>
              <div class="service-card-body">
                <h3>Chakra Balancing &amp; Aura Cleansing</h3>
                <p>
                  Aligning the seven primary energy centers to restore vitality, clear emotional density, and promote whole-body spiritual harmony.
                </p>
                <a href="{rel}services/chakra-balancing-aura-cleansing.html" class="link-arrow">
                  Learn More
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </a>
              </div>
            </article>

            <!-- 6. Holistic Counseling & Guidance -->
            <article class="service-card service-card-has-img">
              <div class="service-card-thumb-wrap">
                <img src="{rel}assets/images/services/holistic-counseling/hero.jpg" alt="Holistic counseling consultation room with armchairs" loading="lazy" width="400" height="250" />
                <span class="service-card-thumb-badge">
                  <span class="chakra-badge-dot" style="background:var(--chakra-throat);"></span>
                  Insight
                </span>
              </div>
              <div class="service-card-body">
                <h3>Holistic Counseling &amp; Guidance</h3>
                <p>
                  A collaborative exploration of recurring patterns, relationships, life purpose, and personal growth for independent decision-making.
                </p>
                <a href="{rel}services/holistic-counseling.html" class="link-arrow">
                  Learn More
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </a>
              </div>
            </article>

            <!-- 7. Meditation -->
            <article class="service-card service-card-has-img" style="grid-column: 1 / -1; max-width: 580px; margin: 0 auto; width:100%;">
              <div class="service-card-thumb-wrap">
                <img src="{rel}assets/images/services/meditation/hero.jpg" alt="Guided meditation outdoor sunrise setting" loading="lazy" width="400" height="250" />
                <span class="service-card-thumb-badge">
                  <span class="chakra-badge-dot" style="background:var(--champagne);"></span>
                  Stillness
                </span>
              </div>
              <div class="service-card-body">
                <h3>Meditation Guidance</h3>
                <p>
                  Guided practices fostering inner stillness, breath awareness, emotional composure, and deeper connection with your spiritual center.
                </p>
                <a href="{rel}services/meditation.html" class="link-arrow">
                  Learn More
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </a>
              </div>
            </article>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 5: Areas of Personal Guidance -->
    <section class="section" aria-labelledby="guidanceHeading">
      <div class="container">
        <div class="section-header">
          <div class="eyebrow">Focused Clarity</div>
          <h2 id="guidanceHeading">Understanding the Questions That Matter.</h2>
          <p>
            Life rarely unfolds along a simple path. We explore the central questions, relationship dynamics, and crossroads that shape your everyday peace of mind.
          </p>
        </div>

        <div class="guidance-grid">
          <div class="guidance-item">
            <div class="guidance-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
              </svg>
            </div>
            <div class="guidance-text">
              <h4>Love &amp; Emotional Connections</h4>
              <p>Understanding partnership dynamics, communication blockages, unspoken emotional ties, and mutual compatibility.</p>
            </div>
          </div>

          <div class="guidance-item">
            <div class="guidance-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M8 14s1.5 2 4 2 4-2 4-2"></path>
                <line x1="9" y1="9" x2="9.01" y2="9"></line>
                <line x1="15" y1="9" x2="15.01" y2="9"></line>
              </svg>
            </div>
            <div class="guidance-text">
              <h4>Marriage &amp; Reconciliation Challenges</h4>
              <p>Navigating emotional distance, complex separations, and exploring whether renewed alignment is possible or healthy.</p>
            </div>
          </div>

          <div class="guidance-item">
            <div class="guidance-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
                <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
              </svg>
            </div>
            <div class="guidance-text">
              <h4>Career &amp; Professional Uncertainty</h4>
              <p>Evaluating executive transitions, business ventures, leadership choices, and finding alignment between ambition and values.</p>
            </div>
          </div>

          <div class="guidance-item">
            <div class="guidance-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
              </svg>
            </div>
            <div class="guidance-text">
              <h4>Important Life Transitions</h4>
              <p>Gaining composure and steady orientation during relocations, family restructuring, or major personal milestones.</p>
            </div>
          </div>

          <div class="guidance-item">
            <div class="guidance-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="3"></circle>
                <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
              </svg>
            </div>
            <div class="guidance-text">
              <h4>Self-Understanding &amp; Inner Growth</h4>
              <p>Recognizing recurring personal cycles, reconnecting with intuition, and unlocking personal clarity.</p>
            </div>
          </div>

          <div class="guidance-item">
            <div class="guidance-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon>
                <line x1="8" y1="2" x2="8" y2="18"></line>
                <line x1="16" y1="6" x2="16" y2="22"></line>
              </svg>
            </div>
            <div class="guidance-text">
              <h4>Finding Direction in Periods of Ambiguity</h4>
              <p>Cultivating grounded discernment when too many voices, pressures, or obligations create mental fatigue.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: A Personal and Intuitive Approach (3 Stages) -->
    <section class="section section-alt" aria-labelledby="processHeading">
      <div class="container">
        <div class="section-header">
          <div class="eyebrow">The Reading Process</div>
          <h2 id="processHeading">Every Journey Is Personal.</h2>
          <p>
            Spiritual guidance should never be hurried or cookie-cutter. Our three-stage approach guarantees thoughtful listening and practical, empowering insights.
          </p>
        </div>

        <div class="process-grid">
          <div class="process-step">
            <div class="process-num">01</div>
            <h3>Understanding Your Situation</h3>
            <p>
              We take time to listen carefully to your concerns, current dilemmas, and the underlying questions prompting your search for perspective.
            </p>
          </div>

          <div class="process-step">
            <div class="process-num">02</div>
            <h3>Exploring Insight &amp; Perspective</h3>
            <p>
              Using the relevant reading or energetic practice, we explore impressions, recurring emotional patterns, and potential trajectories.
            </p>
          </div>

          <div class="process-step">
            <div class="process-num">03</div>
            <h3>Finding Personal Direction</h3>
            <p>
              We bring the insights into focus, empowering you to reflect clearly, make independent choices, and move forward with peace of mind.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 7: Private Guidance and International Clientele -->
    <section class="section" aria-labelledby="intlHeading">
      <div class="container">
        <div class="hero-grid" style="align-items:center;">
          <div class="hero-content">
            <div class="eyebrow">Global Reach &middot; Local Presence</div>
            <h2 id="intlHeading">Personal Attention. Wherever Life Takes You.</h2>
            <p>
              Serving an international clientele, 9th Chakra Psychic offers a personal approach to spiritual guidance. Each individual brings a different story, experience, and set of questions. The focus is always on listening, understanding, and providing thoughtful perspective.
            </p>
            <p>
              Whether you reside locally in the Dallas-Fort Worth metroplex or connect from London, New York, Tokyo, or Sydney, every consultation is conducted with the utmost confidentiality, cultural appreciation, and individual care.
            </p>
            <div class="btn-group" style="margin-top:28px;">
              <a href="{rel}contact.html" class="btn btn-gold">Inquire for Private Session</a>
              <a href="tel:+12148998311" class="btn btn-outline">+1 (214) 899-8311</a>
            </div>
          </div>

          <div class="hero-visual">
            <div class="hero-frame">
              <img src="{rel}assets/images/sanctuary-crystal-altar.jpg" alt="Intimate crystal and tarot sanctuary table with amethyst geode and warm lighting" width="600" height="480" loading="lazy" />
              <div class="hero-frame-badge">
                <span class="chakra-badge-dot" style="background:var(--gold-primary);"></span>
                <span>Atmospheric Consultation Sanctuary</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 8: Gallery Preview (Editorial Bento Sanctuary Showcase) -->
    <section class="section section-alt" aria-labelledby="galleryHeading">
      <div class="container">
        <div class="section-header">
          <div class="eyebrow">Sanctuary Atmosphere</div>
          <h2 id="galleryHeading">A Glimpse Into the Spiritual Journey.</h2>
          <p>
            Experience the calm, restorative environment of our private consultation sanctuary, sacred tools, and spiritual aesthetic.
          </p>
        </div>

        <div class="sanctuary-bento-grid">
          <!-- 1. Large Featured Frame (Left Side) -->
          <div class="bento-featured-item">
            <img src="{rel}assets/images/sanctuary-reading-table-crop.jpg" alt="Crystal consultation desk with astrological zodiac rug and crystal ball" loading="lazy" width="700" height="460" />
            <div class="bento-badge">Featured Sanctuary View</div>
            <div class="bento-caption">
              <h4>Consultation Sanctuary</h4>
              <p>Private crystal desk, astrological zodiac rug, and white wingback armchairs.</p>
            </div>
          </div>

          <!-- 2. Right Column Stack -->
          <div class="bento-stack">
            <!-- Top Wide Card -->
            <div class="bento-item-wide">
              <img src="{rel}assets/images/sanctuary-chakras-room-crop.jpg" alt="Chakra discs alignment on doorway in sanctuary consultation room" loading="lazy" width="600" height="220" />
              <div class="bento-caption">
                <h4>The Chakra Chamber</h4>
                <p>Doorway displaying the 7 aligned rainbow energy centers.</p>
              </div>
            </div>

            <!-- Bottom Split Row (2 Columns) -->
            <div class="bento-split-row">
              <div class="bento-item-sub">
                <img src="{rel}assets/images/sanctuary-palmistry-neon-crop.jpg" alt="Illuminated cobalt neon palmistry hand art in sanctuary window" loading="lazy" width="300" height="220" />
                <div class="bento-caption">
                  <h4>Intuitive Palmistry</h4>
                  <p>Cobalt neon art in sanctuary window.</p>
                </div>
              </div>
              <div class="bento-item-sub">
                <img src="{rel}assets/images/sanctuary-crystal-altar-crop.jpg" alt="Amethyst crystal geode and tarot deck arrangement" loading="lazy" width="300" height="220" />
                <div class="bento-caption">
                  <h4>Crystal Altar &amp; Tarot</h4>
                  <p>Amethyst geode, tarot deck, &amp; sphere.</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div style="text-align:center; margin-top:40px;">
          <a href="{rel}gallery.html" class="btn btn-outline">Explore Full Gallery</a>
        </div>
      </div>
    </section>

    <!-- Section 9: Blog Preview -->
    <section class="section" aria-labelledby="blogHeading">
      <div class="container">
        <div class="section-header">
          <div class="eyebrow">Spiritual Journal</div>
          <h2 id="blogHeading">Insights for Your Personal Journey.</h2>
          <p>
            Thoughtful articles on tarot preparation, the chakra energy system, and navigating emotional uncertainty with dignity.
          </p>
        </div>

        <div class="cards-grid-3">
          <!-- Article 1 -->
          <article class="blog-card">
            <div class="blog-card-img-wrap">
              <img src="{rel}assets/images/blog/tarot-prep.jpg" alt="How to prepare for a tarot reading spread layout with cards and candle" width="600" height="375" loading="lazy" />
              <span class="blog-tag">Tarot &middot; 5 Min Read</span>
            </div>
            <div class="blog-card-content">
              <h3>How to Prepare for a Tarot Reading: Questions, Intentions, and Expectations</h3>
              <p>
                Discover how setting clear intentions and formulating open-ended inquiries creates the most transformative reading experience.
              </p>
              <a href="{rel}blog/how-to-prepare-for-a-tarot-reading.html" class="link-arrow">
                Read Article
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </a>
            </div>
          </article>

          <!-- Article 2 -->
          <article class="blog-card">
            <div class="blog-card-img-wrap">
              <img src="{rel}assets/images/blog/chakras-guide.jpg" alt="The seven chakra gemstones and subtle energy centers guide" width="600" height="375" loading="lazy" />
              <span class="blog-tag">Energy &middot; 7 Min Read</span>
            </div>
            <div class="blog-card-content">
              <h3>Understanding the Seven Chakras: A Gentle Guide to Energy Centers</h3>
              <p>
                A grounded introduction to the human energetic framework, from the grounding root to the expansive crown center.
              </p>
              <a href="{rel}blog/understanding-the-seven-chakras.html" class="link-arrow">
                Read Article
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </a>
            </div>
          </article>

          <!-- Article 3 -->
          <article class="blog-card">
            <div class="blog-card-img-wrap">
              <img src="{rel}assets/images/blog/relationship-clarity.jpg" alt="Navigating relationship uncertainty, reflection journal and contemplative tea setting" width="600" height="375" loading="lazy" />
              <span class="blog-tag">Relationships &middot; 6 Min Read</span>
            </div>
            <div class="blog-card-content">
              <h3>Navigating Relationship Uncertainty: Reflection, Boundaries, and Personal Clarity</h3>
              <p>
                Practical wisdom on recognizing recurring dynamics, honoring boundaries, and finding clarity during emotional transitions.
              </p>
              <a href="{rel}blog/navigating-relationship-uncertainty.html" class="link-arrow">
                Read Article
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </a>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Section 10: Closing Contact Section -->
    <section class="section section-alt" aria-labelledby="ctaHeading">
      <div class="container">
        <div class="service-cta-box" style="flex-direction:column; text-align:center; padding:clamp(40px, 6vw, 64px) clamp(24px, 4vw, 48px);">
          <div class="eyebrow">Connect Personally</div>
          <h2 id="ctaHeading" style="font-size:clamp(1.9rem, 3.5vw, 2.75rem); max-width:760px; margin:0 auto 16px auto;">
            Sometimes, a Different Perspective Changes Everything.
          </h2>
          <p style="max-width:680px; margin:0 auto 28px auto; font-size:1.1rem; color:var(--champagne);">
            Whether you are navigating a personal challenge, seeking insight into a relationship, or looking for direction during an important life transition, take a moment to explore the guidance available.
          </p>
          <div class="btn-group" style="justify-content:center;">
            <a href="tel:+12148998311" class="btn btn-gold">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
              </svg>
              Call +1 (214) 899-8311
            </a>
            <a href="{rel}contact.html" class="btn btn-outline">Contact Us</a>
          </div>
        </div>
      </div>
    </section>
    """
