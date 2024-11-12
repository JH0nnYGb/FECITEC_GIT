from django.shortcuts import render, redirect
from django.urls import path, include
from app_avaliador.views import avaliador_view

app_name = 'app_avaliador' 

urlpatterns = [
    path('avaliador_dashboard/', avaliador_view , name='dashboard_avaliador')
]