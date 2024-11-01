from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def cronograma_view(request):
    return render(request, 'cronograma.html')

def submissao_view(request):
    return render(request, 'submissao.html')

def aprovados_view(request):
    return render(request, 'aprovado.html')

def certificados_view(request):
    return render(request, 'certificados02.html')

def regulamento_view(request):
    return render(request, 'regulamento.html')

def comissao_view(request):
    return render(request, 'comissao.html')

def contate_view(request):
    return render(request, 'contate.html')

def login(request):
    return render(request, 'login.html')