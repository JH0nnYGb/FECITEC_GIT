from django.urls import path, include
from app_participante .views import dash_participante

app_name = 'app_participante'

urlpatterns = [
    path('participante_dashboard/', dash_participante, name='dashboard_participante')
]