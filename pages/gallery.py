# pages/gallery.py
"""Gallery page template and content."""

def render_gallery(rel=""):
    return f"""
    <section class="section" style="padding-top:clamp(50px, 7vw, 84px);" aria-labelledby="galleryMainHeading">
      <div class="container">

        <div class="section-header text-left" style="max-width:820px; margin-bottom:40px;">
          <div class="eyebrow">Visual Sanctuary</div>
          <h1 id="galleryMainHeading">Explore the World of 9th Chakra Psychic.</h1>
          <p style="font-size:1.15rem; color:var(--champagne); line-height:1.7;">
            Step into our private Dallas consultation sanctuary, featuring authentic reading environments, crystal arrangements, celestial symbolism, and the sacred tools of spiritual counsel.
          </p>
        </div>

        <!-- Category Filter Tabs -->
        <div class="gallery-tabs" role="tablist" aria-label="Gallery Categories">
          <button type="button" class="gallery-tab active" data-category="all" role="tab" aria-selected="true">All Perspectives</button>
          <button type="button" class="gallery-tab" data-category="sanctuary" role="tab" aria-selected="false">Sanctuary Space</button>
          <button type="button" class="gallery-tab" data-category="tarot" role="tab" aria-selected="false">Tarot &amp; Cards</button>
          <button type="button" class="gallery-tab" data-category="crystals" role="tab" aria-selected="false">Crystals &amp; Altar</button>
          <button type="button" class="gallery-tab" data-category="chakras" role="tab" aria-selected="false">Chakras &amp; Energy</button>
          <button type="button" class="gallery-tab" data-category="meditation" role="tab" aria-selected="false">Meditation &amp; Peace</button>
        </div>

        <!-- Gallery Grid -->
        <div class="gallery-grid" id="galleryGrid">
          <!-- Item 1: Authentic Sanctuary Desk Photo -->
          <div class="gallery-item" data-category="sanctuary" data-title="The Reading Desk: Crystal sphere, gold hand, and astrological rug" tabindex="0" role="button" aria-label="View photo: The Reading Desk">
            <img src="{rel}assets/images/sanctuary-reading-table.jpg" alt="Crystal glass consultation desk with celestial zodiac rug and white wingback chairs" loading="lazy" width="600" height="450" />
            <div class="gallery-caption">
              <h4>The Reading Sanctuary</h4>
              <span>Sanctuary Space &middot; Dallas Practice</span>
            </div>
          </div>

          <!-- Item 2: Authentic Chakra Sanctuary Doorway -->
          <div class="gallery-item" data-category="sanctuary chakras" data-title="Chakra Chamber: Aligned energy symbols and celestial circle" tabindex="0" role="button" aria-label="View photo: Chakra Chamber">
            <img src="{rel}assets/images/sanctuary-chakras-room.jpg" alt="Chakra discs displayed along the sanctuary doorway with celestial sun carpet" loading="lazy" width="600" height="450" />
            <div class="gallery-caption">
              <h4>The Chakra Chamber</h4>
              <span>Chakras &amp; Energy Alignment</span>
            </div>
          </div>

          <!-- Item 3: Authentic Palmistry Neon Light -->
          <div class="gallery-item" data-category="sanctuary" data-title="Intuitive Palmistry Glow: Cobalt illuminated hand in sanctuary window" tabindex="0" role="button" aria-label="View photo: Intuitive Palmistry Glow">
            <img src="{rel}assets/images/sanctuary-palmistry-neon.jpg" alt="Cobalt blue illuminated palmistry hand artwork in window" loading="lazy" width="600" height="450" />
            <div class="gallery-caption">
              <h4>Intuitive Palmistry Glow</h4>
              <span>Sanctuary Atmosphere</span>
            </div>
          </div>

          <!-- Item 4: Authentic Crystal Altar & Desk View -->
          <div class="gallery-item" data-category="sanctuary crystals tarot" data-title="Crystal Altar: Amethyst geode, crystal sphere, and tarot desk" tabindex="0" role="button" aria-label="View photo: Crystal Altar">
            <img src="{rel}assets/images/sanctuary-crystal-altar.jpg" alt="Amethyst crystal geode and crystal sphere on glass reading desk" loading="lazy" width="600" height="450" />
            <div class="gallery-caption">
              <h4>Crystal Altar &amp; Tarot Desk</h4>
              <span>Crystals &amp; Sacred Tools</span>
            </div>
          </div>

          <!-- Item 5: Tarot Spread Concept -->
          <div class="gallery-item" data-category="tarot" data-title="Celtic Cross Tarot Arrangement on sacred velvet cloth" tabindex="0" role="button" aria-label="View artwork: Celtic Cross Tarot Arrangement">
            <img src="{rel}assets/svg/gallery-tarot-altar.svg" alt="Celtic Cross Tarot Spread layout artwork" loading="lazy" width="600" height="450" />
            <div class="gallery-caption">
              <h4>Celtic Cross Spread</h4>
              <span>Tarot &amp; Symbolism</span>
            </div>
          </div>

          <!-- Item 6: Singing Bowl & Sound Healing -->
          <div class="gallery-item" data-category="meditation" data-title="Tibetan Singing Bowl for harmonic sound meditation and clearing" tabindex="0" role="button" aria-label="View artwork: Tibetan Singing Bowl">
            <img src="{rel}assets/svg/gallery-sound-bowls.svg" alt="Tibetan singing bowl and sound harmonics artwork" loading="lazy" width="600" height="450" />
            <div class="gallery-caption">
              <h4>Harmonic Sound Bowl</h4>
              <span>Meditation &amp; Sound Healing</span>
            </div>
          </div>

          <!-- Item 7: Sacred Crystal Grid -->
          <div class="gallery-item" data-category="crystals chakras" data-title="Metatron Sacred Crystal Grid for energy amplification" tabindex="0" role="button" aria-label="View artwork: Metatron Sacred Crystal Grid">
            <img src="{rel}assets/svg/gallery-crystal-grid.svg" alt="Sacred geometry crystal grid layout with chakra stones" loading="lazy" width="600" height="450" />
            <div class="gallery-caption">
              <h4>Sacred Crystal Grid</h4>
              <span>Crystals &amp; Sacred Geometry</span>
            </div>
          </div>

          <!-- Item 8: Incense & Spiritual Contemplation -->
          <div class="gallery-item" data-category="meditation" data-title="Aromatic Incense Smoke &amp; Lunar Contemplation" tabindex="0" role="button" aria-label="View artwork: Incense & Lunar Contemplation">
            <img src="{rel}assets/svg/gallery-incense-reflection.svg" alt="Aromatic incense burner and rising celestial smoke" loading="lazy" width="600" height="450" />
            <div class="gallery-caption">
              <h4>Sacred Smoke &amp; Reflection</h4>
              <span>Contemplation &amp; Peace</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Accessible Lightbox Modal Dialog -->
    <div class="lightbox-modal" id="lightboxModal" role="dialog" aria-modal="true" aria-label="Image Preview" aria-hidden="true">
      <div class="lightbox-backdrop"></div>
      <button type="button" class="lightbox-btn lightbox-btn-close" aria-label="Close Image Preview">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>

      <button type="button" class="lightbox-btn lightbox-btn-prev" aria-label="Previous Image">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
      </button>

      <div class="lightbox-content">
        <img src="" alt="" class="lightbox-img" />
        <div class="lightbox-meta">
          <h3 class="lightbox-title"></h3>
          <span class="lightbox-counter"></span>
        </div>
      </div>

      <button type="button" class="lightbox-btn lightbox-btn-next" aria-label="Next Image">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </button>
    </div>
    """
