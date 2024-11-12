from django.urls import path, include
from app_jurado.views import dash_jurado

app_name = 'app_jurado'

urlpatterns = [
    path('jurado_dashboard/', dash_jurado, name='dashboard_jurado')
]