from django.shortcuts import render
import locale
from .forms import RegistroForm
from .files_reader import configurar_municipios, configurar_estudiantes
from .models import Registro
from usellm import Message, Options, UseLLM

locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')
service = UseLLM(service_url="https://usellm.org/api/llm")

def FormularioDeRegistroDeAtencion(request):
    context = {}

    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():

            registro = form.save(commit=False)

            registro.form_data = request.POST

            try:
                texto_a_reemplazar = """
Nota: La información consignada no constituye en ningún caso un diagnóstico o concepto medico y/o profesional sobre la salud mental o física de la persona a quien se refiere, ni tampoco sustituye el informe que deben adelantar las autoridades competentes sobre la presunta comisión de algún delito. Este informe es una ficha de seguimiento de la profesional de orientación escolar para darle adecuada atención y acompañamiento en el proceso de formación dentro del sistema de convivencia escolar.

POLÍTICA DE PROTECCIÓN DE DATOS PERSONALES: Dado que la información contenida en el siguiente texto contiene datos sensibles y privados sobre terceros; se solicita mantener absoluta confidencialidad sobre la identidad y circunstancias descriptas; quedando bajo la responsabilidad de quienes reciben este informe la violación del derecho a la intimidad y el respeto a la privacidad. Es preciso abstenerse de exponer en reuniones y comités con carácter informativos o instancias de toma de decisiones estratégicas la identidad, ubicación y demás datos que posibiliten la identificación de las personas de las que trata este este reporte. """
                observaciones = str(request.POST.get('observaciones', ''))
                observaciones = observaciones.replace(texto_a_reemplazar, '')

                mensaje = f"Crea un resumen muy corto de tan solo 1 o máximo 2 renglones de la siguiente observación.\nLa observación es la siguiente: {observaciones}'"

                print(mensaje)

                messages = [
                    Message(role="system", content="Eres un robot psicoorientador con experiencia haciendo observaciones a tus pacientes niños y adolecentes"),
                    Message(role="user", content=mensaje),
                ]

                options = Options(messages=messages)
                response = service.chat(options)

                registro.resumen = response.content
            
            except:
                registro.resumen = 'Resumen no disponible'
            
            registro.save()

            context['success'] = 'Registro guardado correctamente.'
            return render(request, 'form/form.html', context)

    else:
        pass

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
    
    registros = Registro.objects.filter(nombreEstudiante=alumno)
    context = {'registros':registros,
               'alumno':alumno}
    
    return render(request, 'alumno.html', context)