const registrationForm = document.querySelector("#registration-form");
const loginForm = document.querySelector(".test-block");
const loginButton = document.getElementById("showLoginForm");
const registrationButton = document.getElementById("showRegistrationForm");
console.log('dadsadsadsada')

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

//Form validation section

const messageBox = document.getElementById("message-box");
const csrf = document.getElementsByName("csrfmiddlewaretoken");
const email = document.getElementById("email_input");
const password = document.getElementById("password_input");
const birthday = document.getElementById("birthday_field");
const url = "";
console.log("I`m here");

registrationForm.addEventListener("submit", e=>{
    console.log("Now, I`m here");
    e.preventDefault();
    const fd = new FormData();
    fd.append("csrfmiddlewaretoken", csrf[0].value);
    fd.append("email", email.value)
    fd.append("password", password.value)
    $.ajax({
        type: "POST",
        url: url,
        data: fd,
        success: function(response){
            console.log(response);
        },
        error: function(error){
            console.log(error)
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})