let currentStep = parseInt(localStorage.getItem('currentStep')) || 0;
const submitButton = document.getElementById("submit-button");
const backButton = document.getElementById("back-button") || null;
const firstForm = document.getElementById("first-form");
const secondForm = document.getElementById("second-form");
const thirdForm = document.getElementById("third-form");
const fourthForm = document.getElementById("fourth-form");


const updateSetIndicator = () => {
    const stepIndicators = document.querySelectorAll(".step-circle");
    stepIndicators.forEach((indicator, index) => {
        indicator.classList.toggle("active", index === currentStep);
        indicator.classList.toggle('completed', index < currentStep);
    })
}

const goToStep = (step) => {
    currentStep = step;
    localStorage.setItem('currentStep', currentStep);
    updateSetIndicator();
}

let formsArray = [firstForm, secondForm, thirdForm, fourthForm];


updateSetIndicator();