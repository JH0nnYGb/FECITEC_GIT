# Generated by Django 5.1.3 on 2024-12-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fecitec', '0008_submissiontowork_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissiontowork',
            name='formation',
            field=models.CharField(choices=[('EnsinoFundamental', 'Ensino Fundamental'), ('EnsinoMedio', 'Ensino Médio'), ('subsequente', 'Subsequente')], max_length=100),
        ),
    ]
