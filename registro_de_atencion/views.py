from django.shortcuts import render, redirect
import locale
from .forms import RegistroForm
from .files_reader import configurar_municipios, configurar_estudiantes
from .models import Registro
from usellm import Message, Options, UseLLM

locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')
service = UseLLM(service_url="https://usellm.org/api/llm")

mensaje_base = f"""You are an AI trained to summarize texts efficiently. Your task is to provide concise summaries of Spanish texts. When you receive a text, you must read it carefully and distill the information into its most essential points.

Your summaries should be no longer than two lines, capturing the core message or narrative of the text. It is crucial that you maintain the original meaning and context while being succinct. You must also respond in Spanish, regardless of the language the instructions are given in.

Remember, your goal is to provide a clear and concise summary that allows anyone to understand the gist of the text without needing to read the entire piece. Precision and brevity are key. The text is always about observations made by psychologists in the context of scholarly orientation, don't focus on the "note" and "personal data protection policy" terms, just the main text below.

Here's the text to summarize, write your answer in Spanish:"""

def FormularioDeRegistroDeAtencion(request):
    context = {}
    context['envio'] = 'form'

    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():

            registro = form.save(commit=False)

            registro.form_data = request.POST

            try:
                observaciones = str(request.POST.get('observaciones', ''))

                mensaje = f"{mensaje_base} {observaciones}"

                messages = [
                    Message(role="user", content=mensaje),
                ]

                options = Options(messages=messages)
                response = service.chat(options)

                registro.resumen = response.content
            
            except:
                registro.resumen = ''
            
            registro.save()

            context['success'] = 'Registro guardado correctamente.'
            return render(request, 'form/form.html', context)
        

    # Configuración de valores por defecto
    try:
        municipios = configurar_municipios()
        context['municipios'] = municipios
        
        estudiantes = configurar_estudiantes()
        context['alumnos'] = estudiantes

    except Exception as e:
        context['error'] = 'Ocurrió un error al procesar los valores por defecto.'

    # ------------------------------------
    return render(request, 'form/form.html', context)

def Alumno(request, alumno):
    
    registros = Registro.objects.filter(slug=alumno)
    slug = alumno
    alumno = registros.latest('consecutivo').nombreEstudiante
    context = {'registros':registros,
               'alumno':alumno,
               'slug':slug,}
    
    return render(request, 'alumno.html', context)

def UsarRegistroComoPlantilla(request, id):
    
    registro = Registro.objects.get(id=id)
    context = {'registro':registro,
               'vista_detallada':True,
               'envio':'form'}
    
    return render(request, 'form/form.html', context)

def EditarRegistro(request, id):

    registro = Registro.objects.get(id=id)
    consecutivo = registro.consecutivo
    
    context = {'registro':registro,
               'vista_detallada':True,
               'envio':'edit',
               'edit':True}

    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES, instance=registro)
        if form.is_valid():

            nuevo_registro = form.save(commit=False)

            nuevo_registro.form_data = request.POST

            nuevo_registro.consecutivo = consecutivo
            

            try:
                observaciones = str(request.POST.get('observaciones', ''))

                mensaje = f"{mensaje_base} {observaciones}"

                messages = [
                    Message(role="user", content=mensaje),
                ]

                options = Options(messages=messages)
                response = service.chat(options)

                nuevo_registro.resumen = response.content
            
            except:
                nuevo_registro.resumen = ''
            
            nuevo_registro.save()

            context['success'] = 'Registro actualizado exitosamente.'
            return redirect('detail', nuevo_registro.slug)

    
    return render(request, 'form/form.html', context)

def CrearNuevoRegistro(request, alumno):

    registro= Registro.objects.filter(slug=alumno).latest('consecutivo')
    
    context = {'registro':registro,
               'vista_detallada':True,
               'envio':'form'}
    
    return render(request, 'form/form.html', context)