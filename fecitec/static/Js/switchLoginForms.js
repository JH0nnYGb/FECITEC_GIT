
 // Alterna entre os formulários de login e criação de conta

 document.getElementById('show-create-account-forms').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('container-father').style.display = 'none';
    document.getElementById('container-father-creat').style.display = 'block';
    document.getElementById('container-father-creat').style.width = '80%';
})

document.getElementById('show-login-forms').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('container-father-creat').style.display = 'none';
    document.getElementById('container-father').style.display = 'block';
    
   });
