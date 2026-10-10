/*
  reveal timeline items as they enter the viewport.
*/

{
  const onLoad = () => {
    const items = document.querySelectorAll(".journey-stop");
    if (!items.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            entry.target.dataset.visible = "true";
            observer.unobserve(entry.target);
          }
        }
      },
      {
        threshold: 0.2,
        rootMargin: "0px 0px -10% 0px",
      }
    );

    for (const item of items) {
      observer.observe(item);
    }
  };

  window.addEventListener("load", onLoad);
}
