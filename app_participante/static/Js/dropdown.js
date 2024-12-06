document.querySelectorAll('.dropdown-button').forEach(function(button) {
    button.addEventListener('click', function(event) {
        // Fecha todos os dropdowns antes de abrir o atual
        document.querySelectorAll('.dropdown-content').forEach(function(dropdown) {
            dropdown.style.display = 'none';
        });

        // Alterna o dropdown atual
        var dropdownContent = this.nextElementSibling;
        dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
        event.stopPropagation();
    });
});

// Fechar todos os dropdowns ao clicar fora deles
window.addEventListener('click', function(event) {
    document.querySelectorAll('.dropdown-content').forEach(function(dropdown) {
        dropdown.style.display = 'none';
    });
});
