

//<------BOX SLICE-------->//

//Seleccion de los botones
var flechaIz = document.getElementById('flechaIz');
var flechaDe = document.getElementById('flechaDe');
//seleccion del contenedor del Box Slice
var ConteBox = document.querySelector('.boxSliceContainer');
//seleccion del boxSlice
var boxSlice = document.getElementById('boxSlice');
boxSlice.classList.add('none');//Esto para el fade de las imagenes
console.log(boxSlice);
//seleccion de fotos 
var milanes = ['/static/images/milan.jpg', '/static/images/milan2.jpg', '/static/images/milan3.jpg', '/static/images/milan4.jpg', '/static/images/milan5.jpg'];

//Creacion del evento que dispara las funciones
flechaDe.addEventListener('click', sliceIz);
flechaIz.addEventListener('click', sliceDe);

//funciones principales
var color;
var contador = 0;
function condicionesCon(){
   
    if(contador == -1){
        contador = 4;
    }
    else if(contador == 5){
        contador = 0;
        
    }
    // debugger;
  
}

function cambiaColor(){

switch(contador){
    case 0:
    color = '#FF793E';
    break;
    case 1:
    color = '#F9DB65';
    break;
    case 2:
    color = '#D7B85D';
    break;
    case 3:
    color = '#FE8129';
    break;
    case 4:
    color = '#ACFE04';
    break;
}


}

function sliceIz(){

    cambiaColor();
    console.log(contador);
    ConteBox.style.backgroundColor = color;
    ConteBox.style.transition = '.2s all ease-in-out';
    boxSlice.style.backgroundImage = `url(${milanes[contador]})`;
    boxSlice.classList.replace('none','fadeInRight' );
    contador = contador - 1;
    condicionesCon();
    setTimeout(fadeImages, 300);
}

function sliceDe(){
    cambiaColor();
    console.log(contador);
    ConteBox.style.backgroundColor = color;
    ConteBox.style.transition = '.2s all ease-in-out';
    boxSlice.style.backgroundImage = `url(${milanes[contador]})`;
    boxSlice.classList.replace('none', 'fadeInLeft');
    contador = contador + 1;
    condicionesCon();
    setTimeout(fadeImages, 300);
    
}
function fadeImages(){
    if (boxSlice.classList.value == 'boxSlice fadeInLeft'){
        boxSlice.classList.replace('fadeInLeft', 'none');
        
        console.log('entre');
    }
    if (boxSlice.classList.value == 'boxSlice fadeInRight'){
        boxSlice.classList.replace('fadeInRight', 'none');
        console.log('entre');
    }
 
}

//<--OVERLAY DE IMAGENES -->

//Overlay de Pestaña Milan
var overlay = document.getElementById('overlay');//Seleccion del overlay
// console.log(overlay)
var close = document.querySelector('.icon-cross'); //Seleccion del boton de cerrado del Overlay
// console.log(close);
var body = document.getElementById('body');//Seleccion del body para desactivar el scroll al ampliar las fotos

var mostrarBtn = document.getElementsByClassName('imageDiv')//Seleccion del boton de abierto del overlay
console.log(mostrarBtn);
console.log(mostrarBtn[1]);

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
console.log()
var imagen;
var i;
var index;


mostrarBtn[0].addEventListener('click', function(){
    modal.style.backgroundImage =  `url(/static/images/inteMilan/inte1.jpeg)`;
    expandirFunction();
});
mostrarBtn[1].addEventListener('click', function(){
    modal.style.backgroundImage =  `url(/static/images/inteMilan/inte2.jpeg)`;
    expandirFunction();
});
mostrarBtn[2].addEventListener('click', function(){
    modal.style.backgroundImage =  `url(/static/images/inteMilan/inte3.jpeg)`;
    expandirFunction();
});
mostrarBtn[3].addEventListener('click', function(){
    modal.style.backgroundImage =  `url(/static/images/inteMilan/inte4.jpeg)`;
    expandirFunction();
});
mostrarBtn[4].addEventListener('click', function(){
    modal.style.backgroundImage =  `url(/static/images/inteMilan/inte5.jpeg)`;
    expandirFunction();
});
mostrarBtn[5].addEventListener('click', function(){
    modal.style.backgroundImage =  `url(/static/images/inteMilan/inte6.jpeg)`;
    expandirFunction();
});

function expandirFunction(n){
    overlay.style.visibility = 'visible';
    // modal.style.backgroundImage =  `url(./images/inteMilan/inte${n}.jpeg)`;
    modal.classList.add('modalAnimation');
    body.style.overflowY = 'hidden';//Activamos el scroll vertical
    // elegirUrl();
    // alert('funciono')
}


