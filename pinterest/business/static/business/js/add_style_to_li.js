document.addEventListener("DOMContentLoaded", () => {
    let elementLi = document.querySelectorAll(".helper-li");
    elementLi.forEach((li) => {
        li.addEventListener("mouseover", () => {
            console.log(li);
        })
    })
})

