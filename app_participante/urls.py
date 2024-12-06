from django.urls import path, include
from app_participante.views import dash_participante
from app_participante.views import submissao_trabalho

app_name = 'app_participante'

urlpatterns = [
    path('dashboard_participante/',dash_participante, name='dashboard_participante'),
    path('submissao_de_trabalho/', submissao_trabalho, name='submissao_de_trabalho')
]