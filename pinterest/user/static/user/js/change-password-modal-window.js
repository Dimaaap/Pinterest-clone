const openModalBtn = document.getElementById("open-change-btn");
const closeModalBtn = document.getElementById("cancel");
const modalWindow = document.getElementById("change-modal");
const newPasswordModalField = document.getElementById("id_new_password");
const passwordField = document.getElementById("password-field");
const errorBlock = document.getElementById("error-messages")


let close = false;


const openPasswordPopup = () => {
    modalWindow.style.display = "block";
    close = true;
    newPasswordModalField.value = passwordField.value;
    errorBlock.innerHTML = "";
}


const closePasswordPopup = () => {
    modalWindow.style.display = "none";
    close = false;
}

openModalBtn.addEventListener("click", (event) => {
    if(!close){
        openPasswordPopup();
    }
})

closeModalBtn.addEventListener("click", (event) => {
    if(close){
        closePasswordPopup();
    }
})