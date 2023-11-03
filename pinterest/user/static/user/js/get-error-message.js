console.log("In this page")

$(document).ready(function(){
    const currentUrl = window.location.href;
    const errorBlock = $("#error-messages");

    $("#modal-form").submit(function(event) {
        event.preventDefault();
        let formData = $(this).serialize();
        let csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        formData += `&csrfmiddlewaretoken=${csrfToken}`;

        $.ajax({
            type: "POST",
            url: currentUrl,
            data: formData,
            dataType: "json",
            processData: true,
            contentType: "application/x-www-form-urlencoded",
            headers: {
                "X-CSRFToken": csrfToken
            },
            success: function(data){
                if("errors" in data){
                    let errorMessages = $("#error-messages");
                    errorMessages.empty();
                    console.log(data.errors);
                    errorMessages.append("<p>" + data.errors[0] + "</p>");
                } else if("success" in data){
                    errorMessages.append("<p>Пароль успішно змінено</p>")
                }
            },
            error: function(xhr, status, error){
                console.log(error);
            }
        })
    })
})