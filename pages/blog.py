# pages/blog.py
"""Blog listing page and the 3 complete editorial blog articles."""

def render_blog_index(rel=""):
    return f"""
    <!-- Blog Master Hero Section -->
    <section class="blog-index-hero" aria-labelledby="blogIndexHeading">
      <div class="blog-hero-bg-overlay" aria-hidden="true">
        <img src="{rel}assets/images/blog/tarot-featured.jpg" alt="" class="blog-hero-bg-img" loading="eager" />
        <div class="blog-hero-gradient-scrim"></div>
      </div>
      <div class="container" style="position:relative; z-index:2;">

        <div class="blog-hero-content">
          <div class="eyebrow">
            <span class="eyebrow-dot"></span>
            Spiritual Journal &middot; Perspectives
          </div>
          <h1 id="blogIndexHeading" class="blog-hero-title">
            Insights for Your Personal Journey.
          </h1>
          <p class="blog-hero-description" style="margin-bottom:0;">
            Reflective essays, practical guides, and grounded spiritual wisdom developed over three decades of private intuitive counsel in Dallas and for clients worldwide.
          </p>
        </div>
      </div>
    </section>

    <!-- Articles Showcase Grid Section -->
    <section class="section" style="padding-top:clamp(40px, 6vw, 64px); padding-bottom:80px;" aria-label="Spiritual Guidance Articles">
      <div class="container">
        <div class="section-header text-left" style="margin-bottom:36px;">
          <div class="eyebrow">Published Articles</div>
          <h2 style="font-size:clamp(1.8rem, 2.8vw, 2.4rem);">All Journal Entries.</h2>
        </div>

        <!-- Article Cards Grid -->
        <div class="cards-grid-3">
          <!-- Article 1 -->
          <article class="blog-card">
            <div class="blog-card-img-wrap">
              <img src="{rel}assets/images/blog/tarot-prep.jpg" alt="Tarot cards on reading table" width="600" height="375" loading="lazy" />
              <span class="blog-tag">Tarot &middot; 6 Min Read</span>
            </div>
            <div class="blog-card-content">
              <h3>How to Prepare for a Tarot Reading: Questions, Intentions, and Expectations</h3>
              <p>
                Learn how setting clear intentions and formulating thoughtful inquiries elevates your reading from mere curiosity into a deeply reflective tool.
              </p>
              <a href="{rel}blog/how-to-prepare-for-a-tarot-reading.html" class="link-arrow">
                Read Article <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </a>
            </div>
          </article>

          <!-- Article 2 -->
          <article class="blog-card">
            <div class="blog-card-img-wrap">
              <img src="{rel}assets/images/blog/chakras-guide.jpg" alt="The seven chakra energy centers aligned" width="600" height="375" loading="lazy" />
              <span class="blog-tag">Chakras &middot; 8 Min Read</span>
            </div>
            <div class="blog-card-content">
              <h3>Understanding the Seven Chakras: A Gentle Guide to Energy Centers</h3>
              <p>
                A grounded exploration of the human subtle body traditions, examining each chakra's psychological, emotional, and spiritual significance.
              </p>
              <a href="{rel}blog/understanding-the-seven-chakras.html" class="link-arrow">
                Read Article <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </a>
            </div>
          </article>

          <!-- Article 3 -->
          <article class="blog-card">
            <div class="blog-card-img-wrap">
              <img src="{rel}assets/images/blog/relationship-clarity.jpg" alt="Interconnected rings representing emotional clarity" width="600" height="375" loading="lazy" />
              <span class="blog-tag">Relationships &middot; 7 Min Read</span>
            </div>
            <div class="blog-card-content">
              <h3>Navigating Relationship Uncertainty: Reflection, Boundaries, and Personal Clarity</h3>
              <p>
                Practical wisdom on recognizing recurring dynamics, honoring boundaries, and finding clarity during emotional transitions and reconciliation crossroads.
              </p>
              <a href="{rel}blog/navigating-relationship-uncertainty.html" class="link-arrow">
                Read Article <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </a>
            </div>
          </article>
        </div>
      </div>
    </section>
    """

