from django.urls import path, include
from admin_fecitec.views import views_admin_dashboard
from django.contrib.auth.views import LogoutView

from admin_fecitec.views import views_admin_submission
from admin_fecitec.views import views_admin_jurors
from admin_fecitec.views import views_add_members
from admin_fecitec.views import views_admin_evaluators
from admin_fecitec.views import views_admin_reviews
from admin_fecitec.views import views_admin_participants
from admin_fecitec.views import views_admin_commission
from admin_fecitec.views import viewa_admin_contacts


app_name = 'admin_fecitec'

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        # Sobrescrevendo para aceitar o método GET
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('administrador_dashboard/',views_admin_dashboard, name='dashboard_admin'),
    path('logout/', CustomLogoutView.as_view(next_page='fecitec:user_login'), name='logout'),
    path('administracao-submissoes/', views_admin_submission, name='admin_submission'),
    path('administracao-jurados/', views_admin_jurors, name="admin_jurors"),
    path('administracao-add-jurados', views_add_members, name='admin_add_member'),
    path('administracao-avaliadores/', views_admin_evaluators, name='admin_evaluators'),
    path('administracao-avaliaçoes/', views_admin_reviews, name="admin_reviews" ),
    path('administracao-participantes/', views_admin_participants, name="admin_participants"),
    path('administracao-comissao/', views_admin_commission, name="admin_commission"),
    path('administracao-contados/', viewa_admin_contacts, name="admin_contacts"),

]