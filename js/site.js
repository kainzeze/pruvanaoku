(function () {
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.querySelector(".menu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  var safety = document.querySelector(".safety");
  if (safety) {
    var safetyBtn = safety.querySelector(".safety-btn");
    safetyBtn.addEventListener("click", function (event) {
      event.stopPropagation();
      var open = safety.classList.toggle("open");
      safetyBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("click", function (event) {
      if (!safety.contains(event.target)) {
        safety.classList.remove("open");
        safetyBtn.setAttribute("aria-expanded", "false");
      }
    });
    document.addEventListener("keydown", function (event) {
      if (event.key !== "Escape") return;
      safety.classList.remove("open");
      safetyBtn.setAttribute("aria-expanded", "false");
    });
  }

  var slides = Array.prototype.slice.call(document.querySelectorAll(".quote"));
  if (slides.length) {
    var index = 0;
    var timer = null;
    function show(next) {
      index = (next + slides.length) % slides.length;
      slides.forEach(function (slide, i) {
        slide.classList.toggle("active", i === index);
      });
    }
    function play() {
      stop();
      timer = setInterval(function () { show(index + 1); }, 7000);
    }
    function stop() {
      if (timer) clearInterval(timer);
    }
    var root = document.querySelector(".quotes");
    root.addEventListener("mouseenter", stop);
    root.addEventListener("mouseleave", play);
    root.querySelector(".prev").addEventListener("click", function () { show(index - 1); });
    root.querySelector(".next").addEventListener("click", function () { show(index + 1); });
    show(0);
    play();
  }

  var box = document.querySelector(".lightbox");
  if (!box) return;
  var items = Array.prototype.slice.call(document.querySelectorAll(".gallery img"));
  var view = box.querySelector("img");
  var current = 0;
  function openAt(i) {
    current = i;
    view.src = items[i].dataset.full || items[i].src;
    view.alt = items[i].alt || "Okul görseli";
    box.classList.add("open");
  }
  items.forEach(function (img, i) {
    img.parentElement.addEventListener("click", function () { openAt(i); });
  });
  box.querySelector(".close").addEventListener("click", function () { box.classList.remove("open"); });
  box.querySelector(".prev").addEventListener("click", function () { openAt((current - 1 + items.length) % items.length); });
  box.querySelector(".next").addEventListener("click", function () { openAt((current + 1) % items.length); });
  box.addEventListener("click", function (event) {
    if (event.target === box) box.classList.remove("open");
  });
  document.addEventListener("keydown", function (event) {
    if (!box.classList.contains("open")) return;
    if (event.key === "Escape") box.classList.remove("open");
    if (event.key === "ArrowRight") openAt((current + 1) % items.length);
    if (event.key === "ArrowLeft") openAt((current - 1 + items.length) % items.length);
  });
})();
