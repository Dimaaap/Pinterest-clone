const helpButton = document.getElementById("help-button");
const helpPopup = document.getElementById("help-popup");
const additionalInfoForm = document.querySelector(".additional-info-form");
const additionalSubmitButton = document.querySelector("#save");
const resetButton = document.getElementById("reset");
const form = document.querySelector(".personal-data-form");


let isClose = false;

const openHelpPopup = () => {
    helpPopup.style.visibility = "visible";
    isClose = true;
}

const closeHelpPopup = (event) => {
    helpPopup.style.visibility = "hidden";
    isClose = false;
}

helpButton.addEventListener("click", (event) => {
    if(isClose){
        closeHelpPopup();
    } else {
        openHelpPopup(event);
    }
})

document.addEventListener("DOMContentLoaded", () => {
    const initialFormValues = {}
    const formElements = form.elements;
    resetButton.disabled = true;
    additionalSubmitButton.disabled = true;

    for(let i = 0; i < formElements.length; i++) {
        const element = formElements[i]
        if (element.tagName === "INPUT" || element.tagName === "TEXTAREA" || element.tagName === "SELECT"
        || element.tagName === "RADIO") {
            initialFormValues[element.id] = element.value;
            element.addEventListener("input", () => {
                checkFormData();
            });
        }
    }

    resetButton.addEventListener("click", () => {
        for(let i = 0; i < formElements.length; i++) {
            const element = formElements[i];
            if(element.tagName === "INPUT" || element.tagName === "TEXTAREA"){
                element.value = initialFormValues[element.id]
            } else if (element.tagName === "SELECT"){
                element.value = initialFormValues[element.id]
            } else if (element.tagName === "RADIO"){
                console.log(element.value)
                element.value = initialFormValues[element.id]
            }
        }
        resetButton.disabled = true;
        additionalSubmitButton.disabled = true;
    });

    for(let i = 0; i < formElements.length; i++){
    const element = formElements[i];
    if(element.tagName === "INPUT" || element.tagName === "TEXTAREA") {
        element.addEventListener("input", () => {
            checkFormData();
        });
    }
}

    const checkFormData = () => {
        let hasData = false;
        for(let i = 0; i < formElements.length; i++){
            const element = formElements[i];
            if((element.tagName === "INPUT" || element.tagName === "TEXTAREA" || element.tagName === "SELECT") &&
            element.value !== initialFormValues[element.id]){
                hasData = true;
                break;
            }
        }
        resetButton.disabled = !hasData;
        if(hasData){
            additionalSubmitButton.disabled = false;
        } else {
            additionalSubmitButton.disabled = true;
            additionalSubmitButton.style.backgroundColor = "";
        }
    }
    checkFormData();
});
