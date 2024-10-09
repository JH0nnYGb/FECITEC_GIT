from django.urls import path
from fecitec.views import home_view
from fecitec.views import aprovados_view

urlpatterns = [
    path('', home_view, name='home'),
    path('/aprovados',aprovados_view, name='aprovados')
]