# Generated by Django 5.0 on 2024-01-02 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor_formulario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editarcampos',
            name='activacionRuta',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='condicionDiscapacidad',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='dane',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='entidadPrestadoraDeSalud',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='espectativasEntrevistado',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='estadoCaso',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='estadoCivil',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='genero',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='gradoEscolaridad',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='hogarYBienestar',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='institucion',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='lineaDeAtencion',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='lugarNacimientoEstudiante',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='municipio',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='nivelEducativo',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='nombreOrientadora',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='nombreRemitidoPor',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='observaciones',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='ocupacion',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='parentesco',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='parentescoAcudiente',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='posiblesMotivosDeAtencion',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='procesosConvivencia',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='relatoEntrevistado',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='remitidoPor',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='sede',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='sexo',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='talentoYCapacidadesExepcionales',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='tipoDeAtencion',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='tipoDiscapacidad',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='tipoDocumentoEstudiante',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
        migrations.AlterField(
            model_name='editarcampos',
            name='tipoFamilia',
            field=models.JSONField(default={'default': '', 'opciones': '[]'}),
        ),
    ]