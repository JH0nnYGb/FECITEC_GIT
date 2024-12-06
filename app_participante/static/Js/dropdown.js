document.querySelector('.dropdown-button').addEventListener('click', function(event) {
    var dropdownContent = this.nextElementSibling;
    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
    event.stopPropagation();
});

// Fechar o dropdown quando clicar em qualquer lugar fora dele
window.addEventListener('click', function(event) {
    if (!event.target.matches('.dropdown-button')) {
        var dropdowns = document.querySelectorAll('.dropdown-content');
        dropdowns.forEach(function(dropdown) {
            dropdown.style.display = 'none';
        });
    }
});
