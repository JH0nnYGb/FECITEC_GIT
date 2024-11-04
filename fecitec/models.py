from django.db import models
from stdimage.models import StdImageField

class Commission(models.Model):
    name = models.CharField(max_length=100)
    formation = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    image = StdImageField(upload_to='photos/', default='photos/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.name