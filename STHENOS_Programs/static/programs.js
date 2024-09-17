document.addEventListener('DOMContentLoaded', function() {
    // Attach the event listener to the form once the DOM is fully loaded
    document.querySelector('form').addEventListener('submit', handleFormSubmit);

        const absImages = [
            "/static/img/bicycle_crunch.png",
            "/static/img/bird_dog.png",
            "/static/img/crunch.png",
            "/static/img/crunch2.png",
            "/static/img/dead_bug.png",
            "/static/img/declined_crunch.png",
            "/static/img/flutter_kick2.png",
            "/static/img/heel_tap1.png",
            "/static/img/heel_tap2.png",
            "/static/img/hip_raise.png",
            "/static/img/hollow_body_hold.png",
            "/static/img/leg_raise_hiplift.png",
            "/static/img/legraise.png",
            "/static/img/mountain_climber.png",
            "/static/img/russian_twist.png",
            "/static/img/scissor.png"
        ];
        
        const absImageElement = document.getElementById("abs-image");
        const changeImageButton = document.getElementById("change-image-btn");
        const timerElement = document.getElementById("timer");
        let timerInterval;  // to store the interval ID
    
        changeImageButton.addEventListener("click", function() {
            // Get a random index for the image array
            const randomIndex = Math.floor(Math.random() * absImages.length);
            
            // Set the src attribute of the img element to the new random image
            absImageElement.src = absImages[randomIndex];

            let time = 0; // Time in seconds
            clearInterval(timerInterval); // Clear previous interval (if any)
            timerElement.textContent = "00:00";
            
            // Update the timer every second
            timerInterval = setInterval(function() {
                time += 1;

                // Format time as MM:SS
                const minutes = Math.floor(time / 60);
                const seconds = time % 60;
                timerElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

                // Stop the timer at 40 seconds
                if (time >= 40) {
                    clearInterval(timerInterval);
                }
            }, 1000);
        });
});

function handleFormSubmit(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the form element
    const form = event.target;

    // Create a FormData object to hold the form data
    const formData = new FormData(form);

    // Get the CSRF token
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Send the POST request using fetch
    fetch(form.action, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken
        },
        body: formData
    })
    .then(response => {
        if (response.ok) {
            return response.blob(); // Handle binary data (PDF) correctly
        } else {
            throw new Error('Network response was not ok.');
        }
    })
    .then(blob  => {
        // Create a URL for the blob and trigger the download
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'STHENOS_strenght_program.pdf'; // Set the filename
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url); // Clean up
    })
    .catch(error => {
        // Handle any errors that occurred during the fetch
        console.error('Error:', error);
    });
}
