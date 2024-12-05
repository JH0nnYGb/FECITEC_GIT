from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import Participante
from fecitec.models import SubmissionToWork

@login_required
def dash_participante(request):
<<<<<<< HEAD
      participantes = Participante.objects.all()
      print(participantes.values())

      context={
           'participantes':participantes
      }
      if not request.user.grupos_personalizados.filter(nome='Participante').exists():
          print('views : dash_participante')
          messages.error(request, "Você não tem permissão para acessar esta página.")
      return render(request, 'dashboard_participante.html',context)

=======
    try:
        # Recupera o participante associado ao usuário logado
        participante = Participante.objects.get(user=request.user)
    except Participante.DoesNotExist:
        messages.error(request, "Participante não encontrado.")
        return redirect('alguma_url_de_erro')  # Redirecione para uma página apropriada
>>>>>>> 19c5221029820f937810712a4fb1b023efb25c5d

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
