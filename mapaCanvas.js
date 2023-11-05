import { createCircleSVG, buildTree } from './buildTree.js';
import { zoom_pan } from './zoom_pan.js';


const svgObject = document.getElementById("svg");
const svg = svgObject.contentDocument.getElementById("svg")

//ZOOM

zoom_pan(svg)


//Falta asociar nodos con datos.
//Hacerlo con el modulo buildTree que debe ser modificado para esta nueva funcionalidad