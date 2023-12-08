from django.shortcuts import render
from django.conf import settings
import csv
import os

# Create your views here.
def FormularioDeRegistroDeAtencion(request):
    csv_municipios = os.path.join(settings.BASE_DIR, 'uploads/municipios.csv')
    municipios = []

    with open(csv_municipios, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            municipios.append(row['MUNICIPIO'])

    context = {'municipios': municipios}
    
    return render(request, 'form.html', context)