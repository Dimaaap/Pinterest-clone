const setPasswordForm = document.getElementById("set-new-password");
const submitButton = document.querySelector(".btn-reset-password");
const popupWindow = document.querySelector(".popup-window");
const closePopup = document.querySelector(".close-popup");
const modalOverlay = document.getElementById("modal-overlay");


$(document).ready(function() {
    $("#set-new-password").submit(function(event) {
    event.preventDefault();
    modalOverlay.style.display = "block";

    $.ajax({
      type: "POST",
      url: $(this).attr('action'),
      data: $(this).serialize(),
      success: function(response) {
        if (response.success) {
          modalOverlay.style.display = "block";
          popupWindow.style.display = "block";
        } else {
          alert("Error: " + response.error);
        }
      }
    });
  });
});


closePopup.addEventListener("click", () => {
    modalOverlay.style.display = "none";
    popupWindow.style.display = "none";
    window.location.href = "/";
})