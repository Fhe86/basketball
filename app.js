/* Basketball Klasse 6: Filter, Einblenden, Notenrechner. Kein Framework, keine externen Aufrufe. */
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  /* Einblenden beim Scrollen (nur wenn Bewegung erlaubt ist) */
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealEls = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(function (el, i) {
      el.style.setProperty("--d", (i % 4) * 60 + "ms");
      io.observe(el);
    });
  }

  /* Übungspool filtern */
  var chips = document.querySelectorAll(".chip[data-filter]");
  var cards = document.querySelectorAll(".card[data-stufe]");
  var empty = document.getElementById("pool-empty");
  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      chips.forEach(function (c) { c.setAttribute("aria-pressed", c === chip ? "true" : "false"); });
      var f = chip.getAttribute("data-filter");
      var shown = 0;
      cards.forEach(function (card) {
        var hit = f === "alle" || card.getAttribute("data-stufe").split(" ").indexOf(f) !== -1 ||
                  (f === "keller" && card.getAttribute("data-halle") === "beide");
        card.hidden = !hit;
        if (hit) shown++;
      });
      if (empty) empty.hidden = shown !== 0;
    });
  });

  /* Notenrechner */
  var form = document.getElementById("rechner");
  if (form) {
    var MAX = { dribbeln: 8, passen: 8, werfen: 8, spiel: 12 };
    var TOTAL = 36;
    var out = {
      note: document.getElementById("r-note"),
      sum: document.getElementById("r-sum"),
      pct: document.getElementById("r-pct")
    };
    /* Schluessel aus Fabis Standard: ab 90/80/60/40/20 Prozent gleich Note 1 bis 5 */
    function noteFor(points) {
      var p = points / TOTAL;
      if (p >= 0.9) return 1;
      if (p >= 0.8) return 2;
      if (p >= 0.6) return 3;
      if (p >= 0.4) return 4;
      if (p >= 0.2) return 5;
      return 6;
    }
    function update() {
      var sum = 0, filled = 0, bad = false;
      Object.keys(MAX).forEach(function (k) {
        var input = form.elements[k];
        var err = document.getElementById("e-" + k);
        var raw = input.value.trim();
        err.textContent = "";
        input.removeAttribute("aria-invalid");
        if (raw === "") return;
        var v = Number(raw.replace(",", "."));
        if (isNaN(v) || v < 0 || v > MAX[k]) {
          err.textContent = "Bitte 0 bis " + MAX[k] + " eingeben.";
          input.setAttribute("aria-invalid", "true");
          bad = true;
          return;
        }
        sum += v; filled++;
      });
      if (bad || filled === 0) {
        out.note.textContent = "-"; out.sum.textContent = "0 von " + TOTAL + " Punkten"; out.pct.textContent = "";
        return;
      }
      out.sum.textContent = sum + " von " + TOTAL + " Punkten";
      out.pct.textContent = Math.round(sum / TOTAL * 100) + " Prozent" + (filled < 4 ? " (noch nicht alle Teile eingetragen)" : "");
      out.note.textContent = filled < 4 ? "-" : String(noteFor(sum));
    }
    form.addEventListener("input", update);
    form.addEventListener("submit", function (e) { e.preventDefault(); });
    update();
  }
})();
