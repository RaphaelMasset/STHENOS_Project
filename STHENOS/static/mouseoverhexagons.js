document.addEventListener('mousemove', (event) => {
    let hexagonsIndex = document.querySelectorAll('.hexaIndex');
    //let hexagonsNav = document.querySelectorAll('.hexaNav');
    let maxScaleFactor = 1.3;

    hexagonsIndex.length == 0 ? maxScaleFactor = 1.1: maxScaleFactor = 1.3;
    //hexagonsIndex.length == 0 ? hexagonsIndex = hexagonsNav : hexagonsIndex = hexagonsIndex;
    
    hexagonsIndex.forEach(hexagonsIndex  => {
        const rect = hexagonsIndex.getBoundingClientRect();
        const hexagonX = rect.left + rect.width / 2;  //gives the distance from the left edge of the viewport to the left edge of the hexagon.
        const hexagonY = rect.top + rect.height / 2;
        const distance = Math.hypot(hexagonX - event.clientX, hexagonY - event.clientY);  // Euclidean distance cursor - hexa
        
        const maxDistance = 240;
        
        if (distance < maxDistance) {
            const normalizedDistance = 1- (distance / maxDistance);  //0 si loin 1 si proche
            const normalizedDistancesquared = Math.pow(normalizedDistance, 1.2);  //non exponentialisation de l'effet de distance
            const scale = 1 + (maxScaleFactor - 1) * (normalizedDistancesquared);  //if cursor at the center of the hexagon ratio will be 0 -> full effect scale factor
            hexagonsIndex.style.transform = `scale(${scale})`;
        } else {
            hexagonsIndex.style.transform = 'scale(1)';
        }
    });
});
