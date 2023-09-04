const accordions = document.querySelectorAll(".accordion-wrapper .accordion");

accordions.forEach((acc) => {
    acc.onClick = () => {
        acc.classList.add("active");
    }
})
