from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from registro_de_atencion.files_reader import configurar_estudiantes
from .replacer import reemplazar_valores
from datetime import datetime
import locale
from django.conf import settings
import os
from urllib.parse import quote
from .models import Piar
from django.core.files import File
from django.urls import reverse

locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')

# Create your views here.
def piars(request):
    context = {}
    estudiantes = configurar_estudiantes()
    context['alumnos'] = estudiantes

    if request.method == 'POST':
        estudiante = str(request.POST.get('alumno'))
        try:

            documento = estudiantes[estudiante]['numero_documento']
            today = datetime.now().strftime("%d de %B del %Y")

            file = os.path.join(settings.BASE_DIR, 'piar/doc/PIAR.docx')

            if Piar.objects.exists():
                consecutivo = Piar.objects.filter(alumno=estudiante).count() + 1
            else:
                consecutivo = 1

            generation_path = os.path.join(settings.BASE_DIR, f'piar/gen/PIAR_{estudiante}_{consecutivo}.docx')

            replace = {
                '{fecha}': today,
                '{nombre}': str(estudiante).title(),
                '{documento}': str(documento),
                '{grado}': str(estudiantes[estudiante]['grado_escolaridad']),
            }

            docx_to_download = reemplazar_valores(file, replace, generation_path)
            filename = f'PIAR_{estudiante}_{consecutivo}.docx'

            # Crea una instancia del modelo Piar
            piar_instance = Piar(alumno=estudiante, archivo=None)
            # Guarda la instancia sin el archivo para poder asignarle un nombre de archivo
            piar_instance.save()

            # Abre el archivo generado y lo asigna al modelo
            with open(docx_to_download, 'rb') as f:
                piar_instance.archivo.save(filename, File(f), save=True)
                f.seek(0)
                # Crea una respuesta con el contenido del archivo para la descarga
                response = HttpResponse(f.read(), content_type="application/octet-stream")
                # Establece el encabezado 'Content-Disposition' para indicar que es una descarga
                response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(quote(filename))
                # Cierra el archivo 
                f.close()
                os.remove(docx_to_download)
                # Devuelve la respuesta
                return response
        except Exception as e:
            return render(request, '400.html', {'message': f'Error al generar el archivo, por favor verifica que <strong>"{estudiante}"</strong> se encuentre en la lista desplegable. Si el problema persiste, contacta al administrador.'})

    archivos = Piar.objects.values_list('alumno', 'slug').distinct().order_by('alumno')
    context['piars'] = archivos

    return render(request, 'piars.html', context)

def detailed_piar(request, slug):
    piars = Piar.objects.filter(slug=slug)
    first_item = piars.first()
    if not piars:
        return HttpResponse('No se encontró el Piar con el slug proporcionado.', status=404)

    if request.method == 'POST':
        # Asegúrate de que el formulario incluye tanto el campo 'alumno' como el archivo 'new_piar'
        alumno = request.POST.get('alumno')
        new_piar_file = request.FILES.get('new_piar')
        if alumno and new_piar_file:
            new_object = Piar.objects.create(alumno=alumno, archivo=new_piar_file)
            return redirect(reverse('detailed_piar', kwargs={'slug': new_object.slug}))
        else:
            return HttpResponse('Datos del formulario incompletos.', status=400)

    context = {'piars': piars,
               'first': first_item}
    return render(request, 'detailed_piar.html', context)

def delete_piar(request, id):
    piar = get_object_or_404(Piar, id=id)
    slug = piar.slug
    piar.delete()
    return redirect('detailed_piar', slug)