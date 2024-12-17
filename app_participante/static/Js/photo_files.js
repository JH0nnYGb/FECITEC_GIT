// CAPTURAR A IMAGE DO USUARIO 

let profilePic = document.getElementById('profile-pic');
let updateImage = document.getElementById('update-image');

updateImage.onchange = function(){
    profilePic.src = URL.createObjectURL(updateImage.files[0]);
}