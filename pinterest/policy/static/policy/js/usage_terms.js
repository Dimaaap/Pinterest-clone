const header = document.querySelector(".header");
const sidebarContainer = document.querySelector(".sidebar");
const content = document.querySelector(".main-page");

let isSticky = false;

function setSidebarPosition() {
    const headerHeight = header.offsetHeight;
    const contentTop = content.offsetTop;

    if (window.pageYOffset >= contentTop - headerHeight) {
        if (!isSticky) {
            sidebarContainer.style.top = `${headerHeight}px`; // Змініть лише позицію
            isSticky = true;
        }
    } else {
        if (isSticky) {
            sidebarContainer.style.top = '0'; // Змініть лише позицію
            isSticky = false;
        }
    }
}


window.addEventListener("scroll", setSidebarPosition);
window.addEventListener("resize", setSidebarPosition);