from django.shortcuts import render, redirect, get_object_or_404
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
        return redirect('fecitec:login_participante')  # Redirecione para uma página apropriada

    # Recupera as submissões (caso sejam gerais ou específicas do participante)
    submissions = SubmissionToWork.objects.filter(participante=participante)

    # Verifica permissões
    if not request.user.grupos_personalizados.filter(nome='Participante').exists():
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('fecitec:login_participante')

    # Contexto enviado para o template
    context = {
        'participante': participante,
        'submissions': submissions,
    }
    return render(request, 'dashboard_participante.html', context)

def submissao_trabalho(request):
    if request.method == 'POST':
        school_name = request.POST.get('school_name')
        area = request.POST.get('area')
        state = request.POST.get('state')
        municipality = request.POST.get('municipality')
        formation = request.POST.get('formation')
        form_of_presentation = request.POST.get('formOfPresentation')
        title = request.POST.get('title')
        sub_area = request.POST.get('sub_area')
        summary = request.POST.get('summary')
        arquivo_modelo = request.FILES.get('arquivo_modelo')

        try:
            nome_participante = Participante.objects.get(user=request.user)
        except Participante.DoesNotExist:
            messages.error(request, "Participante não encontrado.")
            return redirect('app_participante:dashboard_participante')
        
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
            participante=nome_participante
        )

        messages.success(request, 'Submissão enviada com sucesso!')
        return redirect('app_participante:submissao_de_trabalho')

    return render(request, 'submissao-de-trabalho.html')

def editar_submissao(request, submission_id):
    submission = get_object_or_404(SubmissionToWork, id=submission_id)

    if request.method == 'POST':
        submission.school_name = request.POST.get('school_name')
        submission.area = request.POST.get('area')
        submission.state = request.POST.get('state')
        submission.formation = request.POST.get('formation')
        submission.form_of_presentation = request.POST.get('formOfPresentation')
        submission.municipality = request.POST.get('municipality')
        submission.title = request.POST.get('title')
        submission.sub_area = request.POST.get('sub_area')
        submission.summary = request.POST.get('summary')

        if 'arquivo_modelo' in request.FILES:
            submission.arquivo_modelo = request.FILES['arquivo_modelo']
        submission.save()

        # Redireciona para o dashboard
        return redirect('app_participante:dashboard_participante')

    # Renderiza a página com os dados da submissão
    return render(request, 'editar_submissao.html', {
        'submission': submission,
    })