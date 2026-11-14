/**
 * 9th Chakra Psychic — Main Interactive Scripts
 * Accessible navigation, sticky header, FAQ accordions, form handling
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileNavigation();
  initAccordions();
  initContactForm();
  initServiceFilter();
  initServicesAutoScroll();
});

/**
 * Service Category Filter
 */
function initServiceFilter() {
  const filterBtns = document.querySelectorAll('.service-filter-btn');
  const serviceCards = document.querySelectorAll('.service-luxury-card');

  if (!filterBtns.length || !serviceCards.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterCategory = btn.dataset.filter || 'all';

      serviceCards.forEach(card => {
        const categories = (card.dataset.category || '').split(' ');
        if (filterCategory === 'all' || categories.includes(filterCategory)) {
          card.style.display = 'flex';
          card.style.animation = 'fadeIn 0.3s ease forwards';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/**
 * Sticky Header on Scroll
 */
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 24) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/**
 * Accessible Mobile Navigation Drawer
 */
function initMobileNavigation() {
  const toggleBtn = document.querySelector('.menu-toggle');
  const closeBtn = document.querySelector('.mobile-close-btn');
  const drawer = document.querySelector('.mobile-nav-drawer');
  const overlay = document.querySelector('.mobile-nav-overlay');
  const servicesTrigger = document.querySelector('.mobile-services-trigger');
  const servicesAccordion = document.querySelector('.mobile-services-accordion');

  if (!toggleBtn || !drawer || !overlay) return;

  const openDrawer = () => {
    drawer.classList.add('open');
    overlay.classList.add('open');
    toggleBtn.setAttribute('aria-expanded', 'true');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    if (closeBtn) closeBtn.focus();
  };

  const closeDrawer = () => {
    drawer.classList.remove('open');
    overlay.classList.remove('open');
    toggleBtn.setAttribute('aria-expanded', 'false');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    toggleBtn.focus();
  };

  toggleBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  overlay.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });

  // Services submenu accordion inside mobile drawer
  if (servicesTrigger && servicesAccordion) {
    servicesTrigger.addEventListener('click', (e) => {
      e.preventDefault();
      const isOpen = servicesAccordion.classList.contains('open');
      servicesAccordion.classList.toggle('open');
      servicesTrigger.setAttribute('aria-expanded', String(!isOpen));
      const icon = servicesTrigger.querySelector('svg');
      if (icon) {
        icon.style.transform = isOpen ? 'rotate(0deg)' : 'rotate(180deg)';
      }
    });
  }
}

/**
 * Accessible FAQ Accordion
 */
function initAccordions() {
  const accordionHeaders = document.querySelectorAll('.accordion-header');

  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.closest('.accordion-item');
      if (!item) return;

      const isOpen = item.classList.contains('active');

      const parentAccordion = item.closest('.accordion');
      if (parentAccordion) {
        parentAccordion.querySelectorAll('.accordion-item').forEach(sibling => {
          if (sibling !== item) {
            sibling.classList.remove('active');
            const siblingBtn = sibling.querySelector('.accordion-header');
            if (siblingBtn) siblingBtn.setAttribute('aria-expanded', 'false');
          }
        });
      }

      item.classList.toggle('active');
      header.setAttribute('aria-expanded', String(!isOpen));
    });
  });
}

/**
 * Contact Inquiry Form Validation & Submission Handling
 */
