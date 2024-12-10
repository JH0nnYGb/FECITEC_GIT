from django.contrib import admin
from .models import SubmissionToWork



@admin.register(SubmissionToWork)
class SubmissionToWorkAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na listagem
    list_display = ['school_name', 'area', 'municipality', 'title', 'state', 'formation', 'formOfPresentation', 'status', 'formatted_submission_date']
    list_filter = ['state', 'formation']
    search_fields = ['school_name', 'title']

    def formatted_submission_date(self, obj):
        return obj.submission_date.strftime('%d/%m/%Y')
    formatted_submission_date.short_description = 'Data de Submissão'