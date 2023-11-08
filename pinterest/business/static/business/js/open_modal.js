const divContainer = document.getElementById("open-modal-div");
const modalContainer = document.querySelector(".modal-window");

let modalOpen = false;


//Відкриття модального вікна при натисканні на відповідну кнопку
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

//Закриття модального вікна при повторному натисканні на ту ж кнопку
divContainer.addEventListener("click", () => {
    let arrowIcon = document.querySelector("#open-modal-div #open-modal i");
    if (arrowIcon.classList.contains("rotate")){
        arrowIcon.classList.remove('rotate');
    } else {
        arrowIcon.classList.add('rotate')
    }
})


//Заборона закриття модального вікна при натисканні всередині нього
document.addEventListener("DOMContentLoaded", function(){
    modalContainer.addEventListener("click", (event) => {
        event.stopPropagation();
    });
});