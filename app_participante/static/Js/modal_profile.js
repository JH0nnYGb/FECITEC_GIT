const botaoAbrir = document.getElementById('abrir-modal');
        const botaoFecharInterno = document.getElementById('fechar-modal-interno');
        const modalOverlay = document.getElementById('modal-overlay');
        const botaoFechar = document.querySelector('.fechar-modal');

        function abrirModal() {
            modalOverlay.style.display = 'flex';
        }

        function fecharModal() {
            modalOverlay.style.display = 'none';
        }

        botaoAbrir.addEventListener('click', abrirModal);
        botaoFecharInterno.addEventListener('click', fecharModal);
        botaoFechar.addEventListener('click', fecharModal);

        // Fecha o modal se clicar fora dele
        modalOverlay.addEventListener('click', function(evento) {
            if (evento.target === modalOverlay) {
                fecharModal();
            }
        });
    

let profilePic = document.getElementById('profile-pic');
let updateImage = document.getElementById('update-image');

updateImage.onchange = function(){
    profilePic.src = URL.createObjectURL(updateImage.files[0]);
}