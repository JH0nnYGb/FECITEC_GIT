from django.urls import path, include
from django.contrib.auth.views import LogoutView
from app_participante.views import dash_participante
from app_participante.views import submissao_trabalho

app_name = 'app_participante'

# classe parafazer logout no usuario atual 
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        # Sobrescrevendo para aceitar o método GET
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('dashboard_participante/',dash_participante, name='dashboard_participante'),
    path('submissao_de_trabalho/', submissao_trabalho, name='submissao_de_trabalho'),
    path('logout-participante/', CustomLogoutView.as_view(next_page='fecitec:home'), name='logout_participante')
]