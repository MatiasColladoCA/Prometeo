
const fs = require('fs');
const button = document.getElementById("myButton");
button.addEventListener("click", funct);
function funct(){
  let data = fs.readFileSync('datos.json');
  let json = JSON.parse(data);
  let idioma = prompt("idioma (ingles, espanol): ");
  // let categ_dict = json[idioma][categoría];
  let count = 0;
  let strCateg = "";
  for (let i ; i < json.lenghth; i++) {
    let each_dict = json[i];
    if("categ" in each_dict){
      strCateg += each_dict["categ"];
    }
  }
  let categ = prompt("categoría: ", strCateg);

  
  let = nombre = prompt("Nombre: ");
  let link = prompt("link: ");
  let = descr = prompt("descripción: ");
  let = icono = prompt("ícono: ");
    // for (let i = 0; i < 6; i++){
    
    let newLi = document.createElement("li");
    let liText = document.createTextNode(input);
    newLi.appendChild(liText);
    document.getElementById("myList").appendChild(newLi);
    
    console.log(data);
}


let menu = document.getElementById("ul-general");
let video = document.getElementById("video-fondo");
let transparencia = document.getElementById("transparencia");
let boxDescripcion = document.getElementById("box-degrade-descripcion");
window.addEventListener("scroll", function(){
  let value = window.scrollY;
  menu.style.top = value + "px";
  video.style.top = value + "px";
  transparencia.style.top = value + "px";
  if (value >1){
    menu.style.background ="linear-gradient(180deg, rgba(8, 0, 12, 0.8),rgba(0, 0, 0, 0))";
  }
  else {
      menu.style.background = "none";
  }
})
