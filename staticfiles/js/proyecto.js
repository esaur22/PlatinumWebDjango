// //Animaciones de entrada
// var portada = document.querySelector('portadaFondo');
// window.onload = function(){
// this.portada.classList.add('fadeInDownBig');
// }



//Overlay de Pestaña Proyectos
var overlay = document.getElementById('overlay');//Seleccion del overlay
// console.log(overlay)
var close = document.querySelector('.icon-cross'); //Seleccion del boton de cerrado del Overlay
// console.log(close);
var body = document.getElementById('body');//Seleccion del body para desactivar el scroll al ampliar las fotos

var mostrarBtn = document.querySelector('.enlarge')//Seleccion del boton de abierto del overlay
var modal = document.getElementById('modal');//El Modal
//Ejecucion Boton de cerrado del Overlay
overlay.addEventListener('click', cerrarFunction);
close.addEventListener('click', cerrarFunction);
function cerrarFunction(){
overlay.style.visibility = 'hidden'//Escondemos el overlay;
body.style.overflowY = 'visible';//Activamos el scroll vertical
modal.classList.remove('modalAnimation');

}

//Ejecucion del boton de abierto del Overlay 'Milan'
mostrarBtn.addEventListener('click', expandirFunction)
function expandirFunction(){
    overlay.style.visibility = 'visible';
    modal.style.backgroundImage = "url('/static/images/milan.jpg')";
    modal.classList.add('modalAnimation');
    body.style.overflowY = 'hidden';//Activamos el scroll vertical
    // alert('funciono')
}

//Seleccion y Ejecucion de boton de abierto de Siena y Catania
//seleccion  y ejecucion de Catania

var mostrarCataBtn = document.getElementById('mostrarCatania');
mostrarCataBtn.addEventListener('click', expandirCataniaFunction);

function expandirCataniaFunction(){
    modal.style.backgroundImage = "url('/static/images/catania.jpg')";
    modal.classList.add('modalAnimation');
    overlay.style.visibility = 'visible';
    body.style.overflowY = 'hidden';//Activamos el scroll vertical
}
//Seleccion y ejecucion de siena
var mostrarSienaBtn = document.getElementById('mostrarSiena');
mostrarSienaBtn.addEventListener('click', expandirSienaFunction);

function expandirSienaFunction(){
    modal.style.backgroundImage = "url('/static/images/Siena.jpg')";
    modal.classList.add('modalAnimation');
    overlay.style.visibility = 'visible';
    body.style.overflowY = 'hidden';//Activamos el scroll vertical
}
