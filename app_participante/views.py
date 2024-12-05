from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from core.models import Participante

from fecitec.models import SubmissionToWork
from core.models import Participante


# Create your views here.
@login_required
def dash_participante(request):

      participantes = Participante.objects.all()
      print(participantes.values())

      context={
           'participantes':participantes,
      }
      if not request.user.grupos_personalizados.filter(nome='Participante').exists():
          print('views : dash_participante')
          messages.error(request, "Você não tem permissão para acessar esta página.")
      return render(request, 'dashboard_participante.html',context)

    submissions = SubmissionToWork.objects.all()
    participante = Participante.objects.all()
    print(participante.values())

    context = {
        'submissions': submissions,
        'participante': participante,
    }
    
    if not request.user.grupos_personalizados.filter(nome='Participante').exists():
        print('views : dash_participante')
        messages.error(request, "Você não tem permissão para acessar esta página.")
    return render(request, 'dashboard_participante.html', context)