function initContactForm() {
  const form = document.querySelector('#contactForm');
  if (!form) return;

  const nameInput = form.querySelector('#fullName');
  const emailInput = form.querySelector('#emailAddress');
  const serviceInput = form.querySelector('#serviceInterest');
  const messageInput = form.querySelector('#message');
  const consentInput = form.querySelector('#privacyConsent');
  const statusAlert = form.querySelector('#formStatusAlert');

  const validateEmail = (email) => {
    return /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email);
  };

  const setFieldError = (input, isValid, message) => {
    if (!input) return;
    const parent = input.closest('.form-group');
    if (!parent) return;
    let errorElem = parent.querySelector('.form-error-msg');
    if (!errorElem) {
      errorElem = document.createElement('div');
      errorElem.className = 'form-error-msg';
      parent.appendChild(errorElem);
    }

    if (isValid) {
      input.classList.remove('has-error');
      errorElem.style.display = 'none';
      errorElem.textContent = '';
    } else {
      input.classList.add('has-error');
      errorElem.style.display = 'block';
      errorElem.textContent = message;
    }
  };

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    let hasErrors = false;

    // Validate Name
    if (!nameInput.value.trim()) {
      setFieldError(nameInput, false, 'Please enter your full name.');
      hasErrors = true;
    } else {
      setFieldError(nameInput, true);
    }

    // Validate Email
    if (!emailInput.value.trim()) {
      setFieldError(emailInput, false, 'Please enter your email address.');
      hasErrors = true;
    } else if (!validateEmail(emailInput.value.trim())) {
      setFieldError(emailInput, false, 'Please enter a valid email address.');
      hasErrors = true;
    } else {
      setFieldError(emailInput, true);
    }

    // Validate Message
    if (!messageInput.value.trim()) {
      setFieldError(messageInput, false, 'Please share a brief note about what you are seeking.');
      hasErrors = true;
    } else {
      setFieldError(messageInput, true);
    }

    // Validate Consent
    if (consentInput && !consentInput.checked) {
      setFieldError(consentInput, false, 'Please confirm your consent to be contacted.');
      hasErrors = true;
    } else if (consentInput) {
      setFieldError(consentInput, true);
    }

    if (hasErrors) {
      if (statusAlert) {
        statusAlert.className = 'form-status-alert error';
        statusAlert.textContent = 'Please correct the highlighted fields above.';
        statusAlert.style.display = 'block';
      }
      return;
    }

    if (statusAlert) {
      statusAlert.className = 'form-status-alert success';
      statusAlert.innerHTML = '<strong>Inquiry Details Prepared:</strong> Thank you, ' + nameInput.value.trim() + '. For prompt scheduling and private counsel, please call directly at <a href=\"tel:+12148998311\" style=\"color:#10B981; text-decoration:underline; font-weight:700;\">+1 (214) 899-8311</a>.';
      statusAlert.style.display = 'block';
      form.reset();
    }
  });

  [nameInput, emailInput, messageInput].forEach(inp => {
    if (inp) {
      inp.addEventListener('input', () => {
        if (inp.value.trim()) setFieldError(inp, true);
      });
    }
  });
}

/**
 * Mobile Homepage Services 1-Card Auto-Scroll
 */
function initServicesAutoScroll() {
  const track = document.querySelector('.services-slider-track');
  if (!track) return;

  const cards = track.querySelectorAll('.service-card');
  if (cards.length <= 1) return;

  let currentIndex = 0;
  let isInteracting = false;
  let resumeTimeout = null;

  const getCardWidth = () => {
    return cards[0].offsetWidth + 16; // card width + gap
  };

  const advanceScroll = () => {
    // Only auto-scroll when in mobile/horizontal slider view (< 768px)
    if (window.innerWidth <= 768 && !isInteracting) {
      currentIndex = (currentIndex + 1) % cards.length;
      track.scrollTo({
        left: currentIndex * getCardWidth(),
        behavior: 'smooth'
      });
    }
  };

  let scrollInterval = setInterval(advanceScroll, 3800);

  // Pause when user touches or scrolls manually, then resume gracefully
  const pauseAutoScroll = () => {
    isInteracting = true;
    if (resumeTimeout) clearTimeout(resumeTimeout);
  };

  const resumeAutoScroll = () => {
    resumeTimeout = setTimeout(() => {
      const cardWidth = getCardWidth();
      if (cardWidth > 0) {
        currentIndex = Math.round(track.scrollLeft / cardWidth) % cards.length;
      }
      isInteracting = false;
    }, 2000);
  };

  track.addEventListener('touchstart', pauseAutoScroll, { passive: true });
  track.addEventListener('touchend', resumeAutoScroll, { passive: true });
  track.addEventListener('mousedown', pauseAutoScroll);
  track.addEventListener('mouseup', resumeAutoScroll);
  track.addEventListener('mouseenter', pauseAutoScroll);
  track.addEventListener('mouseleave', resumeAutoScroll);

  window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
      track.scrollTo({ left: 0, behavior: 'auto' });
      currentIndex = 0;
    }
  });
}
