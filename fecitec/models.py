from django.db import models
from stdimage.models import StdImageField

class Commission(models.Model):
    name = models.CharField(max_length=100)
    formation = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    image = StdImageField(upload_to='photos/', default='photos/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.name
    
class SubmissionToWork(models.Model):
    # Campos de texto
    school_name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    sub_area = models.CharField(max_length=255)
    summary = models.TextField()
    # Campos de seleção
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
    ]
    formation = models.CharField(max_length=20, choices=FORMATION_CHOICES)
    # Campos de arquivo
    arquivo_modelo = models.FileField(upload_to='uploads/modelos/')
    arquivo_panner = models.FileField(upload_to='uploads/panners/')
    def __str__(self):
        return self.title