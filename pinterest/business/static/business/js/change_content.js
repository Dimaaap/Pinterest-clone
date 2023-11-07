const firstLabel = document.getElementById("first-label");
const secondLabel = document.getElementById("second-label");

const firstContainer = document.getElementById("first-choice");
const secondContainer = document.getElementById("second-choice");

const option1 = document.getElementById("option1");
const option2 = document.getElementById("option2");

document.addEventListener("DOMContentLoaded", () => {
    option1.addEventListener("change", () => {
        if(option1.checked){
            firstContainer.style.display = "block";
            secondContainer.style.display = "none";
        }
    });

    option2.addEventListener("change", () => {
        if(option2.checked){
            firstContainer.style.display = "none";
            secondContainer.style.display = "block";
        }
    })
})