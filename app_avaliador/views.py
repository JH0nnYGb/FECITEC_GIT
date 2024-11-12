from django.shortcuts import render


# Create your views here.

def avaliador_view (request):
    return render ( request, 'dashboard_avaliador.html')