document.addEventListener('DOMContentLoaded', function() {
    const checkbox = document.getElementById('checkbox');
    const navBar = document.getElementById('navBarStandard');
    const navAdmin = document.getElementById('navBarAdmin')

    checkbox.addEventListener('change', function() {
      if (checkbox.checked) {
        console.log('Checkbox marcado');
        navBar.style.display = 'block';
        navAdmin.style.display = 'none'
      } else {
        console.log('Checkbox desmarcado');
        navBar.style.display = 'none';
        navAdmin.style.display = 'block'
      }
    });
  });