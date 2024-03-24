console.log('hi')
var labels = document.querySelectorAll('#id_industries div label');

for (const label of labels) {
    label.addEventListener('click', function (event) {
        currentLabel = event.target;

        if (currentLabel.classList.contains('clicked')) {
            currentLabel.classList.remove('clicked');
        } else {
            currentLabel.classList.add('clicked');
        }
    })
}