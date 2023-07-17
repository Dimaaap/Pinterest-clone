import { photoGroups } from "./photoGroups.js";

window.addEventListener("DOMContentLoaded", function(){
    const firstPhrase = document.getElementById("first-title");
    const indicators = document.querySelectorAll(".carousel-indicator");
    const firstIndicator = document.getElementById("first-point");
    const carouselGroups = document.querySelectorAll(".carousel-group");
    const carouselPhotos = document.querySelector(".carousel-photos");

    let phrases = document.getElementsByClassName("carousel-title");
    let currentIndex = 0;
    let intervalId;

    firstPhrase.classList.add("show");
    firstIndicator.classList.add("active");

    function updateCarousel(){
        //Проходимось кожною фразою,яка є елементом каруселі
        for(let i = 0; i < phrases.length; i++){
            phrases[i].classList.remove("show");
            indicators[i].classList.remove("active");
        }
        phrases[currentIndex].classList.add("show");
        indicators[currentIndex].classList.add("active");
        const currentGroup = photoGroups[currentIndex];
        carouselPhotos.innerHTML = "";
        currentGroup.forEach(function(photoSrc, index){
            const img = document.createElement("img");
            img.src = photoSrc;
            img.classList.add("section-img");
            if(index === 1 || index === 2){
                img.classList.add("lower");
            }
            if(index === 2){
                img.classList.add("left-section")
            }
            carouselPhotos.appendChild(img);
        })
        const photos = document.querySelectorAll(".section-img");

        const currentTextColor = window.getComputedStyle(phrases[currentIndex]).color;
    }

    function autoRotateCarousel() {
        currentIndex = (currentIndex + 1) % phrases.length;
        updateCarousel();
    }

    //Кожні 5 секунд оновлювати карусель
    function startAutoRotateCarousel(){
        intervalId = setInterval(function(){
            autoRotateCarousel();
            updateCarousel();
        }, 5000);
    }

    //Прохід кожним елементом у списку індикаторів
    indicators.forEach(function(indicator) { // функція у циклі forEach приймає індикатор іх списку indicators
        indicator.addEventListener('click', function(){ // при натисканні на кружечок-індикатор переключається карусель
            currentIndex = parseInt(indicator.getAttribute("data-index"));
            updateCarousel();
        });
    });

    setInterval(autoRotateCarousel, 5000);
})

