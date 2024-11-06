 // Função para abrir e fechar o dropdown
  function toggleDropdown() {
    document.querySelector('.dropdown').classList.toggle('open');
  }

  // Função para selecionar uma opção e exibi-la no botão
  function selectOption(option) {
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    dropdownToggle.textContent = option;
    toggleDropdown(); // Fecha o dropdown
  }

  // Fecha o dropdown ao clicar fora dele
  window.addEventListener('click', function(e) {
    const dropdown = document.querySelector('.dropdown');
    if (!dropdown.contains(e.target)) {
      dropdown.classList.remove('open');
    }
  });