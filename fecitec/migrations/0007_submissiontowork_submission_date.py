# Generated by Django 5.1.3 on 2024-12-05 12:21

from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('fecitec', '0006_submissiontowork_formofpresentation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissiontowork',
            name='submission_date',
            field=models.DateTimeField(default=timezone.now, auto_now_add=True),
            preserve_default=False,
        ),
    ]