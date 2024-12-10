from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import Participante
from core.models import SubmissionToWork
from core.forms import SubmissionToWorkForm

@login_required
def dash_participante(request):
    try:
        # Recupera o participante associado ao usuário logado
        participante = Participante.objects.get(user=request.user)
    except Participante.DoesNotExist:
        messages.error(request, "Participante não encontrado.")
        return redirect('alguma_url_de_erro')  # Redirecione para uma página apropriada

    # Recupera as submissões (caso sejam gerais ou específicas do participante)
    submissions = SubmissionToWork.objects.filter(participante=participante)

    # Verifica permissões
    if not request.user.grupos_personalizados.filter(nome='Participante').exists():
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('alguma_url_de_erro')

    # Contexto enviado para o template
    context = {
        'participante': participante,
        'submissions': submissions,
    }
    return render(request, 'dashboard_participante.html', context)

def submissao_trabalho(request):
    if request.method == 'POST':
        # Capturando os valores do formulário diretamente
        school_name = request.POST.get('school_name')
        area = request.POST.get('area')
        state = request.POST.get('state')
        municipality = request.POST.get('municipality')
        formation = request.POST.get('formation')
        form_of_presentation = request.POST.get('formOfPresentation')
        title = request.POST.get('title')
        sub_area = request.POST.get('sub_area')
        summary = request.POST.get('summary')
        arquivo_modelo = request.FILES.get('arquivo_modelo')  # Para arquivos

        # Obtendo o participante logado
        try:
            nome_participante = Participante.objects.get(user=request.user)
        except Participante.DoesNotExist:
            messages.error(request, "Participante não encontrado.")
            return redirect('app_participante:dashboard_participante')

        # Salvando os dados no banco de dados
        SubmissionToWork.objects.create(
            title=title,
            school_name=school_name,
            area=area,
            state=state,
            municipality=municipality,
            formation=formation,
            form_of_presentation=form_of_presentation,
            sub_area=sub_area,
            summary=summary,
            arquivo_modelo=arquivo_modelo,
            nome_participante=nome_participante
        )

        # Mensagem de sucesso e redirecionamento
        messages.success(request, 'Submissão enviada com sucesso!')
        return redirect('app_participante:dashboard_participante')

    # Renderizar o template em caso de GET
    return render(request, 'submissao-de-trabalho.html')
