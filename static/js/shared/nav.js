// Disable scroll
function disableScroll() {
    // Get the current scroll position
    var scrollPosition = [
        self.pageXOffset || document.documentElement.scrollLeft || document.body.scrollLeft,
        self.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
    ];

    // Save the current scroll position
    var html = document.querySelector('html');
    html.dataset.scrollX = scrollPosition[0];
    html.dataset.scrollY = scrollPosition[1];

    // Set the style to prevent scrolling
    html.style.overflow = 'hidden';
    html.style.position = 'fixed';
    html.style.top = `-${scrollPosition[1]}px`;
    html.style.left = `-${scrollPosition[0]}px`;
}

// Enable scroll
function enableScroll() {
    // Retrieve the previous scroll position
    var html = document.querySelector('html');
    var scrollX = parseInt(html.dataset.scrollX || '0', 10);
    var scrollY = parseInt(html.dataset.scrollY || '0', 10);

    // Reset styles to allow scrolling
    html.style.overflow = '';
    html.style.position = '';
    html.style.top = '';
    html.style.left = '';

    // Restore the previous scroll position
    window.scrollTo(scrollX, scrollY);
}

const menuClosedIcon = document.getElementById("menu-closed-icon");
const menuOpenedIcon = document.getElementById("menu-opened-icon");
const navLinks = document.querySelector('.navigation__container .navigation__links');
const navUserLinks = document.querySelector('.navigation__container .navigation__user');
const navigation = document.querySelector('.navigation');

let windowWidth = 0;

function updateWindowWidth() {
    windowWidth = document.documentElement.clientWidth;

    if (windowWidth < 690) {
        let iconsVisibility = (menuClosedIcon.style.visibility == '' && menuOpenedIcon.style.visibility == '') ||
                              (menuClosedIcon.style.visibility == 'hidden' && menuOpenedIcon.style.visibility == 'hidden')
        
        if (iconsVisibility) {
            menuClosedIcon.style.visibility = 'visible';
            navLinks.style.display = 'none';
            navUserLinks.style.display = 'none';
        }

    } else {
        if (menuOpenedIcon.style.visibility == 'visible') {
            navLinks.style.display = 'none';
            navUserLinks.style.display = 'none';
            navigation.style.height = '';
        }

        navLinks.style.display = 'inline';
        navUserLinks.style.display = 'flex';

        menuClosedIcon.style.visibility = 'hidden';
        menuOpenedIcon.style.visibility = 'hidden';
    }

    menuClosedIcon.addEventListener('click', () => {
        menuClosedIcon.style.visibility = 'hidden';
        menuOpenedIcon.style.visibility = 'visible';
        disableScroll();

        navLinks.style.display = 'flex';
        navUserLinks.style.display = 'flex';
        navigation.style.height = '100vh';
    })

    menuOpenedIcon.addEventListener('click', () => {
        menuClosedIcon.style.visibility = 'visible';
        menuOpenedIcon.style.visibility = 'hidden';
        enableScroll();

        navLinks.style.display = 'none';
        navUserLinks.style.display = 'none';
        navigation.style.height = '';
    })
}




updateWindowWidth();
window.addEventListener('resize', updateWindowWidth);
