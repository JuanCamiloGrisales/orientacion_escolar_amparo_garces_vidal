# Generated by Django 5.0 on 2024-01-01 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EditarCampos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.JSONField(default=dict)),
                ('institucion', models.JSONField(default=dict)),
                ('dane', models.JSONField(default=dict)),
                ('sede', models.JSONField(default=dict)),
                ('remitidoPor', models.JSONField(default=dict)),
                ('nombreRemitidoPor', models.JSONField(default=dict)),
                ('posiblesMotivosDeAtencion', models.JSONField(default=dict)),
                ('lineaDeAtencion', models.JSONField(default=dict)),
                ('tipoDeAtencion', models.JSONField(default=dict)),
                ('entidadPrestadoraDeSalud', models.JSONField(default=dict)),
                ('tipoDocumentoEstudiante', models.JSONField(default=dict)),
                ('gradoEscolaridad', models.JSONField(default=dict)),
                ('lugarNacimientoEstudiante', models.JSONField(default=dict)),
                ('parentescoAcudiente', models.JSONField(default=dict)),
                ('sexo', models.JSONField(default=dict)),
                ('genero', models.JSONField(default=dict)),
                ('parentesco', models.JSONField(default=dict)),
                ('ocupacion', models.JSONField(default=dict)),
                ('nivelEducativo', models.JSONField(default=dict)),
                ('estadoCivil', models.JSONField(default=dict)),
                ('tipoFamilia', models.JSONField(default=dict)),
                ('hogarYBienestar', models.JSONField(default=dict)),
                ('espectativasEntrevistado', models.JSONField(default=dict)),
                ('condicionDiscapacidad', models.JSONField(default=dict)),
                ('tipoDiscapacidad', models.JSONField(default=dict)),
                ('talentoYCapacidadesExepcionales', models.JSONField(default=dict)),
                ('relatoEntrevistado', models.JSONField(default=dict)),
                ('observaciones', models.JSONField(default=dict)),
                ('activacionRuta', models.JSONField(default=dict)),
                ('procesosConvivencia', models.JSONField(default=dict)),
                ('estadoCaso', models.JSONField(default=dict)),
                ('nombreOrientadora', models.JSONField(default=dict)),
            ],
            options={
                'verbose_name': 'Editar Campos',
                'verbose_name_plural': 'Editar Campos',
            },
        ),
    ]