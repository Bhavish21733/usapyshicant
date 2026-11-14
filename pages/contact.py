# pages/contact.py
"""Contact Us page template and content."""

def render_contact(rel=""):
    return f"""
    <section class="section" style="padding-top:clamp(50px, 7vw, 84px);" aria-labelledby="contactMainHeading">
      <div class="container">

        <div class="section-header text-left" style="max-width:820px; margin-bottom:48px;">
          <div class="eyebrow">Direct Spiritual Counsel</div>
          <h1 id="contactMainHeading">Begin With a Conversation.</h1>
          <p style="font-size:1.15rem; color:var(--champagne); line-height:1.7;">
            Every personal journey is different. Reach out to explore the available guidance services and discuss the area in which you are seeking perspective.
          </p>
        </div>

        <div class="contact-grid">
          <!-- Left Column: Contact Information & Phone Highlight -->
          <div class="contact-info-card">
            <h3>9th Chakra Psychic</h3>
            <p>
              Private spiritual counsel, intuitive readings, and energy healing with over 30 years of experience.
            </p>

            <div class="contact-highlight-phone">
              <div class="contact-highlight-label">Direct Telephone Counsel</div>
              <a href="tel:+12148998311" class="contact-highlight-number" title="Call directly">+1 (214) 899-8311</a>
              <div style="font-size:0.84rem; color:var(--text-muted); margin-top:8px;">
                Available for inquiries and scheduling consultations
              </div>
            </div>

            <div style="margin-bottom:24px;">
              <h4 style="font-size:1.1rem; color:var(--champagne); margin-bottom:8px;">Serving Clients Worldwide</h4>
              <p style="font-size:0.92rem; color:var(--text-secondary); line-height:1.6; margin:0;">
                Serving clients in Dallas, Texas, across the United States, and internationally. Consultations are arranged directly by appointment to ensure undivided personal attention and discretion.
              </p>
            </div>

            <div style="border-top:1px solid var(--border-subtle); padding-top:20px;">
              <h4 style="font-size:1.05rem; color:var(--champagne); margin-bottom:6px;">Session Arrangements</h4>
              <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.55; margin:0;">
                Consultation formats (telephone, remote, or in-person arrangements) and specific appointment times are coordinated directly with the practitioner upon initial inquiry.
              </p>
            </div>

            <div style="margin-top:28px;">
              <a href="tel:+12148998311" class="btn btn-gold" style="width:100%;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                </svg>
                Call Now to Inquire
              </a>
            </div>
          </div>

          <!-- Right Column: Interactive Inquiry Form -->
          <div class="contact-form-wrap">
            <h3 style="font-size:1.6rem; margin-bottom:8px;">Send a Confidential Inquiry</h3>
            <p style="font-size:0.95rem; color:var(--text-secondary); margin-bottom:24px;">
              Share your details below to prepare your inquiry, or call directly for immediate scheduling.
            </p>

            <div id="formStatusAlert" class="form-status-alert" role="alert"></div>

            <form id="contactForm" novalidate>
              <div class="form-group">
                <label for="fullName" class="form-label">Full Name <span class="required">*</span></label>
                <input type="text" id="fullName" name="fullName" class="form-control" placeholder="Your full name" required autocomplete="name" />
                <div class="form-error-msg">Please enter your full name.</div>
              </div>

              <div class="form-group">
                <label for="emailAddress" class="form-label">Email Address <span class="required">*</span></label>
                <input type="email" id="emailAddress" name="emailAddress" class="form-control" placeholder="your.email@example.com" required autocomplete="email" />
                <div class="form-error-msg">Please enter a valid email address.</div>
              </div>

              <div class="form-group">
                <label for="contactNumber" class="form-label">Contact Telephone (Optional)</label>
                <input type="tel" id="contactNumber" name="contactNumber" class="form-control" placeholder="+1 (555) 000-0000" autocomplete="tel" />
              </div>

              <div class="form-group">
                <label for="serviceInterest" class="form-label">Service of Interest</label>
                <select id="serviceInterest" name="serviceInterest" class="form-control" style="background:#0E121A; color:var(--text-primary);">
                  <option value="general">General Spiritual Guidance Inquiry</option>
                  <option value="tarot">Tarot Reading</option>
                  <option value="psychic">Psychic Reading</option>
                  <option value="medium">Medium Reading</option>
                  <option value="energy">Reiki &amp; Seichim Energy Healing</option>
                  <option value="chakra">Chakra Balancing &amp; Aura Cleansing</option>
                  <option value="holistic">Holistic Counseling &amp; Guidance</option>
                  <option value="meditation">Meditation Guidance</option>
                </select>
              </div>

              <div class="form-group">
                <label for="message" class="form-label">Brief Note on What You Are Seeking <span class="required">*</span></label>
                <textarea id="message" name="message" class="form-control" rows="4" placeholder="Briefly share the area, relationship, or transition you wish to discuss..." required></textarea>
                <div class="form-error-msg">Please share a brief note about what you are seeking.</div>
              </div>

              <div class="form-group">
                <label class="form-checkbox-label">
                  <input type="checkbox" id="privacyConsent" name="privacyConsent" required />
                  <span>I agree to be contacted regarding this inquiry and acknowledge that spiritual counsel is an intuitive service provided for personal reflection.</span>
                </label>
                <div class="form-error-msg">Please confirm your consent to be contacted.</div>
              </div>

              <button type="submit" class="btn btn-gold" style="width:100%; margin-top:10px;">
                Prepare Inquiry Details
              </button>
            </form>
          </div>
        </div>

        <!-- Section 4: Contact FAQs -->
        <div style="margin-top:80px; max-width:840px; margin-left:auto; margin-right:auto;">
          <div class="section-header">
            <div class="eyebrow">Common Questions</div>
            <h2>Inquiry &amp; Scheduling Details</h2>
          </div>

          <div class="accordion">
            <div class="accordion-item">
              <button type="button" class="accordion-header" aria-expanded="false">
                <span>How can I inquire about a reading?</span>
                <span class="accordion-icon" aria-hidden="true">
                  <svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 1l4 4 4-4" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </span>
              </button>
              <div class="accordion-body">
                <p>
                  The most direct method is by telephone at <strong>+1 (214) 899-8311</strong>. You can discuss your area of interest directly with the practitioner and confirm convenient availability.
                </p>
              </div>
            </div>

            <div class="accordion-item">
              <button type="button" class="accordion-header" aria-expanded="false">
                <span>Which services are currently available?</span>
                <span class="accordion-icon" aria-hidden="true">
                  <svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 1l4 4 4-4" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </span>
              </button>
              <div class="accordion-body">
                <p>
                  All core modalities are available: Tarot Readings, Psychic Readings, Medium Readings, Reiki and Seichim Energy Healing, Chakra Balancing, Holistic Counseling, and Meditation. Secondary modalities (palmistry, crystal reading, past life reflection) may also be requested.
                </p>
              </div>
            </div>

            <div class="accordion-item">
              <button type="button" class="accordion-header" aria-expanded="false">
                <span>Do you serve international clients?</span>
                <span class="accordion-icon" aria-hidden="true">
                  <svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 1l4 4 4-4" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </span>
              </button>
              <div class="accordion-body">
                <p>
                  Yes, 9th Chakra Psychic serves clients across North America, Europe, Asia, and globally. Time-zone accommodations are arranged directly during scheduling.
                </p>
              </div>
            </div>

            <div class="accordion-item">
              <button type="button" class="accordion-header" aria-expanded="false">
                <span>How are session details and format arranged?</span>
                <span class="accordion-icon" aria-hidden="true">
                  <svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 1l4 4 4-4" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </span>
              </button>
              <div class="accordion-body">
                <p>
                  Whether your session is conducted by telephone or other preferred arrangement, all details—including timing, focus, and preparation—are confirmed personally during your initial conversation.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
