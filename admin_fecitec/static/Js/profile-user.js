document.getElementById('profileCheckbox').addEventListener('change', function () {
    const profileImage = document.querySelector('.profile-image');
    const profileModal = document.querySelector('.container-profile');
  
    if (this.checked) {
        // Adicionar estilos ao marcar
        profileImage.style.border = '3px solid #4caf50'; // Borda verde
        profileImage.style.filter = 'brightness(0.8)';  // Escurecer imagem

        // Aplique a classe para exibir com animação suave
        profileModal.classList.add('visible');
    } else {
        // Remover estilos ao desmarcar
        profileImage.style.border = '3px solid transparent'; // Remove borda
        profileImage.style.filter = 'none';                 // Remove filtro

        // Remover a classe para esconder com animação suave
        profileModal.classList.remove('visible');
    }
});
