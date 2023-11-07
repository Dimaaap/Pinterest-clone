const inputField = document.getElementById("search-input");
const searchIcon = document.querySelector(".search-bar form i")


inputField.addEventListener("focus", () => {
    searchIcon.style.display = "none";
})

inputField.addEventListener("blur", () => {
    searchIcon.style.display = "inline";
})