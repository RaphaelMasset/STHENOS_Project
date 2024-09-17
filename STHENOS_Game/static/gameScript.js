document.querySelector('#catch').addEventListener('click', function() {
    alert('Well done');
});

let message = 0;

document.addEventListener('mousemove', (event) => {
    let catchButton = document.querySelector('#catch');
    let maxDistance = 120;
    let parentContainer = document.querySelector('#catch-container');

    // Get scroll offsets
    let scrollX = window.scrollX || window.pageXOffset;
    let scrollY = window.scrollY || window.pageYOffset;

    // Get button dimensions and position
    const rect = catchButton.getBoundingClientRect();
    const buttonX = rect.left + rect.width / 2 + scrollX;
    const buttonY = rect.top + rect.height / 2 + scrollY;

    // Get parent container dimensions and position
    const parentRect = parentContainer.getBoundingClientRect();
    const parentX = parentRect.left + scrollX;
    const parentY = parentRect.top + scrollY;
    const parentWidth = parentRect.width;
    const parentHeight = parentRect.height;

    // Calculate distance between button center and cursor
    const distance = Math.hypot(buttonX - (event.clientX + scrollX), buttonY - (event.clientY + scrollY));

    // Calculate the direction to move the button
    const dx = event.clientX + scrollX - buttonX;
    const dy = event.clientY + scrollY - buttonY;

    // If cursor is within maxDistance, move button away
    if (distance < maxDistance) {
        // Normalize the distance and calculate move distance
        const normalizedDistance = 1 - (distance / maxDistance);
        const moveDistance = 50 * normalizedDistance; // speed multiplier
        
        const angle = Math.atan2(dy, dx);
        const moveX = moveDistance * Math.cos(angle);
        const moveY = moveDistance * Math.sin(angle);
        
        // Calculate new position and ensure it stays within the container
        let newLeft = rect.left - moveX + scrollX;
        let newTop = rect.top - moveY + scrollY;

        // Ensure button stays within parent container
        if (newLeft < parentX || newTop < parentY || newLeft + rect.width > parentX + parentWidth || newTop + rect.height > parentY + parentHeight) {
            message = 1;
            catchButton.style.position = '';
            catchButton.style.left = '';
            catchButton.style.top = '';
        } else {
            catchButton.style.position = 'absolute';
            catchButton.style.left = `${newLeft}px`;
            catchButton.style.top = `${newTop}px`;
        }
    } else if (message === 0) {
        // Reset position if not near and message is still 0?
        
    }
});

document.addEventListener('mousemove', (event) => {
    console.log(message);
    if (message == 1) {
        setTimeout(function() {
            // Select the <h3> element by its ID
            const catchText = document.getElementById('catch-title');
        
            // Change the text content
            catchText.textContent = 'Catch me if you can (You can\'t by normal means)';
        }, 6000);
        message = 2;
    }
});
