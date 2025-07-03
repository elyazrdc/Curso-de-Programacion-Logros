const scrollReveal = {
    distance:"50px",
    origin: "bottom",
    duration: 1000,
};

ScrollReveal().reveal(".section__container h3", {
    ...scrollReveal,
});

ScrollReveal().reveal(".section__container h1", {
    ...scrollReveal,
    origin: "left",
    delay: 500,
});

ScrollReveal().reveal(".section__container h2", {
    ...scrollReveal,
    origin: "right",
    delay: 1000,
});

ScrollReveal().reveal(".section__container button", {
    ...scrollReveal,
    origin: "right",
    delay: 1500,
});

ScrollReveal().reveal(".nav__links li", {
    ...scrollReveal,
    origin: "top",
    interval: 300,
    delay: 1000,
});

ScrollReveal().reveal(".socials a", {
    duration: 1000,
    interval: 500,
    delay: 4000,
})