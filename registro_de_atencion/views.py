from django.shortcuts import render
from django.conf import settings
import csv
import os
import pandas as pd

# Create your views here.


def FormularioDeRegistroDeAtencion(request):
    context = {}
    try:
        # Configuración municipios
        csv_municipios = os.path.join(
            settings.BASE_DIR, 'uploads/municipios.csv')
        municipios = []

        with open(csv_municipios, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                municipios.append(row['MUNICIPIO'])

        context['municipios'] = municipios

        # Configuración Estudiantes
        excel_alumnos_path = os.path.join(
            settings.BASE_DIR, 'uploads/estudiantes.xlsx')
        try:
            excel_alumnos = pd.read_excel(excel_alumnos_path)
        except FileNotFoundError:
            raise Exception(f'Archivo {excel_alumnos_path} no encontrado.')
        except pd.errors.EmptyDataError:
            raise Exception(
                f'Archivo {excel_alumnos_path} está vacío o con formato incorrecto.')

        alumnos = {}

        for fila in excel_alumnos.iterrows():
            nombre1 = fila[1]['NOMBRE1'] if pd.notna(
                fila[1]['NOMBRE1']) else ''
            nombre2 = fila[1]['NOMBRE2'] if pd.notna(
                fila[1]['NOMBRE2']) else ''
            apellido1 = fila[1]['APELLIDO1'] if pd.notna(
                fila[1]['APELLIDO1']) else ''
            apellido2 = fila[1]['APELLIDO2'] if pd.notna(
                fila[1]['APELLIDO2']) else ''

            nombre_completo = " ".join(
                filter(None, [nombre1, nombre2, apellido1, apellido2]))

            tipo_documento = fila[1]['TIPODOC'] if pd.notna(
                fila[1]['TIPODOC']) else ''
            numero_documento = fila[1]['DOC'] if pd.notna(
                fila[1]['DOC']) else ''
            eps = fila[1]['EPS'] if pd.notna(fila[1]['EPS']) else ''
            fecha_nacimiento = fila[1]['FECHA_NACIMIENTO'] if pd.notna(
                fila[1]['FECHA_NACIMIENTO']) else ''
            lugar_nacimiento = fila[1]['PAIS_ORIGEN'] if pd.notna(
                fila[1]['PAIS_ORIGEN']) else ''
            barrio = fila[1]['BARRIO'] if pd.notna(fila[1]['BARRIO']) else ''

            alumnos[nombre_completo] = {
                'tipo_documento': tipo_documento,
                'numero_documento': numero_documento,
                'eps': eps,
                'fecha_nacimiento': fecha_nacimiento,
                'lugar_nacimiento': lugar_nacimiento,
                'barrio': barrio,
            }

        context['alumnos'] = alumnos

    except Exception as e:
        # Puedes optar por enviar un mensaje de error en el contexto o redirigir a una vista de error
        context['error'] = 'Ocurrió un error al procesar los archivos de registro.'

    return render(request, 'form.html', context)
