console.log("hello")

function openEditModal(id,name,email,phone,formation,position){


    document.getElementById("editMemberModal").style.display = "block";
    // document.getElementById("editMemberModal").style.display = "none";

    document.getElementById("memberId").value = id 
    document.getElementById("name").value = name
    document.getElementById("email").value = email
    document.getElementById("phone").value = phone
    
    // Resetar os checkboxes antes de marcar os selecionados
    document.querySelectorAll('input[name="funcao"]').forEach(checkbox => {
        checkbox.checked = position.split(", ").includes(checkbox.value);
    });
    // Resetar os checkboxes antes de marcar os selecionados
    document.querySelectorAll('input[name="formation"]').forEach(checkbox => {
        checkbox.checked = formation.split(", ").includes(checkbox.value);
    });

    // Separar os valores e marcar os checkboxes corretamente
    if (position) {
        let positions = position.split(", ");
        positions.forEach(value => {
            let checkbox = document.querySelector(`input[name="funcao"][value="${value}"]`);
            if (checkbox) {
                checkbox.checked = true;
            }
        });
    }
// Resetar os checkboxes de formação antes de marcar os selecionados
    let formationCheckboxes = document.querySelectorAll('input[name="formation"]');
    formationCheckboxes.forEach(checkbox => {
        checkbox.checked = formation.split(", ").includes(checkbox.value);
        checkbox.onclick = function() {
            formationCheckboxes.forEach(cb => {
                if (cb !== checkbox) {
                    cb.disabled = checkbox.checked;
                }
            });
        };
    });

    // Marcar as formações já atribuídas ao membro
    if (formation) {
        let formations = formation.split(", ");
        formations.forEach(form => {
            let checkbox = document.querySelector(`input[name="formation"][value="${form}"]`);
            if (checkbox) {
                checkbox.checked = true;
            }
        });
    }

    if (profileImageUrl) {
        // Mostrando o caminho da imagem de perfil
        const profileImg = document.getElementById('profileImagePreview');
        if (profileImg) {
            profileImg.src = profileImageUrl;
        }
    }

    
}


function closeEditModal(id,name,email,phone,formation,position){


    document.getElementById("editMemberModal").style.display = "none";
    // document.getElementById("editMemberModal").style.display = "none";

    document.getElementById("memberId").value = id 
    document.getElementById("name").value = name
    document.getElementById("email").value = email
    document.getElementById("phone").value = phone
    
    // Resetar os checkboxes antes de marcar os selecionados
    document.querySelectorAll('input[name="funcao"]').forEach(checkbox => {
        checkbox.checked = position.split(", ").includes(checkbox.value);
    });
    // Resetar os checkboxes antes de marcar os selecionados
    document.querySelectorAll('input[name="formation"]').forEach(checkbox => {
        checkbox.checked = formation.split(", ").includes(checkbox.value);
    });

    // Separar os valores e marcar os checkboxes corretamente
    if (position) {
        let positions = position.split(", ");
        positions.forEach(value => {
            let checkbox = document.querySelector(`input[name="funcao"][value="${value}"]`);
            if (checkbox) {
                checkbox.checked = true;
            }
        });
    }

    // Marcar as formações já atribuídas ao membro
    if (formation) {
        let formations = formation.split(", ");
        formations.forEach(form => {
            let checkbox = document.querySelector(`input[name="formation"][value="${form}"]`);
            if (checkbox) {
                checkbox.checked = true;
            }
        });
    }

    if (profileImageUrl) {
        // Mostrando o caminho da imagem de perfil
        const profileImg = document.getElementById('profileImagePreview');
        if (profileImg) {
            profileImg.src = profileImageUrl;
        }
    }

    
}