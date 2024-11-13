// JavaScript for smooth scrolling to sections
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('.btn-lg').addEventListener('click', function(event) {
        event.preventDefault();
        document.querySelector('#why-choose-us').scrollIntoView({ behavior: 'smooth' });
    });
});
