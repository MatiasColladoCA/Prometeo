export function zoom_pan(svg){
    

    //PANNING Y ZOOMING
    let isPanning = false;
    let panStartX, panStartY, panOffsetX, panOffsetY;
    let scale = 1;

    svg.addEventListener("mousedown", (e) => {
        isPanning = true;
        panStartX = e.clientX;
        panStartY = e.clientY;
        panOffsetX = svg.viewBox.baseVal.x;
        panOffsetY = svg.viewBox.baseVal.y;
        // e.preventDefault();


    });

    svg.addEventListener("mousemove", (e) => {
    if (isPanning) {
        const deltaX = e.clientX - panStartX;
        const deltaY = e.clientY - panStartY;
        svg.viewBox.baseVal.x = panOffsetX - deltaX / scale;
        svg.viewBox.baseVal.y = panOffsetY - deltaY / scale;
        // e.preventDefault();
    }
    });

    svg.addEventListener("mouseup", () => {
    isPanning = false;
    // e.preventDefault();
    });

    
    
    const minScale = 0.5;  // Escala mínima permitida
    const maxScale = 0.6;  // Escala máxima permitida

    svg.addEventListener("wheel", (e) => {
    // e.preventDefault();
    const scaleFactor = e.deltaY > 0 ? 0.99 : 1.01;

    

    console.log(scale)
    console.log("and")
    console.log(scaleFactor)
    // Aplicar el nuevo factor de escala
    scale *= scaleFactor;

    // Aplicar límites a la escala
    if (scale < minScale) {
        scale = minScale;
        return;
    } else if (scale > maxScale) {
        scale = maxScale;
        return;
    }



    const x = e.clientX - svg.getBoundingClientRect().left;
    const y = e.clientY - svg.getBoundingClientRect().top;
    const dx = x - svg.viewBox.baseVal.x - svg.viewBox.baseVal.width / 2;
    const dy = y - svg.viewBox.baseVal.y - svg.viewBox.baseVal.height / 2;
    svg.viewBox.baseVal.x += dx * (1 - 1 / scaleFactor) / scale;
    svg.viewBox.baseVal.y += dy * (1 - 1 / scaleFactor) / scale;



    // Calcular la nueva posición del viewBox
    const newWidth = svg.viewBox.baseVal.width / scaleFactor;
    const newHeight = svg.viewBox.baseVal.height / scaleFactor;

    const offsetX = (svg.viewBox.baseVal.width - newWidth) * (x / svg.clientWidth);
    const offsetY = (svg.viewBox.baseVal.height - newHeight) * (y / svg.clientHeight);




    scale *= scaleFactor;
    svg.viewBox.baseVal.width = svg.clientWidth / scale;
    svg.viewBox.baseVal.height = svg.clientHeight / scale;


    svg.viewBox.baseVal.x += offsetX;
    svg.viewBox.baseVal.y += offsetY;

    });
    }