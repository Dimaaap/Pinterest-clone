const button = document.querySelector(".link-btn");

window.addEventListener("DOMContentLoaded", function(){
    let phrases = document.getElementsByClassName("carousel-title");
    const firstPhrase = document.getElementById("first-title");
    firstPhrase.classList.add("show");
    const indicators = document.querySelectorAll(".carousel-indicator");
    const firstIndicator = document.getElementById("first-point");
    firstIndicator.classList.add("active");

    let currentIndex = 0;
    let intervalId;

    //Функція, яка проходиться кожною фразою і кожним значком у списку фраз і значків і спочатку приховує все,а потім
    //ітеративно відкриває наступний елемент у списку
    function updateCarousel(){
        for(let i = 0; i < phrases.length; i++){
            phrases[i].classList.remove("show");
            indicators[i].classList.remove("active");
        }
        phrases[currentIndex].classList.add("show");
        indicators[currentIndex].classList.add("active");

        const currentTextColor = window.getComputedStyle(phrases[currentIndex]).color;
        button.style.backgroundColor = currentTextColor;
    }

    function autoRotateCarousel() {
        currentIndex = (currentIndex + 1) % phrases.length;
        updateCarousel();
    }

    function startAutoRotateCarousel(){
        intervalId = setInterval(function(){
            autoRotateCarousel();
            updateCarousel();
        }, 5000);
    }

    indicators.forEach(function(indicator) {
        indicator.addEventListener('click', function(){
            currentIndex = parseInt(indicator.getAttribute("data-index"));
            updateCarousel();
        });
    });

    setInterval(autoRotateCarousel, 5000);
    function jumpButton(){
    button.style.transform = "translateY(-20px)";
    button.addEventListener("transitionend", function() {
    button.style.transform = "translateY(0)";
    setTimeout(jumpButton, 500);
  }, { once: true });
}

jumpButton();

})
