from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from stdimage.models import StdImageField

from django.contrib.postgres.fields import ArrayField  # Se estiver usando PostgreSQL


class GroupsFecitec(models.Model):
    namegroup = models.CharField(max_length=50, unique=True, verbose_name="Nome do Grupo")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    usuarios = models.ManyToManyField(User, related_name='grupos_fecitec', blank=True)
    
    def __str__(self):
        return self.namegroup
    
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
    municipio_participante = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    cep_pacticipante = models.CharField(max_length=200)
    celular = models.CharField(max_length=15)
    bairro = models.CharField(max_length=100)
    estado_participante = models.CharField(max_length=2, choices=ESTADOS_CHOICES, default='BA')
    formacao_participante =  models.CharField(max_length=60, choices=FORMACAO_CHOICES, default='Médio - Completo')
    # image = StdImageField(upload_to='photos/', default='photos/default.jpg', blank=True, null=True)

    def __str__(self):
        
        return f"{self.user.first_name} - {self.email_participante}"
    
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
        return self.instituicao_nome
    

class Commission(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member_commission')
    name_member = models.CharField(max_length=100)
    email_member = models.EmailField(max_length=100)
    phone_member = models.CharField(
        max_length=15,
        null = False,
        blank= False
    )
    formation_member = models.CharField(max_length=100)
    position_member = models.JSONField(default=list)
    member_profile = StdImageField(upload_to='photos/', default='photos/default.jpg', blank=True, null=True)
    
    def __str__(self):
        return self.name_member
 
# MODELS DOS TRABALHOS 
class SubmissionToWork(models.Model):

    school_name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    sub_area = models.CharField(max_length=255)
    summary = models.TextField()
    participante = models.ForeignKey(
        Participante,
        on_delete=models.CASCADE,
        related_name='submissions'
    )
    evaluators = models.ManyToManyField(
        "Commission",
        related_name="trabalhos_avaliados",
        blank=True
    )
    

    STATE_CHOICES = [
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
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    
    FORMATION_CHOICES = [
        ('EnsinoFundamental', 'Ensino Fundamental'),
        ('EnsinoMedio', 'Ensino Médio'),
        ('subsequente', 'Subsequente'),
    ]

    FORM_OF_PRESENTATION = [
        ('Exposicao', 'Exposição'),
        ('Painel', 'Painel'),
        ('Maquete', 'Maquete'),
        ('Outro', 'Outro'),
    ]

    formation = models.CharField(max_length=100, choices=FORMATION_CHOICES)
    form_of_presentation = models.CharField(max_length=100, choices=FORM_OF_PRESENTATION)
    
    # Campos de arquivo
    arquivo_modelo = models.FileField(upload_to='uploads/modelos/')

    # Campo para capturar a data da submissão de forma automática
    submission_date = models.DateField(auto_now_add=True)  # Campo que captura a data automaticamente

    STATUS_CHOICES = [
        ('enviado', 'Enviado'),
        ('processando', 'Processando'),
        ('aprovado', 'Aprovado'),
        ('recusado', 'Recusado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='enviado')

    def __str__(self):
        return self.title
    
#MODELS PARA RELAÇÃO DE TRABALHOS SORTEADOS COM SEUS MEMBROS
class JurorAssignment(models.Model):
    juror = models.ForeignKey(Commission, on_delete=models.CASCADE,related_name="assignments")
    work = models.ForeignKey(SubmissionToWork, on_delete=models.CASCADE,related_name="assignments")
    assignments_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.juror.name_member} - {self.work.title}"