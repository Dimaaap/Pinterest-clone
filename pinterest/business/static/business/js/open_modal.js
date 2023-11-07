const divContainer = document.getElementById("open-modal-div");
const modalContainer = document.querySelector(".modal-window");

let modalOpen = false;

divContainer.addEventListener("click", () => {
    if(!modalOpen){
        console.log("here")
        modalContainer.style.display = "block";
    }
    else {
        console.log("No, here")
        modalContainer.style.display = "none";
    }
    modalOpen = !modalOpen;
})

divContainer.addEventListener("click", () => {
    let arrowIcon = document.querySelector("#open-modal-div #open-modal i");
    if (arrowIcon.classList.contains("rotate")){
        arrowIcon.classList.remove('rotate');
    } else {
        arrowIcon.classList.add('rotate')
    }
})