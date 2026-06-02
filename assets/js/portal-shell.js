/**
 * MAGNE.AI Portal Shell JavaScript
 * Multilingual Unified Shell - Vanilla JS
 * No external dependencies
 */

(function() {
  'use strict';

  // ── Mobile Menu Toggle ──
  const mobileToggle = document.getElementById('psMobileToggle');
  const mobileMenu = document.getElementById('psMobileMenu');

  if (mobileToggle && mobileMenu) {
    mobileToggle.addEventListener('click', function() {
      const isOpen = mobileMenu.classList.contains('open');
      mobileMenu.classList.toggle('open');
      mobileToggle.setAttribute('aria-expanded', String(!isOpen));
      document.body.classList.toggle('ps-menu-open', !isOpen);
    });

    // Close on link click
    mobileMenu.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        mobileMenu.classList.remove('open');
        mobileToggle.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('ps-menu-open');
      });
    });
  }

  // ── Language Dropdown ──
  const langBtn = document.getElementById('psLangBtn');
  const langDropdown = document.getElementById('psLangDropdown');

  if (langBtn && langDropdown) {
    langBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      const isOpen = langDropdown.classList.contains('open');
      langDropdown.classList.toggle('open');
      langBtn.setAttribute('aria-expanded', String(!isOpen));
    });

    // Close on option click
    langDropdown.querySelectorAll('.portal-shell-language-option:not(.disabled)').forEach(function(option) {
      option.addEventListener('click', function(e) {
        e.stopPropagation();
        const selectedLang = this.dataset.lang;
        const selectedUrl = this.dataset.url;

        if (selectedUrl) {
          window.location.href = selectedUrl;
        }

        langDropdown.classList.remove('open');
        langBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // ── Escape Key Handler ──
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      // Close mobile menu
      if (mobileMenu && mobileMenu.classList.contains('open')) {
        mobileMenu.classList.remove('open');
        if (mobileToggle) mobileToggle.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('ps-menu-open');
      }

      // Close language dropdown
      if (langDropdown && langDropdown.classList.contains('open')) {
        langDropdown.classList.remove('open');
        if (langBtn) langBtn.setAttribute('aria-expanded', 'false');
      }
    }
  });

  // ── Click Outside Handler ──
  document.addEventListener('click', function(e) {
    // Close language dropdown on outside click
    if (langDropdown && langDropdown.classList.contains('open')) {
      if (!langDropdown.contains(e.target) && e.target !== langBtn) {
        langDropdown.classList.remove('open');
        if (langBtn) langBtn.setAttribute('aria-expanded', 'false');
      }
    }
  });

  // ── Body scroll lock for mobile menu ──
  if (mobileMenu) {
    const style = document.createElement('style');
    style.textContent = 'body.ps-menu-open { overflow: hidden; }';
    document.head.appendChild(style);
  }

})();
