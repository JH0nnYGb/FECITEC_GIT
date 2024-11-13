from django.urls import path, include
from admin_fecitec.views import admin_dashboard

app_name = 'admin_fecitec'

urlpatterns = [
    path('administrador_dashboard/',admin_dashboard, name='dashboard_admin'),

]