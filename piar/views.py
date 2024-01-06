from django.shortcuts import render, HttpResponse
from registro_de_atencion.files_reader import configurar_estudiantes
from .replacer import reemplazar_valores
from datetime import datetime
import locale
from django.conf import settings
import os
import uuid
from urllib.parse import quote

locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')

# Create your views here.
def piars(request):
    context = {}
    estudiantes = configurar_estudiantes()
    context['alumnos'] = estudiantes

    if request.method == 'POST':
        estudiante = str(request.POST.get('alumno'))
        documento = estudiantes[estudiante]['numero_documento']
        today = datetime.now().strftime("%d de %B del %Y")

        u_id = uuid.uuid4().hex

        file = os.path.join(settings.BASE_DIR, 'piar/doc/PIAR.docx')

        generation_path = os.path.join(settings.BASE_DIR, f'piar/gen/PIAR_{estudiante}.docx')

        replace = {
            '{fecha}': today,
            '{nombre}': str(estudiante).title(),
            '{documento}': str(documento),
            '{grado}': str(estudiantes[estudiante]['grado_escolaridad']),
        }

        docx_to_download = reemplazar_valores(file, replace, generation_path)
        filename = f'PIAR_{estudiante}.docx'

        with open(docx_to_download, 'rb') as f:
            # Crea una respuesta con el contenido del archivo
            response = HttpResponse(f.read(), content_type="application/octet-stream")
            # Establece el encabezado 'Content-Disposition' para indicar que es una descarga
            response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(quote(filename))
            
            # Devuelve la respuesta
            return response
    
    return render(request, 'piars.html', context)