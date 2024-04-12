 // Function to handle click events
 function handleClick(event) {
    // Prevent the default behavior of the click event
    event.preventDefault();

    // Add your click event handling logic here
    let url = this.getAttribute('data-url');
    window.location.href = url;
}

// Function to initialize or deactivate clickable div behavior based on window size
function manageClickableDiv() {
    var clickableDivs = document.querySelectorAll('.job-offer.clickable-div');

    if (window.innerWidth <= 1000) {
        // Initialize clickable div behavior
        clickableDivs.forEach(function (div) {
            div.addEventListener('click', handleClick);
        });
    } else {
        // Deactivate clickable div behavior
        clickableDivs.forEach(function (div) {
            div.removeEventListener('click', handleClick);
        });
    }
}

// Call the function to manage clickable div behavior when the DOM content is loaded and when the window is resized
document.addEventListener('DOMContentLoaded', manageClickableDiv);
window.addEventListener('resize', manageClickableDiv);