def render_article_1(rel=""):
    return f"""
    <!-- ARTICLE 1 HERO SECTION -->
    <header class="article-detail-hero" aria-labelledby="art1Heading">
      <div class="article-hero-bg-overlay" aria-hidden="true">
        <img src="{rel}assets/images/blog/tarot-prep.jpg" alt="" class="article-hero-bg-img" loading="eager" />
        <div class="article-hero-gradient-scrim"></div>
      </div>
      <div class="container" style="position:relative; z-index:2;">

        <div class="article-hero-content">
          <div class="eyebrow">
            <span class="eyebrow-dot"></span>
            Tarot &amp; Esoteric Reflection
          </div>
          <h1 id="art1Heading" class="article-hero-title">
            How to Prepare for a Tarot Reading: Questions, Intentions, and Expectations
          </h1>
        </div>
      </div>
    </header>

    <article class="section" style="padding-top:clamp(40px, 6vw, 64px); padding-bottom:80px;">
      <div class="container container-narrow">
        <div class="article-body">
          <h2>1. Introduction</h2>
          <p>
            For centuries, the tarot has captivated the human imagination. In a world saturated with noise, analytical spreadsheets, and relentless notifications, pausing for a tarot consultation offers a rare moment of contemplative stillness. Yet, many people approach a reading with apprehension or misconception, often expecting theatrical fortune-telling or fixed, unavoidable prophecies.
          </p>
          <p>
            When approached with intentionality, tarot is not an exercise in fatalism; it is a profound symbolic dialogue between your conscious questions, subtle emotional currents, and the rich archetypes of the cards. Understanding how to prepare your mind, frame your inquiries, and ground your expectations can make the difference between a superficial encounter and a deeply clarifying consultation.
          </p>

          <h2>2. What a Tarot Reading Truly Is</h2>
          <p>
            At its core, a tarot deck consists of 78 cards divided into the Major Arcana (representing universal human archetypes and significant life passages) and the Minor Arcana (reflecting daily experiences, mental frameworks, emotions, and practical choices).
          </p>
          <p>
            A skilled reader does not claim supernatural control over the future. Rather, the cards function as an intuitive mirror. When the cards are shuffled and placed in purposeful arrangements (spreads), their imagery and relationships illuminate patterns, unseen obstacles, and overlooked emotional dynamics. Tarot clarifies the present moment so that you can navigate future possibilities with conscious discernment.
          </p>

          <h2>3. Why Personal Intentions Matter</h2>
          <p>
            Entering a consultation with a clear personal intention serves as an anchor. Intentions differ from rigid demands; an intention is about your readiness to observe reality truthfully and receive insight without defensiveness.
          </p>
          <p>
            Before your session, take five to ten quiet minutes. Take several slow, centering breaths. Ask yourself: <em>What part of my life feels most obscured right now? Am I willing to hear perspectives that challenge my preconceived assumptions?</em> When you arrive with an intention rooted in personal clarity rather than an urgent need to control external outcomes, the reading unfolds with remarkable depth.
          </p>

          <div class="article-quote">
            &ldquo;Tarot does not take away your power to decide; it illuminates the terrain so you can choose with courage and peace of mind.&rdquo;
          </div>

          <h2>4. How to Think About the Questions You Want to Explore</h2>
          <p>
            The way you formulate your questions directly influences the richness of the reading. Closed, yes-or-no questions often limit the dialogue to binary outcomes, which life rarely follows. Open-ended inquiries invite nuance and empowerment.
          </p>
          <p>Consider the difference between these common inquiry styles:</p>
          <ul>
            <li><strong>Closed:</strong> &ldquo;Will my partner and I stay together?&rdquo; &rarr; <strong>Open:</strong> &ldquo;What emotional patterns are currently influencing our relationship, and how can I foster healthy communication?&rdquo;</li>
            <li><strong>Closed:</strong> &ldquo;Will I get the job?&rdquo; &rarr; <strong>Open:</strong> &ldquo;What energies should I cultivate to align with my highest professional purpose at this crossroads?&rdquo;</li>
            <li><strong>Closed:</strong> &ldquo;When will my financial stress end?&rdquo; &rarr; <strong>Open:</strong> &ldquo;What mindset or practical blockages must I address to restore stability and confidence?&rdquo;</li>
          </ul>

          <h2>5. Approaching a Reading with an Open Mind</h2>
          <p>
            It is natural to hope for reassurance. However, genuine guidance requires emotional honesty. Occasionally, cards appear that evoke initial discomfort—such as the Tower (representing sudden disruption of outmoded structures) or the Three of Swords (reflecting sorrow that must be acknowledged).
          </p>
          <p>
            In authentic tarot, no card is inherently negative. Even challenging cards point toward necessary liberation, healing, and personal resilience. Approaching the cards with non-reactive curiosity allows the practitioner to help you transform potential challenges into conscious growth.
          </p>

          <h2>6. Understanding Card Symbolism</h2>
          <p>
            Every detail in a traditional tarot card—colors, numbers, sacred geometry, elements (fire, water, air, earth)—carries layered meaning. During your reading, you do not need to memorize these systems; your practitioner weaves these symbols together into a coherent narrative.
          </p>
          <p>
            Pay attention to the images that evoke an instinctive emotional reaction in you. Often, the card that catches your eye holds the most immediate resonance for your subconscious awareness.
          </p>

          <h2>7. What You May Take Away from the Experience</h2>
          <p>A thoughtful tarot reading typically leaves a client with:</p>
          <ul>
            <li>A renewed sense of validation regarding feelings they had intuitively sensed but had not yet articulated.</li>
            <li>Fresh perspective on interpersonal dynamics, helping release unnecessary self-blame or unrealistic expectations.</li>
            <li>Actionable clarity on concrete steps that can be taken right now.</li>
            <li>Deep emotional peace derived from being heard and understood without judgment.</li>
          </ul>

          <h2>8. Final Thoughts</h2>
          <p>
            Tarot is ultimately a dialogue of empowerment. By arriving grounded, with purposeful questions and an open heart, you unlock the full contemplative beauty of this ancient practice. Your future is not a predetermined script etched in stone—it is a living path being crafted by the conscious choices you make today.
          </p>

          <div class="service-cta-box">
            <div class="service-cta-text">
              <h4>Ready for a Private Tarot Reading?</h4>
              <p>Experience over 30 years of intuitive counsel tailored to your life questions.</p>
            </div>
            <a href="tel:+12148998311" class="btn btn-gold" style="flex-shrink:0;">
              Call +1 (214) 899-8311
            </a>
          </div>
        </div>
      </div>
    </article>
    """

