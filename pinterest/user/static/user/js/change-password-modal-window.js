openModalBtn = document.getElementById("open-change-btn");
closeModalBtn = document.getElementById("cancel");
modalWindow = document.getElementById("change-modal");

let close = false;


const openPasswordPopup = () => {
    modalWindow.style.display = "block";
    close = true;
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