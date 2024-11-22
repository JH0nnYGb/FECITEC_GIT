function showPage(pageId) {
    // Esconde todas as páginas
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
    });

    // Mostra a página desejada
    document.getElementById(pageId).classList.add('active');
}