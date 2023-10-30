const sidebar = document.querySelector("aside");
const contentContainer = document.querySelector(".main-page")
let sidebarTop = 500;
let contentHeight = contentContainer.clientHeight+880;
let sidebarHeight = sidebar.clientHeight;
const fa


function updateSidebarPosition() {

  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  if (scrollTop > sidebarTop) {
    if (scrollTop + sidebarHeight < contentHeight) {
      sidebar.style.transform = `translateY(${scrollTop - sidebarTop}px)`;
    } else {
      sidebar.style.transform = `translateY(${contentHeight - sidebarHeight - sidebarTop}px)`;
    }
  } else {
    sidebar.style.transform = 'translateY(0)';
  }
}
window.addEventListener('load', updateSidebarPosition);
window.addEventListener('scroll', updateSidebarPosition);
