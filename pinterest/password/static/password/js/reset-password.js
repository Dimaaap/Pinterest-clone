const searchIcon = document.querySelector("#email-input");
const cancelIcon = document.querySelector(".cancel-button");
const cancelBtn = document.querySelector(".cancel-button-btn");
const inputField = document.querySelector("#id_email");
const searchField = document.querySelector("input");
const findIcon = document.querySelector("#header-icon")
const headerCancel = document.querySelector("#header-cancel")
const popupMenyButton = document.querySelector(".popup-menu")
const sendMailButton = document.querySelector(".btn-send-mail")
const findEmailButton = document.querySelector("#find-email");

inputField.addEventListener("input", function(event){
    if(inputField.value.length > 0){
        searchIcon.style.display = "none";
        cancelIcon.style.display = "block";
    } else if(inputField.value.length < 1){
        console.log("Now, here");
        searchIcon.style.display = "block";
        cancelIcon.style.display = "none";
    }
})

inputField.addEventListener("input", function(e){
    if (inputField.value.includes(".com") && inputField.value.length >= 6){
        sendMailButton.style.display = "block";
        find.email.style.backgroundColor = "gray";
    }
    else {
        sendMailButton.style.display = "none";
        find.email.style.backgroundColor = "red";
    }
})

searchField.addEventListener("input", function(event) {
    if(searchField.value.length > 0){
        findIcon.style.display = "none";
        headerCancel.style.display = "block";
    } else if(searchField.value.length < 1){
        findIcon.style.display = "block";
        headerCancel.style.display = "none";
    }
})

headerCancel.addEventListener("click", function(){
    searchField.value = "";
    findIcon.style.display = "block";
    headerCancel.style.display = "bloch"
})

cancelBtn.addEventListener("click", function(){
    inputField.value = "";
    searchIcon.style.display = "block";
    cancelIcon.style.display = "none";
})