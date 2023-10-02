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

