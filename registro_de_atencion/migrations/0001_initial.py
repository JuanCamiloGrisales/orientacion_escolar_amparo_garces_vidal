# Generated by Django 5.0 on 2023-12-15 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consecutivo', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('municipio', models.CharField(blank=True, max_length=500, null=True)),
                ('institucion', models.CharField(blank=True, max_length=500, null=True)),
                ('dane', models.CharField(blank=True, max_length=500, null=True)),
                ('sede', models.CharField(blank=True, max_length=500, null=True)),
                ('remitidoPor', models.TextField(blank=True, null=True)),
                ('posiblesMotivosDeAtencion', models.TextField(blank=True, null=True)),
                ('lineaDeAtencion', models.CharField(blank=True, max_length=500, null=True)),
                ('tipoDeAtencion', models.CharField(blank=True, max_length=500, null=True)),
                ('entidadPrestadoraDeSalud', models.CharField(blank=True, max_length=500, null=True)),
                ('nombreEstudiante', models.CharField(blank=True, max_length=500, null=True)),
                ('tipoDocumentoEstudiante', models.CharField(blank=True, max_length=500, null=True)),
                ('numeroDocumentoEstudiante', models.CharField(blank=True, max_length=500, null=True)),
                ('epsEstudiante', models.CharField(blank=True, max_length=500, null=True)),
                ('fechaNacimientoEstudiante', models.CharField(blank=True, max_length=500, null=True)),
                ('lugarNacimientoEstudiante', models.CharField(blank=True, max_length=500, null=True)),
                ('acudiente', models.CharField(blank=True, max_length=500, null=True)),
                ('telefonoAcudiente', models.CharField(blank=True, max_length=500, null=True)),
                ('documentoAcudiente', models.CharField(blank=True, max_length=500, null=True)),
                ('direccion', models.CharField(blank=True, max_length=500, null=True)),
                ('gradoEscolaridad', models.CharField(blank=True, max_length=500, null=True)),
                ('parentescoAcudiente', models.CharField(blank=True, max_length=500, null=True)),
                ('sexo', models.CharField(blank=True, max_length=500, null=True)),
                ('genero', models.CharField(blank=True, max_length=500, null=True)),
                ('parentesco', models.CharField(blank=True, max_length=500, null=True)),
                ('nombre', models.CharField(blank=True, max_length=500, null=True)),
                ('edad', models.CharField(blank=True, max_length=500, null=True)),
                ('ocupacion', models.CharField(blank=True, max_length=500, null=True)),
                ('nivelEducativo', models.CharField(blank=True, max_length=500, null=True)),
                ('estadoCivil', models.CharField(blank=True, max_length=500, null=True)),
                ('numeroHijos', models.CharField(blank=True, max_length=500, null=True)),
                ('telefono', models.CharField(blank=True, max_length=500, null=True)),
                ('lugarResidencia', models.CharField(blank=True, max_length=500, null=True)),
                ('tipoFamilia', models.CharField(blank=True, max_length=500, null=True)),
                ('espectativasEntrevistado', models.TextField(blank=True, null=True)),
                ('acuerdosPrevios', models.FileField(blank=True, null=True, upload_to='acuerdos_previos/')),
                ('condicionDiscapacidad', models.CharField(blank=True, max_length=500, null=True)),
                ('tipoDiscapacidad', models.CharField(blank=True, max_length=500, null=True)),
                ('talentoYCapacidadesExepcionales', models.TextField(blank=True, null=True)),
                ('relatoEntrevistado', models.TextField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('activacionRuta', models.CharField(blank=True, max_length=500, null=True)),
                ('procesosConvivencia', models.TextField(blank=True, null=True)),
                ('remision', models.FileField(blank=True, null=True, upload_to='remision/')),
                ('piar', models.FileField(blank=True, null=True, upload_to='piar/')),
                ('estadoCaso', models.CharField(blank=True, max_length=500, null=True)),
                ('compromisoPadres', models.FileField(blank=True, null=True, upload_to='compromiso_padres/')),
                ('compromisoEstudiantes', models.FileField(blank=True, null=True, upload_to='compromiso_estudiantes/')),
                ('fechaProximoSeguimiento', models.DateTimeField(blank=True, null=True)),
                ('nombreOrientadora', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
    ]