# data/views.py
import os
from django.shortcuts import render, redirect
import io
from wsgiref.util import FileWrapper
from django.conf import settings
from django.http import HttpResponse
from registro_de_atencion.models import Registro
from django.db.models import Count
from django.utils import timezone
from django.core.management import call_command


def analiticas(request):

    if request.method == 'POST':
        fechaInicio = request.POST.get('fechaInicio')
        fechaInicio = timezone.make_aware(
            timezone.datetime.strptime(fechaInicio, '%Y-%m-%d'))
        fechaFin = request.POST.get('fechaFin')
        fechaFin = timezone.make_aware(
            timezone.datetime.strptime(fechaFin, '%Y-%m-%d'))
        registros = Registro.objects.filter(
            fecha__range=[fechaInicio, fechaFin]).order_by('-fecha', 'gradoEscolaridad')

        context = {
            'lineaDeAtencion': lineaAtencion(fechaInicio, fechaFin),
            'motivoDeAtencion': motivoAtencion(fechaInicio, fechaFin),
            'activacionRuta': activacionRuta(fechaInicio, fechaFin),
            'piar': piar(fechaInicio, fechaFin),
            'estadoCaso': estadoCaso(fechaInicio, fechaFin),
            'registros': registros
        }
    else:
        registros = Registro.objects.all().order_by('-fecha', 'gradoEscolaridad')

        context = {
            'lineaDeAtencion': lineaAtencion(),
            'motivoDeAtencion': motivoAtencion(),
            'activacionRuta': activacionRuta(),
            'piar': piar(),
            'estadoCaso': estadoCaso(),
            'registros': registros
        }

    return render(request, 'analiticas.html', context)


def lineaAtencion(fechaInicio=None, fechaFin=None):
    # Obtener las etiquetas y contar las apariciones de cada una
    if fechaFin:
        conteo_etiquetas = (Registro.objects
                            .filter(fecha__range=[fechaInicio, fechaFin])
                            .values('lineaDeAtencion')
                            .annotate(count=Count('nombreEstudiante', distinct=True))
                            .order_by())
    else:
        conteo_etiquetas = (Registro.objects
                            .values('lineaDeAtencion')
                            .annotate(count=Count('nombreEstudiante', distinct=True))
                            .order_by())
    # Convertir el resultado en un diccionario donde la clave es 'lineaDeAtencion' y el valor es el conteo
    datos = {item['lineaDeAtencion'] if item['lineaDeAtencion']
             else 'No especificado': item['count'] for item in conteo_etiquetas}

    return datos


def motivoAtencion(fechaInicio=None, fechaFin=None):
    # Obtener las etiquetas y contar las apariciones de cada una
    if fechaFin:
        conteo_etiquetas = (Registro.objects
                            .filter(fecha__range=[fechaInicio, fechaFin])
                            .values('posiblesMotivosDeAtencion')
                            .annotate(count=Count('nombreEstudiante', distinct=True))
                            .order_by())
    else:
        conteo_etiquetas = (Registro.objects
                            .values('posiblesMotivosDeAtencion')
                            .annotate(count=Count('nombreEstudiante', distinct=True))
                            .order_by())
    datos = {item['posiblesMotivosDeAtencion'] if item['posiblesMotivosDeAtencion']
             else 'No especificado': item['count'] for item in conteo_etiquetas}

    return datos


def estadoCaso(fechaInicio=None, fechaFin=None):
    # Obtener las etiquetas y contar las apariciones de cada una
    if fechaFin:
        casos_abiertos = Registro.objects.filter(estadoCaso='Abierto', fecha__range=[
                                                 fechaInicio, fechaFin]).values('nombreEstudiante').distinct().count()
        casos_cerrados = Registro.objects.filter(estadoCaso='Cerrado', fecha__range=[
                                                 fechaInicio, fechaFin]).values('nombreEstudiante').distinct().count()
        total_estudiantes = Registro.objects.filter(
            fecha__range=[fechaInicio, fechaFin]).values('nombreEstudiante').distinct().count()

    else:
        casos_abiertos = Registro.objects.filter(estadoCaso='Abierto').values(
            'nombreEstudiante').distinct().count()
        casos_cerrados = Registro.objects.filter(estadoCaso='Cerrado').values(
            'nombreEstudiante').distinct().count()

        total_estudiantes = Registro.objects.values(
            'nombreEstudiante').distinct().count()

    datos = {
        'Casos Abiertos': casos_abiertos,
        'Casos Cerrados': casos_cerrados,
        'Otros Casos': total_estudiantes - casos_abiertos - casos_cerrados
    }

    return datos


def activacionRuta(fechaInicio=None, fechaFin=None):
    # Contar los estudiantes que tienen al menos una 'activacionRuta' asociada
    if fechaFin:
        estudiantes_con_activacion = Registro.objects.filter(
            activacionRuta__isnull=False, fecha__range=[fechaInicio, fechaFin]
        ).values('nombreEstudiante').distinct().count()
        total_estudiantes = Registro.objects.filter(
            fecha__range=[fechaInicio, fechaFin]).values('nombreEstudiante').distinct().count()
    else:
        estudiantes_con_activacion = Registro.objects.filter(
            activacionRuta__isnull=False
        ).values('nombreEstudiante').distinct().count()
        total_estudiantes = Registro.objects.values(
            'nombreEstudiante').distinct().count()

    datos = {
        'Con Activacion': estudiantes_con_activacion,
        'Sin Activacion': total_estudiantes - estudiantes_con_activacion
    }

    return datos


def piar(fechaInicio=None, fechaFin=None):
    # Contar los registros que tienen al menos una 'piar' asociada
    if fechaFin:
        estudiantes_con_piar = Registro.objects.filter(
            piar__isnull=False, fecha__range=[fechaInicio, fechaFin]
        ).values('nombreEstudiante').distinct().count()

        total_estudiantes = Registro.objects.filter(fecha__range=[fechaInicio, fechaFin]).values(
            'nombreEstudiante').distinct().count()
    else:
        estudiantes_con_piar = Registro.objects.filter(
            piar__isnull=False
        ).values('nombreEstudiante').distinct().count()

        total_estudiantes = Registro.objects.values(
            'nombreEstudiante').distinct().count()

    # Preparar los datos de salida
    datos = {
        'Con Piar': estudiantes_con_piar,
        'Sin Piar': total_estudiantes - estudiantes_con_piar
    }

    return datos


def backups(request):

    if request.method == 'POST' and request.FILES:
        try:

            backup_file = request.FILES['backup']
            with open('tmp/' + backup_file.name, 'wb+') as temp_backup_file:
                for chunk in backup_file.chunks():
                    temp_backup_file.write(chunk)

            # Cargamos el archivo de fixture
            call_command('loaddata', temp_backup_file.name)
            try:

                os.remove('tmp/' + backup_file.name)
            except:
                pass

            return render(request, 'backups.html', {'success': 'Base de datos importada correctamente.'})
        except Exception as e:
            return render(request, 'backups.html', {'error': 'Ha habido un error al importar la base de datos, por favor verifica que el archivo sea el correcto. ' + str(e)})

    return render(request, 'backups.html')


def export_database(request):
    response = HttpResponse(content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="backup.json"'

    call_command('dumpdata', stdout=response)

    return response
