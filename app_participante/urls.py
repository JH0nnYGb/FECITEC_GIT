from django.urls import path, include
from app_participante.views import dash_participante

app_name = 'app_participante'

urlpatterns = [
    path('dashboard_participante/',dash_participante, name='dashboard_participante'),
]