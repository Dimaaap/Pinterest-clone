const openPopupBtn = document.getElementById("showModal");
const popup = document.getElementById("popup");
const mainContent = document.querySelector(".main-content")


const modalOpen = () => {
    popup.style.visibility = "visible";
    popup.style.opacity = 1;
}

const modalClose = (event) => {
    const target = event.target;
    if(target === mainContent){
        popup.style.visibility = "hidden";
        popup.style.opacity = 0;
    }
}

openPopupBtn.addEventListener("click", modalOpen);
popup.addEventListener("click", modalClose);