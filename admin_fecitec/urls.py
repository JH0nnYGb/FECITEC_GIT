from django.urls import path, include
from admin_fecitec.views import admin_dashboard
from django.contrib.auth.views import LogoutView


app_name = 'admin_fecitec'

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        # Sobrescrevendo para aceitar o método GET
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('administrador_dashboard/',admin_dashboard, name='dashboard_admin'),
    path('logout/', CustomLogoutView.as_view(next_page='fecitec:user_login'), name='logout'),
]