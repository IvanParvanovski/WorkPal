

var lastScrollTop = 0;
var navigationArrow = document.getElementById('navigation__arrow');

window.addEventListener('scroll', function() {
    var currentScroll = window.scrollY;
    
    if (currentScroll > lastScrollTop) {
        // Scrolling down or at the bottom
        navigationArrow.style.visibility = 'hidden';
    } else {
        // Scrolling up
        navigationArrow.style.visibility = currentScroll === 0 ? 'hidden' : 'visible';
    }

    lastScrollTop = currentScroll;
});

navigationArrow.addEventListener('click', function() {
    // Scroll to the top of the page
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });

    // Hide the arrow after clicking
    navigationArrow.style.visibility = 'hidden';
});
