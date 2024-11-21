from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, reverse 
from django.contrib import messages

@login_required
def admin_dashboard(request):
    if not request.user.groups.filter(name='Administradores').exists():
          messages.error(request, "Você não tem permissão para acessar esta página.")
          return redirect('fecitec:user_login')  # Redireciona para a página inicial ou login
    return render(request, 'dashboard_admin.html')