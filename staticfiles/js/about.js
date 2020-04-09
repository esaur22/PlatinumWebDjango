//menu
const menu = document.querySelector('.menu');
// console.log(menu)
const menuButton = document.querySelector('.icon-list');
// console.log(menuButton)
function hideShow(){
    menu.classList.toggle('is-active');
}
menuButton.addEventListener('click', hideShow);