// alert('hola');
var index = 0;

var listaimg = ['/static/images/sienaPortada.jpg', '/static/images/catania2.jpg', '/static/images/catania3.jpg', '/static/images/catania4.jpg', '/static/images/milan2.jpg', '/static/images/catania8.jpg', '/static/images/catania9.jpg', '/static/images/catania11.jpg', '/static/images/catania12.jpg', '/static/images/catania14.jpg', '/static/images/catania15.jpg', '/static/images/catania16.jpg', '/static/images/catania10.jpg', '/static/images/catania17.jpg', '/static/images/portada3.jpg'];

function interval(){
  setInterval(changeImage, 5000);
};

function changeImage() {
  
  var caja = document.getElementById('imagePortada')  
   caja.style.backgroundImage = `url(${listaimg[index]})`;
   caja.style.transition = '1s all ease-in-out'
//    css("background-image", 'url(' + listaimg[index] + ')');
                  
   index++;
                  
   if(index == 15)
      index = 0;
     
}
interval();