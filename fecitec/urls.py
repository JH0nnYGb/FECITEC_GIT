from django.urls import path
from . import views
from fecitec.views import home_view
from fecitec.views import cronograma_view
from fecitec.views import submissao_view
from fecitec.views import aprovados_view
from fecitec.views import certificados_view
from fecitec.views import regulamento_view
from fecitec.views import comissao_view
from fecitec.views import contate_view
from fecitec.views import user_login
from fecitec.views import formigueiro_view

app_name = 'fecitec'

urlpatterns = [
    path('', home_view, name='home'),
    path('cronograma/', cronograma_view, name='cronograma'),
    path('submissao/', submissao_view, name='submissao'),
    path('aprovados/', aprovados_view, name='aprovados'),
    path('certificados/', certificados_view, name='certificados'),
    path('regulamento/', regulamento_view, name='regulamento'),
    path('comissao/', comissao_view, name='comissao'),
  
    path('contate-nos/', contate_view, name='contate'),
    path('login/', user_login, name='user_login'),

    path('formigueiro', formigueiro_view, name='formigueiro')
]