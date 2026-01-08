gsap.registerPlugin(ScrollTrigger);

/* ---------------------------
   ACCESSIBILITY
---------------------------- */
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------------------------
   SCROLL PROGRESS BAR
---------------------------- */
if (!reduceMotion) {
  gsap.to(".progress-bar", {
    width: "100%",
    scrollTrigger: {
      scrub: 0.3
    }
  });
}

/* ---------------------------
   TEXT REVEAL ANIMATION
---------------------------- */
if (!reduceMotion) {
  gsap.from(".reveal-text", {
    yPercent: 100,
    opacity: 0,
    duration: 1,
    stagger: 0.3,
    ease: "power4.out"
  });
}

/* ---------------------------
   PARALLAX EFFECT
---------------------------- */
if (!reduceMotion) {
  gsap.to(".layer-back", {
    y: -100,
    scrollTrigger: {
      trigger: ".parallax",
      scrub: true
    }
  });

  gsap.to(".layer-mid", {
    y: -200,
    scrollTrigger: {
      trigger: ".parallax",
      scrub: true
    }
  });

  gsap.to(".layer-front", {
    y: -300,
    scrollTrigger: {
      trigger: ".parallax",
      scrub: true
    }
  });
}

/* ---------------------------
   MOUSE MOVE INTERACTION
---------------------------- */
const box = document.querySelector(".cursor-box");

document.addEventListener("mousemove", (e) => {
  gsap.to(box, {
    x: e.clientX / 15,
    y: e.clientY / 15,
    duration: 0.3,
    ease: "power3.out"
  });
});
