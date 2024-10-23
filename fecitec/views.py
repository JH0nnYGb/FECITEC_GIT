from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')


def aprovados_view(request):
    return render(request, 'aprovado.html')