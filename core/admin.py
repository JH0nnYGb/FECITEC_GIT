from django.contrib import admin
from .models import GrupoPersonalizado
from .models import Participante
from .models import Commission
from .models import SubmissionToWork
# Register your models here.


@admin.register(GrupoPersonalizado)
class GrupoPersonalizadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    filter_horizontal = ('usuarios',)  # Facilita a seleção de usuários 
    
@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('id','nome_participante','email_participante','celular',)

@admin.register(Commission)
class ComissionAdmin(admin.ModelAdmin):
    list_display = ('id','name_member', 'email_member', 'phone_member','position_member')

@admin.register(SubmissionToWork)
class SubmissionToWorkAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na listagem
    list_display = ['school_name', 'area', 'municipality', 'title', 'state', 'formation', 'form_of_presentation', 'status', 'formatted_submission_date']
    list_filter = ['state', 'formation']
    search_fields = ['school_name', 'title']

    def formatted_submission_date(self, obj):
        return obj.submission_date.strftime('%d/%m/%Y')
    formatted_submission_date.short_description = 'Data de Submissão'