// // Crear una función para cargar el SVG del círculo
// function loadCircleSVG(callback) {
//     fetch("./elem_folder/w_circle.svg")
//     .then((response) => response.text())
//     .then((svgContent) => {
//         const parser = new DOMParser();
//         const doc = parser.parseFromString(svgContent, "image/svg+xml");
//         const circleSVG = doc.querySelector("svg");
//         callback(circleSVG);
//     })
//     .catch((error) => {
//         console.error("Error al cargar el archivo SVG:", error);
//     });
// }

// export function buildTree(node, x, y, depth) {
//     if (!node) return; // Verificar si el nodo existe

//     // Ajusta la posición del círculo SVG clonado
//     const xOffset = 10 * depth; // Desplazamiento horizontal basado en la profundidad
//     const yOffset = 50; // Desplazamiento vertical fijo

//     // Llama a la función loadCircleSVG para cargar el círculo SVG
//     loadCircleSVG(function (circleSVG) {
//     // Clona el círculo SVG para tener uno independiente por nodo
//     const clonedCircle = circleSVG.cloneNode(true);

//     // Ajusta las coordenadas del círculo clonado
//     const circleX = x + xOffset;
//     const circleY = y + yOffset;
//     clonedCircle.setAttribute("c", circleX);
//     clonedCircle.setAttribute("cy", circleY);

//     // Asigna un ID único al círculo basado en su profundidad
//     const circleId = `circle_${depth}`;
//     clonedCircle.setAttribute("id", circleId);

//     // Agrega el círculo clonado al documento
//     svg.appendChild(clonedCircle);

//     // Calcula el desplazamiento para los hijos
//     const childY = circleY + 30; // Desplazamiento vertical para los hijos
//     let childX = x; // Valor predeterminado
//     if (node.children && Array.isArray(node.children)) {
//         childX -= (node.children.length - 1) * 30;
//     }

//     // Recorre los hijos de manera recursiva
//     if (node.children && Array.isArray(node.children)) {
//         node.children.forEach((child) => {
//             node.children.forEach((child, index) => {
//                 buildTree(child, childX, childY, depth + 1);
//                 childX += 60; // Ajusta según tus necesidades
//             });
//         });
//       }
    
//     });
// }



export function createCircleSVG() {
    // Cargar el círculo blanco desde "./elem_folder/w_circle.svg"
    return new Promise((resolve, reject) => {
      fetch('./elem_folder/w_circle.svg')
        .then((response) => response.text())
        .then((svgContent) => {
          const parser = new DOMParser();
          const doc = parser.parseFromString(svgContent, 'image/svg+xml');
          const circleSVG = doc.querySelector('svg');
          resolve(circleSVG);
        })
        .catch((error) => {
          reject(error);
        });
    });
  }
  
export function buildTree(node, svg, x, y, depth) {
    // Crear un círculo SVG y ajustar sus atributos según la posición y el nivel de profundidad
    const xOffset = 60; // Espacio horizontal entre círculos
    const yOffset = 80; // Espacio vertical entre niveles
    const radius = 20; // Radio del círculo

    createCircleSVG().then((circleSVG) => {
    const clonedCircle = circleSVG.cloneNode(true);
    clonedCircle.setAttribute('x', x);
    clonedCircle.setAttribute('y', y);
    svg.appendChild(clonedCircle);

    // Recorrer los hijos de manera recursiva
    if (node.children) {
        let childY = y - (node.children.length - 1) * yOffset;
        let childX = x + xOffset;

        node.children.forEach((child) => {
        buildTree(child, svg, childX, childY, depth + 1);
        childY += yOffset;
        });
    }
    });
}