const openPopupBtn = document.getElementById("showModal");
const popup = document.getElementById("popup");
const popupContent = document.querySelector("#popup-content")
const popupTitle = document.querySelector(".popup__title")
const popupContainer = document.querySelector(".popup__container")
const mainContent = document.querySelector(".main-content")
const chooseFileBtn = document.getElementById("choose-file")
const uploadImageForm = document.querySelector(".upload-avatar-form")
const fileInput = document.querySelector('input[type="file"]')
const submitButton = document.getElementById("confirm")
const formLabel = document.querySelector(".upload-avatar-form label")
const helpButton = document.getElementById("help-button");
const helpPopup = document.getElementById("help-popup");
const additionalInfoForm = document.querySelector(".additional-info-form");
const additionalSubmitButton = document.querySelector("#save");
const resetButton = document.getElementById("reset");

const modalOpen = () => {
    popup.style.visibility = "visible";
    popup.style.opacity = 1;
}

const modalClose = (event) => {
    const target = event.target;
    if(target === popupContent || target === popupTitle || target === popupContainer){
        popup.style.visibility = "hidden";
        popup.style.opacity = 0;
    }
}

const modalCloseWithoutClick = () => {
    popup.style.visibility = 'hidden';
    popup.style.opacity = 0;
}

openPopupBtn.addEventListener("click", modalOpen);
popup.addEventListener("click", modalClose);

fileInput.addEventListener("change", function() {
    if(fileInput.files.length > 0){
        submitButton.removeAttribute("disabled");
        formLabel.style.display = "none";
    } else {
        submitButton.setAttribute("disabled", "true");
        fileInput.removeAttribute("disabled");
    }
})


$(document).ready(function() {
    let currentUrl = window.location.href;
    $("#upload-form").on('submit', function(e){
        e.preventDefault();
        var formData = new FormData(this);
        $.ajax({
            url: currentUrl,
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: data => {
                $('#default-image').attr("src", data.new_image_url);
                $('#user-image-small').attr("src", data.new_image_url);
                modalCloseWithoutClick();
            },
            error: data => {
                console.log("Помилка завантаження")
            }
        });
    });
});


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
    const formElements = additionalInfoForm.elements;
    resetButton.disabled = true;
    additionalSubmitButton.disabled = true;

    for(let i = 0; i < formElements.length; i++) {
        const element = formElements[i]
        if (element.tagName === "INPUT" || element.tagName === "TEXTAREA") {
            initialFormValues[element.id] = element.value
        }
    }

    resetButton.addEventListener("click", () => {
        for(let i = 0; i < formElements.length; i++) {
            const element = formElements[i];
            if(element.tagName === "INPUT" || element.tagName === "TEXTAREA"){
                element.value = initialFormValues[element.id]
            }
        }
        resetButton.disabled = true;
        additionalSubmitButton.disabled = true;
    });

    /*const enableSubmitButton = () => {
        additionalSubmitButton.disabled = false;
        additionalSubmitButton.style.backgroundColor = "red";
    }

    const disableSubmitButton = () => {
        additionalSubmitButton.disabled = true;
        additionalSubmitButton.style.background = ""
    }*/

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
            if((element.tagName === "INPUT" || element.tagName === "TEXTAREA") &&
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
