document.addEventListener("DOMContentLoaded", () => {

    /* ── Появление карточек ── */
    const cards = document.querySelectorAll(".card");
    const io = new IntersectionObserver((entries) => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                e.target.classList.add("card--visible");
                io.unobserve(e.target);
            }
        });
    }, { threshold: 0.12 });

    cards.forEach((c, i) => {
        c.style.opacity = "0";
        c.style.transform = "translateY(28px)";
        c.style.transition =
            `opacity .55s ${i * 55}ms cubic-bezier(.22,1,.36,1),
             transform .55s ${i * 55}ms cubic-bezier(.22,1,.36,1),
             box-shadow .3s, border-color .3s, background .3s`;
        io.observe(c);
    });

    // Класс для видимости
    const style = document.createElement("style");
    style.textContent =
        `.card--visible{opacity:1!important;transform:translateY(0)!important;}`;

    document.head.appendChild(style);

    /* ── Parallax на hero (лёгкий) ── */
    const hero = document.querySelector(".hero");
    if (hero) {
        window.addEventListener("scroll", () => {
            const y = window.scrollY;
            hero.style.backgroundPositionY = `${y * 0.25}px`;
        }, { passive: true });
    }

    /* ── Filters (заглушка) ── */
    document.querySelectorAll(".filter").forEach(sel => {
        sel.addEventListener("change", () => {
            // TODO: fetch(`/filter?genre=${sel.value}`)
        });
    });
});