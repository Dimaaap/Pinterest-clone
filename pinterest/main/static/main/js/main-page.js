window.addEventListener("DOMContentLoaded", function(){
    let phrases = document.getElementsByClassName("carousel-title");
    const firstPhrase = document.getElementById("first-title");
    firstPhrase.classList.add("show");
    const indicators = document.querySelectorAll(".carousel-indicator");

    let currentIndex = 0;
    let intervalId;

    function updateCarousel(){
        for(let i = 0; i < phrases.length; i++){
            phrases[i].classList.remove("show");
        }
        phrases[currentIndex].classList.add("show");
    }

    function autoRotateCarousel() {
        currentIndex = (currentIndex + 1) % phrases.length;
        updateCarousel();
    }

    indicators.forEach(function(indicator) {
        indicator.addEventListener('click', function(){
            currentIndex = parseInt(indicator.getAttribute("data-index"));
            updateCarousel();
        });
    });

    setInterval(autoRotateCarousel, 5000);
})