console.log('helloWorld');
 // Alterna entre os formulários de login e criação de conta

 document.getElementById('show-create-account-forms').addEventListener('click', function(event){
    event.preventDefault();
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('create-account-forms').style.display = 'block';
 });

 document.getElementById('showLoginForms').addEventListener('click',function(event){
    event.preventDefault();
    document.getElementById('create-account-forms').style.display = 'none';
    document.getElementById('login-form').style.display = 'block';
 });
