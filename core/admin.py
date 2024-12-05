from django.contrib import admin
from .models import GrupoPersonalizado
from .models import Participante
# Register your models here.


@admin.register(GrupoPersonalizado)
class GrupoPersonalizadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    filter_horizontal = ('usuarios',)  # Facilita a seleção de usuários 
    
@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome_participante','email_participante','celular',)