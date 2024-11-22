from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard_participante(request):
    if not request.user.groups.filter(name='Participante').exists():
          messages.error(request, "Você não tem permissão para acessar esta página.")
          return redirect('fecitec:participante')  # Redireciona para a página inicial ou login
    return render(request, 'dashboard_participante.html')
