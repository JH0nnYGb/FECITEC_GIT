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
    
### models do participante fecitec ######
class Participante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='participante')
    nome_instituicao = models.CharField(max_length=255)
    municipio = models.CharField(max_length=100)
    estado_instituicao = models.CharField(max_length=2)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)
    bairro = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    formacao = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.first_name} - {self.nome_instituicao}"
    
###### models de instituicao ####
class Instituicao(models.Model):
    nome_instituicao = models.CharField(max_length=255)
    municipio = models.CharField(max_length=100)
    estado_instituicao = models.CharField(max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self. instituicao_nome