def render_article_2(rel=""):
    return f"""
    <!-- ARTICLE 2 HERO SECTION -->
    <header class="article-detail-hero" aria-labelledby="art2Heading">
      <div class="article-hero-bg-overlay" aria-hidden="true">
        <img src="{rel}assets/images/blog/chakras-guide.jpg" alt="" class="article-hero-bg-img" loading="eager" />
        <div class="article-hero-gradient-scrim"></div>
      </div>
      <div class="container" style="position:relative; z-index:2;">

        <div class="article-hero-content">
          <div class="eyebrow">
            <span class="eyebrow-dot"></span>
            Energetic Anatomy &middot; Spiritual Traditions
          </div>
          <h1 id="art2Heading" class="article-hero-title">
            Understanding the Seven Chakras: A Gentle Guide to Energy Centers
          </h1>
        </div>
      </div>
    </header>

    <article class="section" style="padding-top:clamp(40px, 6vw, 64px); padding-bottom:80px;">
      <div class="container container-narrow">
        <div class="article-body">
          <h2>1. Introduction to Chakra Traditions</h2>
          <p>
            For millennia, Eastern contemplative traditions—specifically ancient Vedic philosophy and yogic sciences—have mapped the human experience not merely as a biological mechanism, but as an intricate interplay between consciousness and subtle energy. Central to this understanding is the concept of the <em>chakras</em> (derived from the Sanskrit word for &ldquo;wheel&rdquo; or &ldquo;disc&rdquo;).
          </p>
          <p>
            It is essential to clarify that within spiritual practice, chakras are understood not as physical anatomical organs, but as focal points of vital energy (Prana) aligned along the spine. They represent psycho-spiritual centers where physical sensation, emotion, mental perception, and spiritual consciousness intersect.
          </p>

          <h2>2. What the Seven Chakras Represent</h2>
          <p>
            The human energetic body is traditionally described as possessing seven principal chakras stacked vertically along the central channel, known as the <em>Sushumna</em>. Each center corresponds to distinct stages of personal development, psychological needs, color frequencies, and emotional archetypes. When energy flows harmoniously through these centers, an individual experiences vitality, emotional equilibrium, and a profound sense of inner wholeness.
          </p>

          <h2>3. The Root Chakra (Muladhara) — Crimson Red</h2>
          <p>
            Situated at the base of the spine and perineum, the Root Chakra represents our fundamental sense of safety, physical embodiment, and belonging on the earth.
          </p>
          <p>
            <strong>Themes:</strong> Survival, physical health, grounding, material security, stability.<br>
            <strong>When in balance:</strong> You feel centered, anchored in your physical body, and confident in your ability to provide for your daily needs.<br>
            <strong>When depleted or unsettled:</strong> Feelings of persistent anxiety, scarcity mindset, restlessness, or fear of abandonment.
          </p>

          <h2>4. The Sacral Chakra (Svadhisthana) — Warm Orange</h2>
          <p>
            Located just below the navel, the Sacral Chakra governs emotional fluidity, creative inspiration, and intimacy.
          </p>
          <p>
            <strong>Themes:</strong> Passion, emotional expression, pleasure, adaptability, sensuality.<br>
            <strong>When in balance:</strong> Creative projects flow naturally; you navigate interpersonal intimacy with grace and joy.<br>
            <strong>When depleted or unsettled:</strong> Creative apathy, emotional numbness, fear of vulnerability, or boundary challenges.
          </p>

          <h2>5. The Solar Plexus Chakra (Manipura) — Sun Yellow</h2>
          <p>
            Located in the upper abdomen around the stomach, this center is the seat of personal willpower, autonomy, and inner fire (Agni).
          </p>
          <p>
            <strong>Themes:</strong> Self-confidence, personal power, decision-making, discipline, purpose.<br>
            <strong>When in balance:</strong> You possess a healthy self-esteem, can state clear boundaries, and pursue meaningful goals with quiet determination.<br>
            <strong>When depleted or unsettled:</strong> Self-doubt, chronic procrastination, people-pleasing, or conversely, an urge to dominate others.
          </p>

          <div class="article-quote">
            &ldquo;When the lower chakras provide grounding and the upper chakras offer vision, the heart center becomes the bridge of authentic living.&rdquo;
          </div>

          <h2>6. The Heart Chakra (Anahata) — Emerald Green</h2>
          <p>
            Positioned at the center of the chest, Anahata serves as the sacred fulcrum uniting the three earthly, physical chakras below with the three spiritual centers above.
          </p>
          <p>
            <strong>Themes:</strong> Unconditional love, compassion, forgiveness, grief processing, interconnection.<br>
            <strong>When in balance:</strong> Empathy flows freely without losing personal boundaries; you can love and be loved with ease.<br>
            <strong>When depleted or unsettled:</strong> Guardedness, holding grudges, emotional coldness, or codependency.
          </p>

          <h2>7. The Throat Chakra (Vishuddha) — Sky Cyan</h2>
          <p>
            Located at the base of the throat, this center is the portal of truthful expression and authentic voice.
          </p>
          <p>
            <strong>Themes:</strong> Truth, communication, creative expression, listening, integrity.<br>
            <strong>When in balance:</strong> You speak your truth kindly and clearly; you listen attentively to others without defensiveness.<br>
            <strong>When depleted or unsettled:</strong> Swallowing words, fear of public speaking, gossiping, or difficulty articulating true feelings.
          </p>

          <h2>8. The Third Eye Chakra (Ajna) — Deep Indigo</h2>
          <p>
            Positioned between the eyebrows, Ajna is the center of intuition, spiritual perception, and mental clarity.
          </p>
          <p>
            <strong>Themes:</strong> Intuition, wisdom, insight, imagination, seeing past illusion.<br>
            <strong>When in balance:</strong> Your intuition is strong; you can discern truth from projection and maintain clear perspective in complex situations.<br>
            <strong>When depleted or unsettled:</strong> Over-intellectualizing every decision, lack of imagination, or cynicism toward spiritual realities.
          </p>

          <h2>9. The Crown Chakra (Sahasrara) — Violet &amp; Pure White</h2>
          <p>
            Resting at the crown of the head, Sahasrara represents our connection to universal consciousness, transcendence, and divine wisdom.
          </p>
          <p>
            <strong>Themes:</strong> Spiritual unity, higher purpose, peace, sacred connection.<br>
            <strong>When in balance:</strong> A quiet abiding sense that you are part of a larger, benevolent cosmos; release of existential dread.<br>
            <strong>When depleted or unsettled:</strong> Spiritual alienation, feeling disconnected from life, or excessive dogmatism.
          </p>

          <h2>10. Exploring Awareness and Balance</h2>
          <p>
            Chakra balancing is not about achieving rigid perfection. Life is dynamic, and our energy centers naturally expand and contract in response to daily interactions, stress, relationships, and seasons.
          </p>
          <p>
            Cultivating energetic awareness involves simple contemplative check-ins: noticing where tension gathers in your body, spending time in nature to ground the root, speaking truthfully to open the throat, and making space for meditation to quiet the crown. In professional consultations, subtle vibrational work like Reiki and specialized aura cleansing assists in releasing accumulated blockages that self-care alone may struggle to shift.
          </p>

          <h2>11. Final Thoughts</h2>
          <p>
            The seven chakras offer a gentle, holistic map for understanding yourself as an integrated whole—mind, body, emotions, and spirit. By honoring each center with patience and care, you cultivate a grounded, luminous presence capable of meeting life with grace.
          </p>

          <div class="service-cta-box">
            <div class="service-cta-text">
              <h4>Experience Chakra Balancing &amp; Aura Cleansing</h4>
              <p>Harmonize your subtle energy centers in a private, restorative consultation.</p>
            </div>
            <a href="tel:+12148998311" class="btn btn-gold" style="flex-shrink:0;">
              Call +1 (214) 899-8311
            </a>
          </div>
        </div>
      </div>
    </article>
    """

