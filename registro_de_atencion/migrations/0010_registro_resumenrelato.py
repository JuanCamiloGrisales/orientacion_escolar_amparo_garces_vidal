# Generated by Django 5.0 on 2024-01-06 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_de_atencion', '0009_remove_registro_acudiente_registro_edadestudiante_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='resumenRelato',
            field=models.TextField(blank=True, null=True),
        ),
    ]