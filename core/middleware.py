from django.shortcuts import redirect
from core.models import GrupoPersonalizado

class VerificarGrupoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            grupo_requerido = self._obter_grupo_requerido(request.path)
            if grupo_requerido:
                if not request.user.grupos_personalizados.filter(nome=grupo_requerido).exists():
                    return redirect('login')  # Ou outra página de acesso negado
        return self.get_response(request)

    def _obter_grupo_requerido(self, path):
        if '/jurado/' in path:
            return 'Jurado'
        elif '/avaliador/' in path:
            return 'Avaliador'
        elif '/administrador/' in path:
            return 'Administrador'
        elif '/participante' in path:
            return 'Participante'
        return None