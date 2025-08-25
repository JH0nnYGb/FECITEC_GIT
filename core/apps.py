from django.apps import AppConfig
from django.db.models.signals import post_migrate

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from .models import GruposFecitec
        post_migrate.connect(criar_grupos_padrao, sender=self)


def criar_grupos_padrao(sender, **kwargs):
    from .models import GruposFecitec

    grupos_padrao = ['Administrador', 'Jurado', 'Avaliador', 'Participante']
    for grupo_nome in grupos_padrao:
        GruposFecitec.objects.get_or_create(nome=grupo_nome)
