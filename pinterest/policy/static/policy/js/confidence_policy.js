const accordions = document.querySelectorAll(".accordion");
const sidebar = document.querySelector("aside");
let sidebarTop = 500;

accordions.forEach(accordion => {
    accordion.addEventListener("click", () => {
        accordion.classList.toggle("active");
    })
})

function updateSidebarPosition(){
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if(scrollTop > sidebarTop){
        sidebar.style.transform = `translateY(${scrollTop - sidebarTop}px)`;
    }
    else {
        sidebar.style.transform = 'translateY(0)';
    }
}

window.addEventListener("load", updateSidebarPosition);
window.addEventListener("scroll", updateSidebarPosition);

