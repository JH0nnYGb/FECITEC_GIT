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
    ESTADOS_CHOICES = [
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
    ]

    FORMACAO_CHOICES = [
        ('Fundamental - Incompleto', 'Fundamental - Incompleto'),
        ('Fundamental - Completo', 'Fundamental - Completo'),
        ('Médio - Incompleto', 'Médio - Incompleto'),
        ('Médio - Completo', 'Médio - Completo'),
        ('Superior - Incompleto', 'Superior - Incompleto'),
        ('Superior - Completo', 'Superior - Completo'),
        ('Pós-graduação (Lato sensu) - Incompleto', 'Pós-graduação (Lato sensu) - Incompleto'),
        ('Pós-graduação (Lato sensu) - Completo', 'Pós-graduação (Lato sensu) - Completo'),
        ('Pós-graduação (Stricto sensu, nível mestrado) - Incompleto', 'Pós-graduação (Stricto sensu, nível mestrado) - Incompleto'),
        ('Pós-graduação (Stricto sensu, nível mestrado) - Completo', 'Pós-graduação (Stricto sensu, nível mestrado) - Completo'),
        ('Pós-graduação (Stricto sensu, nível doutor) - Incompleto', 'Pós-graduação (Stricto sensu, nível doutor) - Incompleto'),
        ('Pós-graduação (Stricto sensu, nível doutor) - Completo', 'Pós-graduação (Stricto sensu, nível doutor) - Completo'),
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='participante')
    nome_participante = models.CharField(max_length=50)
    email_participante = models.EmailField(max_length=200)
    municipio = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)
    bairro = models.CharField(max_length=100)
    estado_participante = models.CharField(max_length=2, choices=ESTADOS_CHOICES, default='BA')
    formacao_participante =  models.CharField(max_length=60, choices=FORMACAO_CHOICES, default='Médio - Completo')
#   DADOS INTITUICAO   #
    instituicao = models.ForeignKey('Instituicao', on_delete=models.CASCADE, related_name='participantes')

    def __str__(self):
        return f"{self.user.first_name} - {self.instituicao.instituicao_nome}"
    
###### models de instituicao ####
class Instituicao(models.Model):
    ESTADOS_CHOICES = [
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
    ]


    instituicao_nome = models.CharField(max_length=255)
    municipio = models.CharField(max_length=100)
    estado_instituicao = models.CharField(max_length=2, choices=ESTADOS_CHOICES,default='BA')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self. instituicao_nome