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
    let clickableDivs = document.querySelectorAll('.project.clickable-div');

    // Initialize clickable div behavior
    clickableDivs.forEach(function (div) {
        div.addEventListener('click', handleClick);
    });
}

document.addEventListener('DOMContentLoaded', manageClickableDiv);
