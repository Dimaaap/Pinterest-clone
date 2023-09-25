document.addEventListener("DOMContentLoaded", function(){
    const dropdownBtn = document.querySelector(".dropdown-btn");
    const dropdownContent = document.querySelector(".dropdown-content");

    const profileDetailBtn = document.querySelector("#detail-btn");
    const profileDetailDropdown = document.querySelector("#account-settings")

    dropdownBtn.addEventListener("click", function(){
        dropdownContent.style.display = (dropdownContent.style.display === "block") ? "none": "block";
    });

    profileDetailBtn.addEventListener("click", function(){
        profileDetailDropdown.style.display = (profileDetailDropdown.style.display === "block") ? "none" : "block";
    });

    dropdownContent.addEventListener("click", function(e){
        if(e.target.tagName === "LI"){
            dropdownBtn.textContent = e.target.textContent;
            dropdownContent.style.display = "none";
        }
    });

    profileDetailDropdown.addEventListener("click", function(e) {
        if(e.target.tagName === "LI") {
            profileDetailBtn.textContent = e.target.textContent;
            profileDetailDropdown.style.display = "none";
        }
    })

    window.addEventListener("click", function(e){
        if(!dropdownBtn.contains(e.target) && !dropdownContent.contains(e.target)) {
            dropdownContent.style.display = "none";
        }
        else if(!profileDetailBtn.contains(e.target) && !profileDetailDropdown.contains(e.target)) {
            profileDetailDropdown.style.display = "none";
        }
    });
});