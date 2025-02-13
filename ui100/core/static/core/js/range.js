const sliders = document.querySelectorAll('.slider')

sliders.forEach((slider) => {
    slider.addEventListener('input', (e) => {
        const value = +e.target.value;
        const label = e.target.nextElementSibling;
        label.innerHTML = value;
    });
});