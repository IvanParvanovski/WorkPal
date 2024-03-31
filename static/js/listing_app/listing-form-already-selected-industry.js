const checkboxes = document.querySelectorAll('#id_industries input[type="checkbox"]');

checkboxes.forEach(checkbox => {
    if (checkbox.checked) {
        checkbox.parentElement.classList.add('clicked');
    }
});
