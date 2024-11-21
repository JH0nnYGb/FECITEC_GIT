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

def login_participante(request):
    return render(request,'login_participante.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Obtem todos os grupos do usuário
            user_groups = user.groups.all()
            role = request.POST.get('role')

            if len(user_groups) > 1:
                # O usuário pertence a mais de um grupo
                if role and user_groups.filter(name=role).exists():
                    if role == 'Administrador':
                        return redirect('admin_fecitec:dashboard_admin')
                    elif role == 'Jurado':
                        return redirect('app_jurado:dashboard_jurado')
                    elif role == 'Avaliador':
                        return redirect('app_avaliador:dashboard_avaliador')
                    else:
                        messages.error(request, 'Função inválida.')
                        return render(request, 'login.html', {'form': form})
                else:
                    messages.error(request, 'Por favor, escolha uma função válida.')
                    return render(request, 'login.html', {'form': form})
            elif len(user_groups) == 1:
                # O usuário pertence a apenas um grupo
                group_name = user_groups[0].name
                if group_name == 'Administrador':
                    return redirect('admin_fecitec:dashboard_admin')
                elif group_name == 'Jurado':
                    return redirect('app_jurado:dashboard_jurado')
                elif group_name == 'Avaliador':
                    return redirect('app_avaliador:dashboard_avaliador')
                else:
                    messages.error(request, 'Grupo de usuário inválido.')
                    return render(request, 'login.html', {'form': form})
            else:
                # O usuário não pertence a nenhum grupo
                messages.error(request, 'Usuário não pertence a nenhum grupo.')
                return render(request, 'login.html', {'form': form})

        else:
            messages.error(request, 'Usuário ou senha incorretos. Por favor, tente novamente.')
            return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
   

def formigueiro_view(request):
    return render(request, 'formigueiro.html')


# crf token
def csrf_failure(request, reason=""):
    messages.error(request, "Ops !! algo deu errado, tente novemente")
    return redirect(request.META.get('HTTP_REFERER', 'login/'))


from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# Função para verificar o grupo do usuário
def is_administrator(user):
    return user.groups.filter(name='Administrador').exists()

# Proteção da view com login e grupo
@login_required
@user_passes_test(is_administrator, login_url='login/')
def dashboard_admin(request):
    return render(request, 'admin_fecitec/dashboard.html')
