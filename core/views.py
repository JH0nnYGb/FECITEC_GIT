from django.shortcuts import render, redirect
from core.models import GrupoPersonalizado
# Create your views here.

def redirecionar_usuario(request):
    # Obtém todos os grupos do usuário
    user_grupos = request.user.grupos_personalizados.all()

    # Verifica se o usuário pertence a algum grupo específico e redireciona
    if user_grupos.filter(nome='Administrador').exists():
        return redirect('admin_fecitec:dashboard_admin')
    elif user_grupos.filter(nome='Jurado').exists():
        return redirect('app_jurado:dashboard_jurado')
    elif user_grupos.filter(nome='Avaliador').exists():
        return redirect('app_avaliador:dashboard_avaliador')
    elif user_grupos.filter(nome='Participante').exits():
        return redirect('app_participante:dashboard_participante')
    else:
        return redirect('login')
