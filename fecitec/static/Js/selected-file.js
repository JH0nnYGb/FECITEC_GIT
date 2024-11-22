const fileInput = document.getElementById('file-upload');
const fileName = document.querySelector('.file-name');

fileInput.addEventListener('change', (event) => {
    // Atualiza o texto com o nome do arquivo selecionado
    if (fileInput.files.length > 0) {
        fileName.textContent = fileInput.files[0].name;
    } else {
        fileName.textContent = "Nenhum arquivo escolhido";
    }
});