def render_article_3(rel=""):
    return f"""
    <!-- ARTICLE 3 HERO SECTION -->
    <header class="article-detail-hero" aria-labelledby="art3Heading">
      <div class="article-hero-bg-overlay" aria-hidden="true">
        <img src="{rel}assets/images/blog/relationship-clarity.jpg" alt="" class="article-hero-bg-img" loading="eager" />
        <div class="article-hero-gradient-scrim"></div>
      </div>
      <div class="container" style="position:relative; z-index:2;">

        <div class="article-hero-content">
          <div class="eyebrow">
            <span class="eyebrow-dot"></span>
            Relationships &middot; Emotional Clarity
          </div>
          <h1 id="art3Heading" class="article-hero-title">
            Navigating Relationship Uncertainty: Reflection, Boundaries, and Personal Clarity
          </h1>
        </div>
      </div>
    </header>

    <article class="section" style="padding-top:clamp(40px, 6vw, 64px); padding-bottom:80px;">
      <div class="container container-narrow">
        <div class="article-body">
          <h2>1. Introduction</h2>
          <p>
            Few experiences in human life are as disorienting as relationship uncertainty. Whether it manifests as subtle emotional withdrawal, prolonged communication breakdowns, or the painful ambiguity of separation, relationship crossroads test our emotional resilience to its core.
          </p>
          <p>
            In moments of romantic crisis, individuals frequently seek spiritual readings in search of quick guarantees or reassurance that an estranged partner will immediately return. Responsible intuitive guidance, however, takes a much deeper and more honorable stance. While we examine interpersonal dynamics and energetic ties, true spiritual clarity focuses on returning you to your center, helping you discern healthy possibilities from destructive illusions.
          </p>

          <h2>2. Understanding Emotional Uncertainty</h2>
          <p>
            When a relationship enters ambiguity, the human nervous system naturally triggers distress. We crave resolution—any resolution—simply to escape the painful discomfort of not knowing.
          </p>
          <p>
            The first step toward clarity is learning to pause. Impulsive actions driven by fear—such as barrage texting, over-analyzing social media, or demanding instant ultimatums—frequently exacerbate the very tension you seek to relieve. Recognizing that uncertainty is a temporary season allows you to slow down and observe dynamics with greater composure.
          </p>

          <h2>3. Recognizing Communication Patterns</h2>
          <p>
            Relationships thrive or falter not solely on feelings of love, but on behavioral patterns. During intuitive counsel, we often look at recurring interaction loops:
          </p>
          <ul>
            <li><strong>The Pursuer-Distancer Dynamic:</strong> Where one partner's anxiety prompts pursuit, which drives the other partner into defensive retreat.</li>
            <li><strong>Unspoken Resentments:</strong> Needs that were never voiced directly, eventually curdling into passive withdrawal or sudden rupture.</li>
            <li><strong>Projection:</strong> Projecting unhealed wounds from childhood or previous relationships onto the present partner.</li>
          </ul>
          <p>
            Identifying these patterns does not mean assigning blame; it means understanding the emotional climate so conscious choices can replace automatic reactions.
          </p>

          <div class="article-quote">
            &ldquo;Spiritual guidance cannot force another soul to change; it provides you with the discernment to see where truth, respect, and mutual willingness truly lie.&rdquo;
          </div>

          <h2>4. Exploring Expectations and Realities</h2>
          <p>
            Often, our suffering stems not from what another person is actually doing, but from the gap between who they are and who we wish they would be.
          </p>
          <p>
            Ask yourself with compassionate honesty: <em>Am I in love with the actual person standing before me today, with their demonstrated behaviors and limitations, or am I holding onto potential that requires them to become someone else?</em> Honoring reality is not defeat—it is the foundational prerequisite for genuine love and peace of mind.
          </p>

          <h2>5. The Importance of Healthy Boundaries</h2>
          <p>
            A common misconception in spiritual communities is that &ldquo;unconditional love&rdquo; requires unconditional tolerance of disrespect or emotional neglect.
          </p>
          <p>
            Love can be boundless, but relationships require container walls. Boundaries are not punitive walls designed to hurt the other; they are clear, loving definitions of what you need to feel safe, respected, and valued. Without boundaries, attempts at reconciliation inevitably devolve into repeated cycles of heartbreak.
          </p>

          <h2>6. Considering Reconciliation Thoughtfully</h2>
          <p>
            When navigating marriage challenges or estrangement, reconciliation is often deeply desired. However, healthy reconciliation is never merely &ldquo;getting back together.&rdquo;
          </p>
          <p>
            For a relationship to heal, both individuals must demonstrate genuine mutual accountability, a willingness to examine past mistakes, and concrete changes in communication. If only one person is doing the emotional work, the dynamic remains unbalanced. Spiritual insight helps illuminate whether a genuine mutual door exists or whether closure is the more loving and dignified choice.
          </p>

          <h2>7. Taking Responsibility for Personal Decisions</h2>
          <p>
            No reading, tarot card, or spiritual advisor can or should make relationship decisions on your behalf. Your life and your heart belong to you.
          </p>
          <p>
            When you reclaim your power of choice, you step out of victimhood. Whether you choose to stay, to fight for renewal, or to walk away with grace, making that choice from a grounded place of self-respect changes everything.
          </p>

          <h2>8. Finding Clarity During Emotional Transitions</h2>
          <p>
            If a relationship does reach its conclusion, remember that endings in the spiritual perspective are not personal failures. Relationships serve as profound spiritual teachers. Sometimes, their highest purpose was to awaken you to your own worth, boundaries, and capacity for deep feeling.
          </p>

          <h2>9. Final Thoughts</h2>
          <p>
            Uncertainty is challenging, but it is also fertile ground for personal growth. By stepping back from panic, honoring boundaries, and listening to your inner truth, you emerge from relationship crossroads not broken, but wiser, clearer, and deeply grounded in your own dignity.
          </p>

          <div class="service-cta-box">
            <div class="service-cta-text">
              <h4>Seeking Perspective on Your Relationship?</h4>
              <p>Explore your connection in a private, confidential consultation with The Reader.</p>
            </div>
            <a href="tel:+12148998311" class="btn btn-gold" style="flex-shrink:0;">
              Call +1 (214) 899-8311
            </a>
          </div>
        </div>
      </div>
    </article>
    """
