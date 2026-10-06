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

  /* Notenrechner: drei Noten, jede einzeln aus ihren Punkten */
  var form = document.getElementById("rechner");
  if (form) {
    var MAX = { dribbeln: 10, werfen: 10, spiel: 12 };
    /* Schluessel aus Fabis Standard: ab 90/80/60/40/20 Prozent gleich Note 1 bis 5 */
    function noteFor(points, max) {
      var p = Math.round(points / max * 1e6) / 1e6;
      if (p >= 0.9) return 1;
      if (p >= 0.8) return 2;
      if (p >= 0.6) return 3;
      if (p >= 0.4) return 4;
      if (p >= 0.2) return 5;
      return 6;
    }
    function update() {
      Object.keys(MAX).forEach(function (k) {
        var input = form.elements[k];
        var err = document.getElementById("e-" + k);
        var note = document.getElementById("r-" + k);
        var info = document.getElementById("p-" + k);
        var raw = input.value.trim();
        err.textContent = "";
        input.removeAttribute("aria-invalid");
        note.textContent = "-";
        info.textContent = "";
        if (raw === "") return;
        var v = Number(raw.replace(",", "."));
        if (isNaN(v) || v < 0 || v > MAX[k]) {
          err.textContent = "Bitte 0 bis " + MAX[k] + " eingeben.";
          input.setAttribute("aria-invalid", "true");
          return;
        }
        note.textContent = String(noteFor(v, MAX[k]));
        info.textContent = v + " von " + MAX[k] + " Punkten";
      });
    }
    form.addEventListener("input", update);
    form.addEventListener("submit", function (e) { e.preventDefault(); });
    update();
  }
})();
