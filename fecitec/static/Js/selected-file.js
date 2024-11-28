    // Função para atualizar o nome do arquivo selecionado
    document.getElementById('file-upload-modelo').addEventListener('change', function(event) {
        const fileName = event.target.files.length ? event.target.files[0].name : 'Nenhum arquivo escolhido';
        this.nextElementSibling.textContent = fileName;  // Atualiza o texto do span
    });

    document.getElementById('file-upload-panner').addEventListener('change', function(event) {
        const fileName = event.target.files.length ? event.target.files[0].name : 'Nenhum arquivo escolhido';
        this.nextElementSibling.textContent = fileName;  // Atualiza o texto do span
    });