/* arxiv-header.js — behavior for the shared spinout chrome (.ds-site-header /
 * .ds-announcement / .ds-site-footer). Vanilla JS, no jQuery.
 *
 * Responsibilities:
 *  (a) Open/close the header search overlay (progressive enhancement of the
 *      Search <a href="/search"> — without JS it just navigates to search).
 *  (b) Collapse the nav behind the phone hamburger. Per the design-system
 *      contract this script ADDS `.is-collapsible` to .ds-site-header, so the
 *      hamburger appears only when JS is actually running (no-JS falls back to
 *      the WCAG-reflow wrapped nav).
 *  (c) Persist announcement-banner dismissal (localStorage, keyed by
 *      data-banner-name).
 *  (d) Fill the inline member-institution acknowledgement (.ack-member-inline)
 *      from the IP-keyed /institutional_banner endpoint.
 *
 * Replaces the prior member_acknowledgement.js, which targeted the legacy
 * #support-ack-url element from the Cornell-era footer.
 */

(function () {
  "use strict";

  /* ----- Search overlay ----- */
  const toggle = document.getElementById("arxiv-search-toggle"); // the Search <a>
  const overlay = document.getElementById("arxiv-search-overlay");
  const input = document.getElementById("arxiv-search-input");

  function openOverlay() {
    if (!overlay) return;
    overlay.removeAttribute("hidden");
    overlay.classList.add("is-open");
    if (toggle) toggle.setAttribute("aria-expanded", "true");
    if (input) setTimeout(function () { input.focus(); }, 50);
  }

  function closeOverlay() {
    if (!overlay) return;
    overlay.classList.remove("is-open");
    overlay.setAttribute("hidden", "");
    if (toggle) {
      toggle.setAttribute("aria-expanded", "false");
      toggle.focus();
    }
  }

  // Search is a real <a href="/search">: without JS it navigates to the search
  // page; with JS we intercept the click and open the in-page overlay instead.
  if (toggle && overlay) {
    toggle.addEventListener("click", function (e) {
      e.preventDefault();
      openOverlay();
    });
    overlay.addEventListener("click", function (e) {
      if (e.target === overlay) closeOverlay();
    });
  }

  /* ----- Hamburger nav (phone breakpoint) -----
   * The design-system CSS hides the hamburger until .ds-site-header carries
   * .is-collapsible. We add it here so the hamburger only ever shows when this
   * script ran (and therefore the toggle works). */
  const navToggle = document.getElementById("ds-nav-toggle");
  const nav = document.getElementById("ds-site-header-nav");
  const header = document.querySelector(".ds-site-header");

  function setNavOpen(open) {
    if (!nav || !navToggle) return;
    nav.classList.toggle("is-open", open);
    navToggle.setAttribute("aria-expanded", open ? "true" : "false");
    navToggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  }

  if (navToggle && nav && header) {
    header.classList.add("is-collapsible");
    navToggle.addEventListener("click", function (e) {
      e.stopPropagation();
      setNavOpen(!nav.classList.contains("is-open"));
    });
    document.addEventListener("click", function (e) {
      if (!nav.classList.contains("is-open")) return;
      if (nav.contains(e.target) || navToggle.contains(e.target)) return;
      setNavOpen(false);
    });
  }

  /* ----- Shared keyboard handling ----- */
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      if (overlay && overlay.classList.contains("is-open")) {
        closeOverlay();
      } else if (nav && nav.classList.contains("is-open")) {
        setNavOpen(false);
        if (navToggle) navToggle.focus();
      }
    } else if ((e.metaKey || e.ctrlKey) && e.key === "k") {
      e.preventDefault();
      openOverlay();
    }
  });

  /* ----- Announcement banner: stay-closed-when-closed -----
   * Dismissal is remembered in localStorage keyed by the banner's
   * data-banner-name; the server controls when the banner runs, so a new
   * announcement (new name) shows again. */
  const banner = document.getElementById("announcement-banner");
  if (banner) {
    const dismissKey = "arxiv-banner-dismissed:" + (banner.dataset.bannerName || "announcement");
    if (localStorage.getItem(dismissKey)) {
      banner.classList.add("is-dismissed");
    } else {
      const closeBtn = banner.querySelector(".ds-announcement-close");
      if (closeBtn) {
        closeBtn.addEventListener("click", function () {
          banner.classList.add("is-dismissed");
          try { localStorage.setItem(dismissKey, "1"); } catch (e) {}
        });
      }
    }
  }

  /* ----- Institutional ack ----- */
  const MEMBER_TTL_MS = 30 * 24 * 60 * 60 * 1000;
  const FAIL_TTL_MS = 60 * 60 * 1000;

  async function fetchInstitutionLabel() {
    let label = localStorage.getItem("member_label");
    const expiresStr = localStorage.getItem("member_expires");
    const now = new Date();
    let expired = true;
    if (expiresStr) {
      const expires = new Date(expiresStr);
      if (!isNaN(expires.getTime()) && now < expires) expired = false;
    }

    if (!expired) return label;

    localStorage.removeItem("member_label");
    localStorage.removeItem("member_expires");

    let ttl = MEMBER_TTL_MS;
    try {
      const result = await fetch("/institutional_banner");
      if (result && result.ok) {
        const j = await result.json();
        if (j && j.label) {
          label = j.label;
          localStorage.setItem("member_label", label);
        } else {
          label = null;
        }
      } else {
        ttl = FAIL_TTL_MS;
        label = null;
      }
    } catch (e) {
      ttl = FAIL_TTL_MS;
      label = null;
    }

    const newExpires = new Date(now.getTime() + ttl);
    localStorage.setItem("member_expires", newExpires.toISOString());
    return label;
  }

  function renderMemberLabel(label) {
    if (!label) return;
    const wrap = document.querySelector(".ack-member-inline");
    if (!wrap) return;
    const strong = wrap.querySelector("strong");
    if (strong) strong.textContent = label;
    wrap.hidden = false;
  }

  fetchInstitutionLabel().then(renderMemberLabel);
})();
