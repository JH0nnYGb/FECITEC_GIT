<<<<<<< HEAD
# Generated by Django 5.1.2 on 2024-10-31 12:34
=======
# Generated by Django 5.1.2 on 2024-10-31 11:56
>>>>>>> 15e2bd9cd96e6bf5d2d7c2840e8d0039898eafba

import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('formation', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
<<<<<<< HEAD
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='', variations={})),
=======
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='colaboradores', variations={}, verbose_name='Imagem')),
>>>>>>> 15e2bd9cd96e6bf5d2d7c2840e8d0039898eafba
            ],
        ),
    ]