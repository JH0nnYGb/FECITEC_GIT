from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Commission

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib import messages
##################################
from .forms import ContactForm
###################################
def home_view(request):
    return render(request, 'home.html')

def cronograma_view(request):
    return render(request, 'cronograma.html')

def submissao_view(request):
    return render(request, 'submissao.html')

def aprovados_view(request):
    return render(request, 'aprovado.html')

def certificados_view(request):
    return render(request, 'certificados.html')

def regulamento_view(request):
    return render(request, 'regulamento.html')

def comissao_view(request):
    members = Commission.objects.all()
    comission_paginator = Paginator(members, 1)
    members_num = request.GET.get('page')
    members_page = comission_paginator.get_page(members_num)

    context = {
        'comission': members_page,
        'current_page': members_page.number
    }

    return render(request, 'comissao.html', context)

def contate_view(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContactForm()

        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }

    return render(request, 'contate.html', context)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

         
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Verifica se o usuário está em mais de um grupo
            user_groups = user.groups.all()
            # Caso o usuário não pertença a nenhum grupo, verifica o 'role' escolhido
            role = request.POST.get('role')

            if user_groups.count() > 1:
                messages.error(request, 'Você pertencer a mais de um grupo. Escolha uma função.')

            # Verificar o grupo do usuário e redirecionar
            elif user.groups.filter(name='Administrador').exists() and role == 'Administrador':
                 return redirect('admin_fecitec:dashboard_admin')  # redireciona para a área do admin
            
            elif user.groups.filter(name='Jurado').exists()  and role == 'Jurado':
                return redirect('app_jurado:dashboard_jurado') # redireciona para a área do jurados
            
            elif user.groups.filter(name='Avaliador').exists()  and role == 'Avaliador':
                return redirect('app_avaliador:dashboard_avaliador')
            else:
                # Caso o role não seja válido
                messages.error(request, 'Por favor, selecione uma função válida.')
                return render(request, 'login.html', {'form': form})

        else:
            if form.non_field_errors():
                messages.error(request, 'Usuário ou senha incorretos. Por favor, tente novamente.')
            
    else:

        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
   

def formigueiro_view(request):
    return render(request, 'formigueiro.html')
