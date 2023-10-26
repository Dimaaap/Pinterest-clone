console.log("In this page")

$(document).ready(function(){
    const currentUrl = window.location.href;

    $("#change-modal").submit(function(event) {
        event.preventDefault();
        let formData = $(this).serialize();
        let csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        formData += `&csrfmiddlewaretoken=${csrfToken}`;

        console.log("before the AJAX request")

        $.ajax({
            type: "POST",
            url: currentUrl,
            data: formData,
            dataType: "json",
            processData: false,
            contentType: "application/json",
            headers: {
                "X-CSRFToken": csrfToken
            },
            success: function(data){
                console.log("in success")
                if("errors" in data){
                    let errorMessages = $("#error-messages");
                    console.log(errorMessages)
                    errorMessages.empty();

                    for(let error in data.errors){
                        console.log(error)
                        errorMessages.append("<p>" + error + "</p>");
                    }
                } else if("success" in data){
                    console.log("All success")
                    errorMessages.append("<p>Пароль успішно змінено</p>")
                }
            },
            error: function(xhr, status, error){
                console.log(xhr)
                console.log(status)
                console.log("ERROR!")
                console.log(error);
                console.warn(xhr.responseText)
            }
        })
    })
})