let currentStep = parseInt(localStorage.getItem('currentStep')) || 1;
const submitButton = document.getElementById("submit-button");
const backButton = document.getElementById("back-button") || null;
const forms = document.querySelectorAll(".form");


let formsIndexMap = new Map([
    ["first-form", 1],
    ["second-form", 2],
    ["third-form", 3],
    ["fourth-form", 4]
])

const goToStep = (step) => {
    currentStep = step;
    localStorage.setItem('currentStep', currentStep);
    updateSetIndicator(step);
}

document.addEventListener('DOMContentLoaded', (event) => {
    activeForm = forms[0].id;
    currentIndex = formsIndexMap.get(activeForm) - 1;
    goToStep(currentIndex)
})

const updateSetIndicator = (index) => {
    const stepIndicators = document.querySelectorAll(".step-circle");
    stepIndicators.forEach((indicator, indIndex) => {
        if(indIndex <= index){
            indicator.classList.add("active");
        }
    })
}