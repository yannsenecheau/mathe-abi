/* Mathe-Abi — Site-Verhalten: klappbare Abschnitte, TOC-Highlight, Mobil-Menü.
   Vanilla JS, keine externen Abhängigkeiten. */
(function () {
  "use strict";
  var KEY = "mathe-abi:collapsed:" + location.pathname;

  function loadState() {
    try { return JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) { return {}; }
  }
  function saveState(s) {
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) {}
  }

  var sections = Array.prototype.slice.call(document.querySelectorAll("main section.level2"));
  var state = loadState();

  // Klappbare Level-2-Abschnitte: Klick auf die Überschrift toggelt.
  sections.forEach(function (sec, i) {
    var h2 = sec.querySelector(":scope > h2");
    if (!h2) return;
    var id = sec.id || ("sec-" + i);
    sec.id = id;
    h2.setAttribute("role", "button");
    h2.setAttribute("tabindex", "0");
    if (state[id] === true) sec.classList.add("collapsed");
    function toggle() {
      sec.classList.toggle("collapsed");
      state[id] = sec.classList.contains("collapsed");
      saveState(state);
    }
    h2.addEventListener("click", toggle);
    h2.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(); }
    });
  });

  // Alles auf-/zuklappen
  function setAll(collapsed) {
    sections.forEach(function (sec) {
      sec.classList.toggle("collapsed", collapsed);
      if (sec.id) state[sec.id] = collapsed;
    });
    saveState(state);
  }
  var expandBtn = document.getElementById("expand-all");
  var collapseBtn = document.getElementById("collapse-all");
  if (expandBtn) expandBtn.addEventListener("click", function () { setAll(false); });
  if (collapseBtn) collapseBtn.addEventListener("click", function () { setAll(true); });

  // TOC-Highlight beim Scrollen
  var tocLinks = {};
  document.querySelectorAll(".toc a").forEach(function (a) {
    var href = a.getAttribute("href") || "";
    if (href.charAt(0) === "#") tocLinks[href.slice(1)] = a;
  });
  if (window.IntersectionObserver && sections.length) {
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          Object.keys(tocLinks).forEach(function (k) { tocLinks[k].classList.remove("active"); });
          var link = tocLinks[en.target.id];
          if (link) link.classList.add("active");
        }
      });
    }, { rootMargin: "-10% 0px -80% 0px", threshold: 0 });
    sections.forEach(function (s) { obs.observe(s); });
  }

  // Beim Klick auf einen TOC-Link den Zielabschnitt aufklappen
  document.querySelectorAll(".toc a").forEach(function (a) {
    a.addEventListener("click", function () {
      var href = a.getAttribute("href") || "";
      if (href.charAt(0) === "#") {
        var sec = document.getElementById(href.slice(1));
        if (sec) { sec.classList.remove("collapsed"); if (sec.id) { state[sec.id] = false; saveState(state); } }
      }
      document.body.classList.remove("nav-open");
    });
  });

  // Mobil-Menü
  var menuToggle = document.querySelector(".menu-toggle");
  var backdrop = document.querySelector(".backdrop");
  if (menuToggle) menuToggle.addEventListener("click", function () { document.body.classList.toggle("nav-open"); });
  if (backdrop) backdrop.addEventListener("click", function () { document.body.classList.remove("nav-open"); });
})();
