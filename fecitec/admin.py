from django.contrib import admin
from .models import Commission

@admin.register(Commission)
class ComissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'formation', 'position')