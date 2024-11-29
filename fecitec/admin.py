from django.contrib import admin
from .models import Commission
from .models import SubmissionToWork

@admin.register(Commission)
class ComissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'formation', 'position')

@admin.register(SubmissionToWork)
class SubmissionToWorkAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na listagem
    list_display = ['school_name', 'area', 'municipality', 'title', 'state', 'formation']
    list_filter = ['state', 'formation']
    search_fields = ['school_name', 'title']