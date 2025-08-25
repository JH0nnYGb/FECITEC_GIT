from django.shortcuts import render, redirect
from django.core.paginator import Paginator


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm
from django.contrib.auth.models import Group
from core.forms import SubmissionToWorkForm


################ Importacaoes do Cores #######

from core.models import Commission
from core.models import GruposFecitec
from core.models import Participante
from core.forms import ParticipantCreationForm
from core.models import User, Participante,Instituicao

###############################################

def home_view(request):
    return render(request, 'home.html')

def cronograma_view(request):
    return render(request, 'cronograma.html')



def submissao_view(request):
    form = SubmissionToWorkForm()  # Cria o formulário inicialmente

    # Define o contexto, com o formulário, fora da verificação de POST
    context = {
        'form': form
    }

    if request.method == 'POST' and request.FILES:
        form = SubmissionToWorkForm(request.POST, request.FILES)

        if form.is_valid():
            # Obtendo o participante logado
            try:
                participante = Participante.objects.get(user=request.user)
            except Participante.DoesNotExist:
                messages.error(request, "Participante não encontrado.")
                return redirect('alguma_url_de_erro')

            # Atribuindo o participante ao formulário antes de salvar
            submissao = form.save(commit=False)  # Não salva imediatamente
            submissao.participante = participante  # Atribui o participante
            submissao.save()  # Agora salva

            messages.success(request, 'Submissão enviada com sucesso!')
            return redirect('fecitec:submissao')  # Redireciona para a página de submissão

    return render(request, 'submissao.html', context)  # Sempre retorna o contexto

def aprovados_view(request):
    return render(request, 'aprovado.html')

def certificados_view(request):
    return render(request, 'certificados.html')

def regulamento_view(request):
    return render(request, 'regulamento.html')

def comissao_view(request):
    members = Commission.objects.all()
    comission_paginator = Paginator(members, 6)
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

###### VIEWS DE LOGIN PARA OS MEMBROS DA COMISSAO  #########
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Obtém todos os grupos do usuário
            user_groups = request.user.grupos_fecitec.all()
            role = request.POST.get('role')

            print(user_groups)

            if len(user_groups) > 1:
                # O usuário pertence a mais de um grupo
                if role and user_groups.filter(nome=role).exists():
                    if role == 'Administrador' and user_groups.filter(nome='Administrador').exists():
                        return redirect('admin_fecitec:dashboard_admin')
                    elif role == 'Jurado' and user_groups.filter(nome='Jurado').exists():
                        return redirect('app_jurado:dashboard_jurado')
                    elif role == 'Avaliador' and user_groups.filter(nome='Avaliador').exists():
                        return redirect('app_avaliador:dashboard_avaliador')
                    else:
                        messages.error(request, 'Função inválida.')
                        return render(request, 'login.html', {'form': form})
                else:
                    messages.error(request, 'Por favor, escolha uma função válida.')
                    return render(request, 'login.html', {'form': form})
            elif len(user_groups) == 1:
                # O usuário pertence a apenas um grupo
                group_name = user_groups[0].nome
                if role == group_name:
                    if group_name == 'Administrador':
                        return redirect('admin_fecitec:dashboard_admin')
                    elif group_name == 'Jurado':
                        return redirect('app_jurado:dashboard_jurado')
                    elif group_name == 'Avaliador':
                        return redirect('app_avaliador:dashboard_avaliador')
                else:
                    messages.error(request, 'Grupo ou função não correspondem.')
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

###### VIEWS DE LOGIN PARA O PARTICIPANTE FECITEC #########
def login_participante_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Verifique se o usuário pertence ao grupo 'Participante'
            if user.grupos_fecitec.filter(nome='Participante').exists():
                
                login(request, user)
                return redirect('app_participante:dashboard_participante')# Certifique-se de que a URL esteja correta
            else:
                messages.error(request, 'Você não tem permissão para acessar essa página.')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos. Tente novamente.')
    else:
        form = AuthenticationForm()
    return render(request, 'login_participante.html', {'form': form})



def Cadastrar_participante_views(request):
    form = ParticipantCreationForm()

    if request.method == 'POST':
        form = ParticipantCreationForm(request.POST)
        if form.is_valid():
            # Verifique se o nome de usuário já existe antes de salvar
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if User.objects.filter(username=username).exists():
                messages.error(request, "Já existe um usuário com este nome.")
                return render(request, 'cadastro_participante.html', {'form': form})

            if password1 != password2 or password2 != password1:
                messages.error(request, "As senhas não coincidem. Tente novamente.")
                return render(request, 'cadastro_participante.html', {'form': form})

            if len(password1) < 8:
                messages.error(request, "A senha deve ter pelo menos 8 caracteres.")
                return render(request, 'cadastro_participante.html', {'form': form})

            if password1.isdigit():
                messages.error(request, "A senha não pode ser totalmente numérica.")
                return render(request, 'cadastro_participante.html', {'form': form})

            # Salvar usuário
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['nome_participante']
            user.email = form.cleaned_data['email_participante']
            user.set_password(password1)
            user.save()

            # Criar participante
            participante = Participante.objects.create(
                user=user,
                nome_participante=form.cleaned_data['nome_participante'],
                email_participante=form.cleaned_data['email_participante'],
                municipio_participante=form.cleaned_data['municipio_participante'],
                endereco=form.cleaned_data['endereco'],
                cep_pacticipante=form.cleaned_data['cep_pacticipante'],
                celular=form.cleaned_data['celular'],
                bairro=form.cleaned_data['bairro'],
                estado_participante=form.cleaned_data['estado_participante'],
                formacao_participante=form.cleaned_data['formacao_participante'],
            )

            # Associar usuário ao grupo "Participante"
            grupo_participante = GruposFecitec.objects.get(nome='Participante')
            grupo_participante.usuarios.add(user)

            messages.success(request, "Conta criada com sucesso! Faça login para continuar.")
            return redirect('fecitec:login_participante')
        
        else:
            for field, error in form.errors.items():
                if field == 'email_participante' and error == 'Informe um endereço de email válido.':
                        messages.error(request, "O e-mail informado não é válido. Por favor, verifique.")
                elif field == 'password2' and error == 'Os dois campos de senha não correspondem.':
                        messages.error(request, "As senhas digitadas não coincidem. Tente novamente.")
                messages.error(request, f"{error}")

    return render(request, 'cadastro_participante.html', {'form': form})
