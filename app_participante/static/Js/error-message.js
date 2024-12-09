function checkFile() {
    const element = document.getElementById('error-archives');

    const inputModel = document.getElementById('file-upload-modelo');
    
    if (inputModel.files.length === 0) {
        if (element.style.display === 'none') {
    
            element.style.display = 'block';
        }
    }
}