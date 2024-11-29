document.addEventListener('DOMContentLoaded', function() {
    const telefoneInput = document.getElementById('telephone');
    
    if (telefoneInput) {
        telefoneInput.addEventListener('input', function() {
            formatarTelefone(this);
        });
    }
});

function formatarTelefone(input) {
    let valor = input.value.replace(/\D/g, ''); // Remove qualquer coisa que não seja número


    
    valor = valor.replace(/(\d{2})(\d{5})(\d{0,1})/, '($1) $2-$3');  // Formato: (XX) XXXXX


    input.value = valor; // Atualiza o valor do input com a máscara
}