document.addEventListener('DOMContentLoaded', function() {
    const checkbox = document.getElementById('checkbox');
    const navBar = document.getElementById('navBarStandard');

    checkbox.addEventListener('change', function() {
      if (checkbox.checked) {
        console.log('Checkbox marcado');
        navBar.style.display = 'block';
      } else {
        console.log('Checkbox desmarcado');
        navBar.style.display = 'none';
      }
    });
  });