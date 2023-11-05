export function coordJerarqui(d) {

    const lienzo = document.getElementById('lienzo');
    const ancho = parseFloat(window.getComputedStyle(lienzo).getPropertyValue('width'));
    const alto = parseFloat(window.getComputedStyle(lienzo).getPropertyValue('height'));

    const escalaX = d3.scaleLinear()
        .domain([0, ancho]) // Por ejemplo, si los datos van de 0 a 10
        .range([0, ancho]); // Ajusta el ancho del lienzo

    const escalaY = d3.scaleLinear()
        .domain([0, alto]) // Rango de valores en el eje Y
        .range([0, alto]); // Ajusta la altura del lienzo

    const nivelJerarquia = d.depth; // Profundidad de la jerarquía
    const x = escalaX(d.data.valueX); // Utiliza un valor de datos para el eje X
    const y = nivelJerarquia * 10; // Ajusta la posición vertical según la profundidad
    
    return { x, y };
}