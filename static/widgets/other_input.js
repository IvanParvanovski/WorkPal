document.addEventListener('DOMContentLoaded', function() {
    const selectField = document.getElementById('selectField');
    const otherInputContainer = document.getElementById('otherInputContainer');

    selectField.addEventListener('change', function() {
        if (selectField.value === 'other') {
            otherInputContainer.style.display = 'block';
        } else {
            otherInputContainer.style.display = 'none';
        }
    });
});