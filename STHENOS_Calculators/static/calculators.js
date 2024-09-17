document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".input-field").forEach(input => {
        input.addEventListener("keyup", calculate);
        input.addEventListener("change", calculate);
    });
    calculate();

});

function calculate() {
    let weight, height, wrist, ankle, bodyfat,age;

    document.querySelectorAll(".input-field.numeric").forEach(input => {
        const value = parseFloat(input.value);
        if (!isNaN(value)) {
            switch (input.id) {
                case "weight":
                    weight = value;
                    break;
                case "height":
                    height = value;
                    break;
                case "wrist":
                    wrist = value;
                    break;
                case "ankle":
                    ankle = value;
                    break;
                case "bodyfat":
                    bodyfat = value;
                    break;
                case "age":
                    age = value;
                    break;
            }
        }
    });

    if (!height) {
        document.getElementById("marc-perry").innerText = 'Marc Perry Formula:';
        document.getElementById("martin-berkhan").innerText = 'Martin Berkhan Formula:';
        document.getElementById("elena-kouri").innerText = 'Elena Kouri Formula:';
        document.getElementById("casey-butt").innerText = 'Casey Butt Formula: ';
        if(!weight){
            document.getElementById("imc-result").innerText = 'IMC:';
        }
    }

    
    if ( !isNaN(height) && height > 0 ) {
        heightmeter = height * 0.01

        if (!isNaN(weight) && weight > 0 ) {
            // IMC Calculation
            const imc = weight / (heightmeter * heightmeter);
            document.getElementById("imc-result").innerText = `IMC/BMI: ${imc.toFixed(2)}`;
            //87 to 342  -> 255 pixels pour 24 pt IMC dc 10.625 pixel par pt IMC
          
            imc<16? cursor.style.top = '61px' : cursor.style.top=cursor.style.top;
            imc>16? cursor.style.top = '112px' : cursor.style.top=cursor.style.top;
            imc>18.4? cursor.style.top = '163px' : cursor.style.top=cursor.style.top;
            imc>25? cursor.style.top = '214px' : cursor.style.top=cursor.style.top;
            imc>30? cursor.style.top = '264px' : cursor.style.top=cursor.style.top;
            imc>35? cursor.style.top = '315px' : cursor.style.top=cursor.style.top;
            imc>40? cursor.style.top = '366px' : cursor.style.top=cursor.style.top;
        }
        // Marc Perry Formula   
        const heightInches = height * 0.393701;
        const marcPerry = (((heightInches - 70) * 5 + 160)*0.453592)/0.95;
        document.getElementById("marc-perry").innerText = `Marc Perry Formula: ${marcPerry.toFixed(2)} kg`;

        // Martin Berkhan Formula
        const martinBerkhan = height - 100;
        document.getElementById("martin-berkhan").innerText = `Martin Berkhan Formula: ${martinBerkhan.toFixed(2)} kg`;

        // Elena Kouri Formula
        const elenaKouri = Math.pow(heightmeter, 2) * 26 - (6.1 * (1.8 - heightmeter));
        document.getElementById("elena-kouri").innerText = `Elena Kouri Formula: ${elenaKouri.toFixed(2)} kg`;

        if (!isNaN(wrist) && !isNaN(ankle) && !isNaN(bodyfat) && !!wrist && !!ankle && !!bodyfat) {
            wristInch = wrist * 0.393701;
            ankleInch = ankle * 0.393701;
            bodyfatDecimal = bodyfat
            // Casey Butt Formula
            console.log(wristInch, ankleInch, heightInches, bodyfatDecimal )
            const caseyButt = (Math.pow(heightInches, 1.5) * (Math.sqrt(wristInch) / 22.6670 + Math.sqrt(ankleInch) / 17.0104) * (bodyfatDecimal / 224 + 1))*0.453592;
            document.getElementById("casey-butt").innerText = `Casey Butt Formula: ${caseyButt.toFixed(2)} kg`;
        }
    }
}