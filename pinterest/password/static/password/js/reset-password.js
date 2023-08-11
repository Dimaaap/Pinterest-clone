const searchIcon = document.querySelector(".search-icon");
const cancelIcon = document.querySelector(".cancel-button");
const cancelBtn = document.querySelector(".cancel-button-btn");
const inputField = document.querySelector("input");

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

cancelBtn.addEventListener("click", function(){
    inputField.value = "";
    searchIcon.style.display = "block";
    cancelIcon.style.display = "none";
})