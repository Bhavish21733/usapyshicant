# pages/legal.py
"""Privacy Policy and Spiritual Services Disclaimer pages."""

def render_privacy_policy(rel=""):
    return f"""
    <section class="section" style="padding-top:clamp(50px, 7vw, 84px);" aria-labelledby="privacyHeading">
      <div class="container container-narrow">

        <header class="article-header text-left" style="margin-bottom:36px; padding:0;">
          <div class="eyebrow">Client Confidentiality</div>
          <h1 id="privacyHeading">Privacy Policy</h1>
          <div style="font-size:0.88rem; color:var(--text-muted); margin-top:8px;">
            Effective Date: November 2026 &middot; Subject to Client &amp; Legal Review
          </div>
        </header>

        <div class="article-body">
          <p>
            At <strong>9th Chakra Psychic</strong>, your personal privacy, discretion, and trust are fundamental to our practice. This Privacy Policy outlines how information provided by visitors and clients through this website is handled.
          </p>

          <h2>1. Information Collected Through the Website</h2>
          <p>
            We collect personal information solely when you voluntarily provide it to us, such as when you reach out by telephone or initiate an inquiry through our contact form. This information may include:
          </p>
          <ul>
            <li>Your full name</li>
            <li>Your email address</li>
            <li>Your contact telephone number</li>
            <li>The service or modality of interest</li>
            <li>Any contextual notes or questions you choose to share</li>
          </ul>

          <h2>2. How Submitted Information Is Used</h2>
          <p>
            Any information submitted is used exclusively for the purpose of responding to your inquiry, coordinating session scheduling, and conducting your private spiritual consultation. We do not sell, rent, lease, or trade personal client information to any third parties or marketing brokers under any circumstances.
          </p>

          <h2>3. Discretion and Consultation Confidentiality</h2>
          <p>
            In keeping with our more than 30 years of private spiritual counsel, the topics, questions, and personal details discussed during your spiritual reading or energy session remain strictly private between you and the practitioner.
          </p>

          <h2>4. Data Retention</h2>
          <p>
            Contact inquiry details are retained only as long as necessary to facilitate your consultation and fulfill reasonable communication requests, after which they may be securely deleted or archived.
          </p>

          <h2>5. Cookies and Technical Data</h2>
          <p>
            This website is designed for privacy and does not employ intrusive third-party behavioral advertising trackers. Standard, non-identifying server logs (such as page requests, browser types, and access timestamps) may be generated automatically by web hosting infrastructure to ensure site security and proper technical operation.
          </p>

          <h2>6. Third-Party Service Links</h2>
          <p>
            Our website may contain links to external resources or telephone protocols. We are not responsible for the privacy practices of external websites. We encourage you to review the policies of any third-party websites you visit.
          </p>

          <h2>7. Contact Information for Privacy Inquiries</h2>
          <p>
            If you have questions regarding this Privacy Policy or wish to request the removal of your inquiry details, please contact us directly by telephone at <strong>+1 (214) 899-8311</strong>.
          </p>
        </div>
      </div>
    </section>
    """

def render_disclaimer(rel=""):
    return f"""
    <section class="section" style="padding-top:clamp(50px, 7vw, 84px);" aria-labelledby="disclaimerHeading">
      <div class="container container-narrow">

        <header class="article-header text-left" style="margin-bottom:36px; padding:0;">
          <div class="eyebrow">Professional Notice</div>
          <h1 id="disclaimerHeading">Spiritual Services Disclaimer</h1>
          <div style="font-size:0.88rem; color:var(--text-muted); margin-top:8px;">
            Please Read Before Scheduling a Consultation
          </div>
        </header>

        <div class="article-body">
          <div class="notice-box">
            <h4>Important Notice of Purpose</h4>
            <p>
              The services provided by 9th Chakra Psychic—including tarot readings, psychic readings, medium readings, Reiki, Seichim energy healing, chakra balancing, aura cleansing, holistic guidance, and meditation—are spiritual, intuitive, and educational practices intended for personal reflection and well-being.
            </p>
          </div>

          <h2>1. Subjective Nature of Intuitive Guidance</h2>
          <p>
            All intuitive readings, symbolic card interpretations, and energetic impressions provided during consultations are inherently subjective and personal. They reflect intuitive perspectives and patterns at the time of the session. No reading or spiritual service guarantees a specific outcome, fixed event, or predetermined future.
          </p>

          <h2>2. Not a Substitute for Professional Medical or Mental Health Care</h2>
          <p>
            Spiritual services, energy healing modalities (Reiki, Seichim), and chakra balancing are not medical treatments, do not diagnose conditions, and do not cure illnesses or psychiatric disorders. They are complementary wellness practices intended for somatic relaxation and spiritual balance. If you are experiencing physical illness, medical symptoms, or a mental health crisis, please consult a licensed physician, clinical psychologist, or medical healthcare provider immediately.
          </p>

          <h2>3. Not a Substitute for Legal, Financial, or Business Counsel</h2>
          <p>
            Insights shared during sessions regarding professional paths, business decisions, or personal finances are offered strictly as intuitive and spiritual perspectives. They do not constitute certified financial, accounting, investment, or legal advice. You must consult certified professionals (attorneys, CPAs, licensed advisors) for formal legal and financial determinations.
          </p>

          <h2>4. Personal Agency, Sovereignty, and Free Will</h2>
          <p>
            At 9th Chakra Psychic, we firmly uphold the universal principle of individual free will. You retain full personal autonomy and responsibility for all choices, interpretations, and actions you take following a consultation. Our guidance is designed to inspire clarity and self-reliance, never to replace your own sovereign judgment.
          </p>

          <h2>5. Age of Majority</h2>
          <p>
            All private readings and spiritual services are intended for adults aged 18 and older, or minors accompanied by a consenting parent or legal guardian.
          </p>

          <h2>6. Questions Regarding Our Disclaimer</h2>
          <p>
            If you have questions about the scope of our services or would like to discuss whether a spiritual consultation is appropriate for your current situation, please contact us directly at <strong>+1 (214) 899-8311</strong>.
          </p>
        </div>
      </div>
    </section>
    """
