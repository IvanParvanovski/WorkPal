document.addEventListener('DOMContentLoaded', main);

function main() {
    const rangeBar = document.getElementsByClassName('grid-range-bar')[0];
    const leftThumb = rangeBar.querySelector('.thumb:first-child');
    const rightThumb = rangeBar.querySelector('.thumb:last-child');
    const thumb1PositionInput = document.getElementById('thumb1Position');
    const thumb2PositionInput = document.getElementById('thumb2Position');

    // Function to handle both mouse and touch events
    function startDrag(event) {
        // Prevent default behavior to avoid scrolling on touch devices
        event.preventDefault();

        // Determine if the event is a mouse or touch event
        const isTouch = event.type.startsWith('touch');

        // Get the correct position based on the event type
        const clientX = isTouch ? event.touches[0].clientX : event.clientX;

        // Calculate the initial thumb position
        const rect = rangeBar.getBoundingClientRect();
        const thumb = event.target.classList.contains('thumb') ? event.target : null;
        const initialThumbPosition = thumb ? parseFloat(thumb.style.left) : null;
        const initialMousePosition = clientX - rect.left;

        // Add move and end event listeners to the document
        document.addEventListener(isTouch ? 'touchmove' : 'mousemove', handleDrag);
        document.addEventListener(isTouch ? 'touchend' : 'mouseup', endDrag);

        // Function to handle thumb movement during drag
        function handleDrag(event) {
            const clientX = isTouch ? event.touches[0].clientX : event.clientX;
            const mousePosition = clientX - rect.left;
            let newPosition = initialThumbPosition + (mousePosition - initialMousePosition) / rect.width * 100;

            // Ensure the minimum thumb does not pass the maximum thumb
            if (thumb === leftThumb) {
                newPosition = Math.min(newPosition, parseFloat(rightThumb.style.left));
            } else if (thumb === rightThumb) {
                newPosition = Math.max(newPosition, parseFloat(leftThumb.style.left));
            }

            // Limit the thumb movement within the range bar bounds
            newPosition = Math.min(100, Math.max(0, newPosition));
            if (thumb) {
                thumb.style.left = newPosition + '%';
                // Update the hidden field values
                if (thumb === leftThumb) {
                    thumb1PositionInput.value = newPosition;
                } else if (thumb === rightThumb) {
                    thumb2PositionInput.value = newPosition;
                }
            }
        }

        // Function to handle end of drag
        function endDrag(event) {
            document.removeEventListener(isTouch ? 'touchmove' : 'mousemove', handleDrag);
            document.removeEventListener(isTouch ? 'touchend' : 'mouseup', endDrag);
        }
    }

    // Add mousedown and touchstart event listeners to the range bar
    rangeBar.addEventListener('mousedown', startDrag);
    rangeBar.addEventListener('touchstart', startDrag);
}

 document.addEventListener('DOMContentLoaded', function() {
    const thumb1Input = document.getElementById('thumb1Position');
    const thumb2Input = document.getElementById('thumb2Position');
    const rangeBar = document.getElementsByClassName('grid-range-bar')[0];

    // Function to check screen width and change input types
    function checkScreenWidth() {
        if (window.innerWidth < 900) {
            thumb1Input.type = 'number';
            thumb2Input.type = 'number';
            thumb1Input.value = '150';
            thumb2Input.value = '25000';
            // rangeBar.style.visibility = 'hidden';
            // rangeBar.style.position = 'absolute'
        } else {
            // If the screen width is greater than or equal to 900px, revert to type "hidden"
            thumb1Input.type = 'hidden';
            thumb2Input.type = 'hidden';
            thumb1Input.value = '55';
            thumb2Input.value = '75';
            // rangeBar.style.visibility = 'visible';
            // rangeBar.style.position = 'relative';
        }
    }

     thumb1Input.addEventListener('change', function() {
        if (parseInt(thumb1Input.value) < 150) {
            thumb1Input.value = 150;
        }
    });

    thumb2Input.addEventListener('change', function() {
        if (parseInt(thumb2Input.value) < 100) {
            thumb2Input.value = 150;
        }
    });

    // Call the function initially
    checkScreenWidth();

    // Listen for window resize events and update input types accordingly
    window.addEventListener('resize', checkScreenWidth);
});
