console.log("In this page")


/*$(document).ready(function(){
    console.log("I`m here")
    let currentUrl = window.location.href;

    $("#change-modal").submit(function(event){
        event.preventDefault();
        let formData = $(this).serialize();
        let csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        console.log(csrfToken)
        formData += `&csrfmiddlewaretoken=${csrfToken}`;
        console.log(formData);

        $.ajax({
            type: "POST",
            url: currentUrl,
            data: formData,
            dataType: "json",
            success: function(data) {
                //if(data.errors){
                //    let errorMessages = $("#error-messages");
                //    errorMessages.empty();
                //    $.each(data.errors, function(field, error){
                //        errorMessages.append(`<p> ${error} </p>`);
                //        print("here")
                //    });
                console.log('sdasdsadsa')
                errorMessages.append("<p>Пароль успішно змінено</p>")
            },
            error: function(data) {
               if(data.errors){
                    let errorMessages = $("#error-messages");
                    errorMessages.empty();
                    $.each(data.errors, function(field, error){
                        errorMessages.append(`<p> ${error} </p>`);
                        print("here")
                    });
                }
            })
        })
    })
})*/

$(document).ready(function() {
    console.log("I`m here");
    const currentUrl = window.location.href;

    $("#change-modal").submit(function(event){
        event.preventDefault();
        let formData = $(this).serialize();
        let csrfToken = $('input[name=csrfmiddlewaretoken]').val()
        formData += `&csrfmiddlewaretoken=${csrfToken}`;

        console.log('asdasdsad')
        $.ajax({
            type: "POST",
            url: currentUrl,
            data: formData,
            dataType: 'json',
            success: function(data){
                console.log("dadasda")
                errorMessages.append("<p>Пароль успішно змінено</p>")
            },
            error: function(data){
                console.log(data.errors)
                if(data.errors){
                    let errorMessages = $("#error-messages");
                    $.each(data.errors, function(field, error){
                        errorMessages.append(`<p> ${error} </p>`);
                        print("here")
                    })
                }
            }
        })
    })
})