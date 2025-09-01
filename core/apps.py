from django.apps import AppConfig
from django.db.models.signals import post_migrate

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from .models import GroupsFecitec
        post_migrate.connect(creat_grupo_defalt, sender=self)


def creat_grupo_defalt(sender, **kwargs):
    from .models import GroupsFecitec

    grups_defalt = ['Administrador', 'Jurado', 'Avaliador', 'Participante']
    for group_name in grups_defalt:
        GroupsFecitec.objects.get_or_create(namegroup=group_name)
