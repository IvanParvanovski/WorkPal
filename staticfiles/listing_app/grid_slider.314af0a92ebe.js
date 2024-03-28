document.addEventListener('DOMContentLoaded', main);

function main() {
    const rangeBar = document.getElementsByClassName('grid-range-bar')[0]
    const leftThumb = rangeBar.querySelector('.thumb:first-child');
    const rightThumb = rangeBar.querySelector('.thumb:last-child');

    // Add mousedown event listener to the range bar
    rangeBar.addEventListener('mousedown', function (event) {
        // Check if the left or right thumb is clicked
        var target = event.target;
        if (target.classList.contains('thumb')) {
            var thumb = target;
            // Add mousemove event listener to the document
            document.addEventListener('mousemove', onMouseMove);
            // Add mouseup event listener to the document
            document.addEventListener('mouseup', onMouseUp);
        }
        // Function to handle mousemove event
        function onMouseMove(event) {
            // Calculate new thumb position in percentages
            var rect = rangeBar.getBoundingClientRect();
            var mouseX = event.clientX - rect.left;
            var newPosition = (mouseX / rect.width) * 100;

            // Ensure the thumb stays within the range bar bounds
            newPosition = Math.min(100, Math.max(0, newPosition));

            // Update thumb position
            thumb.style.left = newPosition + '%';
        }
        // Function to handle mouseup event
        function onMouseUp(event) {
            // Remove mousemove and mouseup event listeners
            document.removeEventListener('mousemove', onMouseMove);
            document.removeEventListener('mouseup', onMouseUp);
        }
    });
}