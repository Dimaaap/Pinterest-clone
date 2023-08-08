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


const handleErrors = (type, text) => {
    registrationForm.innerHTML = `<div class="alert alert-${type}" role="alert">
        ${text}
    </div>`
}

const messageBox = document.getElementById("message-box");
const csrf = document.getElementsByName("csrfmiddlewaretoken");
const email = document.getElementById("email_input");
const password = document.getElementById("password_input");
const birthday = document.getElementById("birthday_input");
const hiddenField = document.getElementById("hidden-field")
$(document).ready(function(){
    $("#registration-form").on("submit", (function(event) {
        event.preventDefault();
        const fd = new FormData();
        fd.append("hidden", hiddenField.value)
        fd.append("csrfmiddlewaretoken", csrf[0].value);
        fd.append("email", email.value);
        fd.append("password", password.value);
        fd.append("birthday_field", birthday.value);
        $.ajax({
            type: "POST",
            url: "",
            data: fd,
            processData: false,
            contentType: false,
            cache: false,
            success: (response) => {
                if(response.result === "success"){
                    window.location.href = "http://127.0.0.1:8080/wall";
                    console.log("Success response")
                }
                else if(response.result === "error"){
                    const errorMessage = response.message;
                    const errorContainer = $("#error-message");
                    console.log(`Error text - ${errorMessage}`)
                    errorContainer.text(errorMessage).show();
                }
            },
            error: (error) => {
                console.log(error);
            }
        })
    }))
})

