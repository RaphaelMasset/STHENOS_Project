function changeStyle(style) {
    const body = document.body;
    const hexaElements = document.getElementsByClassName('hexa');
    const titreElements = document.getElementsByClassName('titre');

    // Iterate over all title elements once
    for (let i = 0; i < titreElements.length; i++) {
        switch (style) {
            case 'style1':
                titreElements[i].style.color = '#492f19'; 
                titreElements[i].style.textShadow = '1px 1px 2px #25180d'; // Updated text shadow

                body.style.background = 'linear-gradient(0.25turn, #116466, #D1E8E2, #116466)';
                body.style.backgroundColor = '#ffffff'; // White background for body

                // Iterate over all hexagon elements
                for (let j = 0; j < hexaElements.length; j++) {
                    hexaElements[j].style.background = 'radial-gradient(circle, #116466 0%, #2C3531 75%, #116466 90%)'; // Updated gradient
                    hexaElements[j].style.color = '#FFCB9A'; // Light gray color for text
                }
                break;

            case 'style2':
                titreElements[i].style.color = '#3d52a0'; 
                titreElements[i].style.textShadow = '1px 1px 2px #3D52A0'; // Updated text shadow

                body.style.background = 'linear-gradient(0.25turn, #3D52A0, #ADBBDA, #3D52A0)';
                body.style.backgroundColor = '#ffffff'; // White background for body

                // Iterate over all hexagon elements
                for (let j = 0; j < hexaElements.length; j++) {
                    hexaElements[j].style.background = 'radial-gradient(circle, #7091E6 0%, #3D52A0 75%, #3D52A0 90%)'; // Updated gradient
                    hexaElements[j].style.color = '#EDE8F5'; // Light color for text
                }
                break;

            case 'style3':
                titreElements[i].style.color = '#F5F5F5'; // Off-White for text
                titreElements[i].style.textShadow = '1px 1px 3px #1E2A38'; // Dark Slate shadow

                body.style.background = 'linear-gradient(0.25turn, #2C2E3A, #4B4F61, #2C2E3A)'; // Symmetrical Gradient
                body.style.backgroundColor = '#4B4F61'; // Cool Gray background for body

                // Iterate over all hexagon elements
                for (let j = 0; j < hexaElements.length; j++) {
                    hexaElements[j].style.background = 'radial-gradient(circle, #0A21C0 0%, #2C2E3A 70%, #B3B4BD 90%)'; // Vibrant Blue to Charcoal with Light Gray
                    hexaElements[j].style.color = '#F5F5F5'; // Off-White text color
                }
                break;
                
            case 'style4':
                titreElements[i].style.color = '#F5F5F5'; // Off-White for text
                titreElements[i].style.textShadow = '1px 1px 3px #1E2A38'; // Dark Slate shadow

                body.style.background = 'linear-gradient(0.25turn, #2C2E3A, #4B4F61, #2C2E3A)'; // Symmetrical Gradient
                body.style.backgroundColor = '#4B4F61'; // Cool Gray background for body

                // Iterate over all hexagon elements
                for (let j = 0; j < hexaElements.length; j++) {
                    hexaElements[j].style.background = 'radial-gradient(circle, #0A21C0 0%, #2C2E3A 70%, #B3B4BD 90%)'; // Vibrant Blue to Charcoal with Light Gray
                    hexaElements[j].style.color = '#F5F5F5'; // Off-White text color
                }
                break;

            default:
                console.log('Unknown style:', style);
                break;
        }
    }
}
