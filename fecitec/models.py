from django.db import models
from stdimage.models import StdImageField

class Commission(models.Model):
    name = models.CharField(max_length=100)
    formation = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    image = StdImageField(upload_to='fecitec/static/images')

    def __str__(self):
        return self.name