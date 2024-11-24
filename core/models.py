from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class GrupoPersonalizado(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name="Nome do Grupo")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    usuarios = models.ManyToManyField(User, related_name='grupos_personalizados', blank=True)

    def __str__(self):
        return self.nome
    
