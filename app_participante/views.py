from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import Participante
from fecitec.models import SubmissionToWork
from fecitec.forms import SubmissionToWorkForm

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

    return render(request, 'submissao-de-trabalho.html', context)  # Sempre retorna o contexto