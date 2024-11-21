from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# Função para verificar o grupo do usuário
def is_administrator(user):
    return user.groups.filter(name='Administrador').exists()

# Proteção da view com login e grupo
@login_required(login_url='fecitec:login/')  # Redireciona para o login se o usuário não estiver autenticado
@user_passes_test(is_administrator, login_url='fecitec:login/')  # Redireciona se o grupo não for "Administrador"

def admin_dashboard(request):
    return render(request, 'dashboard_admin.html')