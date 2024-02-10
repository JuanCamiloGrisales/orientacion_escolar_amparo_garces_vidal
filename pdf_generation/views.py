from django.shortcuts import render
from registro_de_atencion.models import Registro
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

def imprimir(request):
    return render(request, 'imprimir.html')

def informe_completo(request, filtro='default'):
    if filtro == 'orientacion':
        registros = Registro.objects.filter(lineaDeAtencion='Orientación').order_by('gradoEscolaridad', 'nombreEstudiante', 'consecutivo')
    elif filtro == 'prevencion':
        registros = Registro.objects.filter(lineaDeAtencion='Prevención').order_by('gradoEscolaridad', 'nombreEstudiante', 'consecutivo')
    elif filtro == 'intervencion':
        registros = Registro.objects.filter(lineaDeAtencion='Intervención').order_by('gradoEscolaridad', 'nombreEstudiante', 'consecutivo')
    else:
        registros = Registro.objects.order_by('gradoEscolaridad', 'nombreEstudiante', 'consecutivo')
    estudiantes = {}

    for registro in registros:
        if registro.nombreEstudiante not in estudiantes:
            estudiantes[registro.nombreEstudiante] = []
        estudiantes[registro.nombreEstudiante].append(registro)

    context = {'estudiantes': estudiantes}
    template_path = 'informe_completo.html'

    return render(request, template_path, context)

def informe_nombres(request, filtro='default'):
    if filtro == 'orientacion':
        nombres = Registro.objects.filter(lineaDeAtencion='Orientación').values_list('nombreEstudiante', flat=True).distinct().order_by('nombreEstudiante')
    elif filtro == 'prevencion':
        nombres = Registro.objects.filter(lineaDeAtencion='Prevención').values_list('nombreEstudiante', flat=True).distinct().order_by('nombreEstudiante')
    elif filtro == 'intervencion':
        nombres = Registro.objects.filter(lineaDeAtencion='Intervención').values_list('nombreEstudiante', flat=True).distinct().order_by('nombreEstudiante')
    else:
        nombres = Registro.objects.values_list('nombreEstudiante', flat=True).distinct().order_by('nombreEstudiante')
    
    return render(request, 'informe_nombres.html', {'registros': nombres})

def informe_orientacion(request):
    registros = Registro.objects.filter(lineaDeAtencion='Orientación').order_by('gradoEscolaridad', 'nombreEstudiante', 'consecutivo')
    estudiantes = {}

    for registro in registros:
        if registro.nombreEstudiante not in estudiantes:
            estudiantes[registro.nombreEstudiante] = []
        estudiantes[registro.nombreEstudiante].append(registro)

    context = {'estudiantes': estudiantes}
    template_path = 'informe_completo.html'

    return render(request, template_path, context)

def generar_pdf(request, template_path):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="informe.pdf"'
    
    template = get_template(f'{template_path}.html').render(template_path)
    html = template.render()
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response