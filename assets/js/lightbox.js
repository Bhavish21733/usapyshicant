/**
 * 9th Chakra Psychic — Gallery & Lightbox Functionality
 * Category filter tabs, full-screen accessible modal, keyboard navigation
 */

document.addEventListener('DOMContentLoaded', () => {
  initGallery();
});

function initGallery() {
  const tabs = document.querySelectorAll('.gallery-tab');
  const items = document.querySelectorAll('.gallery-item');
  const modal = document.querySelector('#lightboxModal');

  if (!items.length) return;

  // Category Filtering
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const category = tab.dataset.category || 'all';

      items.forEach(item => {
        if (category === 'all' || item.dataset.category.includes(category)) {
          item.style.display = '';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });

  // Lightbox Implementation
  if (!modal) return;

  const modalImg = modal.querySelector('.lightbox-img');
  const modalTitle = modal.querySelector('.lightbox-title');
  const modalCounter = modal.querySelector('.lightbox-counter');
  const prevBtn = modal.querySelector('.lightbox-btn-prev');
  const nextBtn = modal.querySelector('.lightbox-btn-next');
  const closeBtn = modal.querySelector('.lightbox-btn-close');

  let currentIndex = 0;
  let activeItems = [];

  const updateActiveItems = () => {
    activeItems = Array.from(items).filter(item => item.style.display !== 'none');
  };

  const showItem = (index) => {
    updateActiveItems();
    if (!activeItems.length) return;

    if (index < 0) index = activeItems.length - 1;
    if (index >= activeItems.length) index = 0;
    currentIndex = index;

    const currentItem = activeItems[currentIndex];
    const img = currentItem.querySelector('img');
    const title = currentItem.dataset.title || (img ? img.alt : '');

    if (modalImg && img) {
      modalImg.src = img.src;
      modalImg.alt = title;
    }
    if (modalTitle) {
      modalTitle.textContent = title;
    }
    if (modalCounter) {
      modalCounter.textContent = (currentIndex + 1) + ' of ' + activeItems.length;
    }
  };

  const openLightbox = (item) => {
    updateActiveItems();
    currentIndex = activeItems.indexOf(item);
    if (currentIndex === -1) currentIndex = 0;
    showItem(currentIndex);

    modal.classList.add('open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    if (closeBtn) closeBtn.focus();
  };

  const closeLightbox = () => {
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  };

  items.forEach(item => {
    item.addEventListener('click', () => openLightbox(item));
    item.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openLightbox(item);
      }
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  if (prevBtn) prevBtn.addEventListener('click', () => showItem(currentIndex - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => showItem(currentIndex + 1));

  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target.classList.contains('lightbox-backdrop')) {
      closeLightbox();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('open')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') showItem(currentIndex - 1);
    if (e.key === 'ArrowRight') showItem(currentIndex + 1);
  });
}
