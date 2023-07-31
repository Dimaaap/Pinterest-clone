const registrationForm = document.querySelector("#registration-form");
const loginForm = document.querySelector(".test-block");
const loginButton = document.getElementById("showLoginForm");
const registrationButton = document.getElementById("showRegistrationForm");

function showRegistrationForm(){
    registrationForm.style.display = "block";
    loginForm.style.display = "none";
}

function showLoginForm(){
    registrationForm.style.display = "none";
    loginForm.style.display = "block";
    console.log("This function work");
}

window.addEventListener("load", showRegistrationForm);
loginButton.addEventListener("click", function(event){
    event.preventDefault();
    showRegistrationForm();
})
loginButton.addEventListener("click", function(event){
    event.preventDefault();
    showLoginForm();
});
console.log('adaddadasdsadasd')