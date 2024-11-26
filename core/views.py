from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from core.models import GrupoPersonalizado
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

from core.forms import CustomUserCreationForm
from core.models import GrupoPersonalizado, Participante
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
    elif user_grupos.filter(nome='Participante').exists():
        return redirect('app_participante:dashboard_participante')
    else:
        return redirect('login')


def Cadastrar_participante(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Salva o usuário
            user = form.save()
            user.first_name = form.cleaned_data['nome_completo']
            user.email = form.cleaned_data['email']
            user.save()

            
            instituicao_nome = form.cleaned_data['instituicao_nome']
            municipio = form.cleaned_data['municipio']
            estado_instituicao = form.cleaned_data['estado_instituicao']
            endereco = form.cleaned_data['endereco']
            cidade = form.cleaned_data['cidade']
            celular = form.cleaned_data['celular']
            bairro = form.cleaned_data['bairro']
            estado = form.cleaned_data['estado']
            formacao = form.cleaned_data['formacao']

            
            participante = Participante.objects.create(
                user=user,
                nome_instituicao=instituicao_nome,
                municipio=municipio,
                estado_instituicao=estado_instituicao,
                endereco=endereco,
                cidade=cidade,
                celular=celular,
                bairro=bairro,
                estado=estado,
                formacao=formacao
            )

       
            grupo_participante = GrupoPersonalizado.objects.get(nome='Participante')
            grupo_participante.usuarios.add(user)

        
            instituicao = Instituicao.objects.create(
                user=user,
                instituicao_nome=instituicao_nome,
                municipio=municipio,
                estado_instituicao=estado_instituicao
            )

            messages.success(request, "Conta criada com sucesso!")
            login(request, user)  
            return redirect('fecitec:login_participante')
        else:
            messages.error(request, "Erro ao criar conta. Verifique os campos.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'cadastro_participante.html', {'form': form})