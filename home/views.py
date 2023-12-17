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
        registros = Registro.objects.filter(lineaDeAtencion='Orientación').values_list('nombreEstudiante', flat=True).distinct()
        mode = 'Orientación'
    elif filter == 'prevencion':
        registros = Registro.objects.filter(lineaDeAtencion='Prevención').values_list('nombreEstudiante', flat=True).distinct()
        mode = 'Prevención'
    elif filter == 'intervencion':
        registros = Registro.objects.filter(lineaDeAtencion='Intervención').values_list('nombreEstudiante', flat=True).distinct()
        mode = 'Intervención'

    context = {'registros': registros,
               'mode': mode}
    
    return render(request, 'home.html', context)


"""
Dear ChatGPT,

I am in need of your assistance to summarize various texts that are written in Spanish. Your task is to provide concise summaries, encapsulating the core message or main points of each text. It is crucial that your summaries are limited to a maximum of two lines to ensure brevity, while still conveying the essence of the text.

Your responses must be written in Spanish, regardless of the fact that this prompt is in English. This is to cater to an audience that prefers summaries in Spanish.

At the end of each text I provide, you will find a clear indication that marks the beginning of the section you need to summarize. Look for the phrase "Here's the text to summarize:" immediately followed by the Spanish text.

Please adhere to the following guidelines when creating your summaries:

Read the provided Spanish text thoroughly to understand the key themes and messages.
Craft a summary that is no longer than two lines, capturing the essence of the text in a succinct manner.
Ensure that the summary is written in Spanish, using appropriate grammar and vocabulary.
Maintain the original tone and intent of the text, whether it is formal, informal, persuasive, descriptive, etc.
Thank you for your help with this task. Your ability to distill information into concise summaries is greatly appreciated. Here's an example to demonstrate what I'm looking for:

Here's the text to summarize: "La importancia del reciclaje no puede ser subestimada. Contribuye a la conservación de recursos, la reducción de la contaminación y la mejora del medio ambiente para las generaciones futuras."

Your summary in Spanish: "El reciclaje es vital para conservar recursos, reducir contaminación y proteger el ambiente."

Now, let's proceed with the actual texts.

Here's the text to summarize:
"""

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