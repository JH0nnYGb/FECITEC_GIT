from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Commission
from .forms import ContactForm
from django.contrib import messages

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

def login(request):
    return render(request, 'login.html')

def formigueiro_view(request):
    return render(request, 'formigueiro.html')