# Generated by Django 5.0 on 2024-01-08 22:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piar', '0002_piar_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='piar',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
