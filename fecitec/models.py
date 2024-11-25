from django.db import models
from stdimage.models import StdImageField

class Commission(models.Model):
    name = models.CharField(max_length=100)
    formation = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    image = StdImageField(upload_to='photos/', default='photos/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.name
    
 # FUNCAO PARA CRIAR UM CONTA COMO PARTICIPANTE 
class Participante(models.Model):
    nome_completo = models.CharField(max_length=100, verbose_name="Nome Completo")
    email = models.EmailField(unique=True, verbose_name="E-mail")
    username = models.CharField(max_length=50, unique=True, verbose_name="Nome de Usuário")
    senha = models.CharField(max_length=128, verbose_name="Senha")
    celular = models.CharField(max_length=15, verbose_name="Celular")
    endereco = models.TextField(verbose_name="Endereço")
    cidade = models.CharField(max_length=50, verbose_name="Cidade")
    bairro = models.CharField(max_length=50, verbose_name="Bairro")
    estado = models.CharField(max_length=2, verbose_name="Estado (UF)")
    formacao_academica = models.CharField(max_length=100, verbose_name="Formação Acadêmica")

    def __str__(self):
        return self.nome_completo
#FIM FUNCAO PARA CRIAR UM CONTA COMO PARTICIPANTE