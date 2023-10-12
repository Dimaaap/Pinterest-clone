const helpButton = document.getElementById("help-button");
const helpPopup = document.getElementById("help-popup");

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