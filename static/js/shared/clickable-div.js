var clickableDivs = document.querySelectorAll('.clickable-div');
clickableDivs.forEach(function (div) {
    div.addEventListener('click', function () {
        var url = this.getAttribute('data-url');
        window.location.href = url;
    });
});
