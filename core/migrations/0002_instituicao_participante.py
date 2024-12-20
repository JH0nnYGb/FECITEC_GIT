# Generated by Django 5.1.2 on 2024-11-26 14:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('municipio', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_instituicao', models.CharField(max_length=255)),
                ('municipio', models.CharField(max_length=100)),
                ('estado_instituicao', models.CharField(max_length=2)),
                ('endereco', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=15)),
                ('bairro', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('formacao', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='participante', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
