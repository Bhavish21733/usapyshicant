# pages/not_found.py
"""404 Not Found Page."""

def render_404(rel=""):
    return f"""
    <section class="section" style="padding-top:clamp(60px, 10vw, 120px); text-align:center;">
      <div class="container container-narrow">
        <div class="eyebrow">Error 404 &middot; Uncharted Path</div>
        <h1 style="font-size:clamp(2.5rem, 6vw, 4.5rem); margin-bottom:16px;">The Path Appears Unmarked.</h1>
        <p style="font-size:1.15rem; color:var(--champagne); max-width:600px; margin:0 auto 36px auto;">
          The page or reading you are seeking may have transitioned or moved. Let us guide you back toward clarity and centered stillness.
        </p>
        <div class="btn-group" style="justify-content:center;">
          <a href="{rel}index.html" class="btn btn-gold">Return to Homepage</a>
          <a href="{rel}services.html" class="btn btn-outline">Explore All Services</a>
        </div>
      </div>
    </section>
    """
