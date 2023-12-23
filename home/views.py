from django.shortcuts import render, redirect
from django.conf import settings
import os
from registro_de_atencion.models import Registro

# Create your views here.
def home(request):
    registros = Registro.objects.values_list('nombreEstudiante', 'slug').distinct()
    
    context = {'registros': registros,
               'mode': 'Filtrar'}
    
    return render(request, 'home.html', context)

def filter(request, filter='orientacion'):
    if filter == 'orientacion': 
        registros = Registro.objects.filter(lineaDeAtencion='Orientación').values_list('nombreEstudiante', 'slug').distinct()
        mode = 'Orientación'
    elif filter == 'prevencion':
        registros = Registro.objects.filter(lineaDeAtencion='Prevención').values_list('nombreEstudiante', 'slug').distinct()
        mode = 'Prevención'
    elif filter == 'intervencion':
        registros = Registro.objects.filter(lineaDeAtencion='Intervención').values_list('nombreEstudiante', 'slug').distinct()
        mode = 'Intervención'

    context = {'registros': registros,
               'mode': mode}
    
    return render(request, 'home.html', context)


def actualizar(request):

    if request.method == 'POST':
        excel_file = request.FILES['file']
        #Guarda el archivo
        path = os.path.join(settings.BASE_DIR, 'uploads', "estudiantes.xlsx")
        if excel_file.name.endswith('.xlsx'):
            with open(path, 'wb+') as destination:
                for chunk in excel_file.chunks():
                    destination.write(chunk)
        
        return redirect('home')
        

    return render(request, 'actualizar.html')