# Generated by Django 5.1.3 on 2024-12-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fecitec', '0007_submissiontowork_submission_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissiontowork',
            name='status',
            field=models.CharField(choices=[('enviado', 'Enviado'), ('processando', 'Processando'), ('aprovado', 'Aprovado'), ('recusado', 'Recusado')], default='enviado', max_length=20),
        ),
        migrations.AlterField(
            model_name='submissiontowork',
            name='submission_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]