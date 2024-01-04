from django.shortcuts import render
from .functionality import main
import datetime
import locale

# Create your views here.
def calendario(request):
    eventos = main()
    context = {}
    if isinstance(eventos, list):
        formatted_eventos = []
        for date, title in eventos:
            formatted_date = fecha_a_string(date)
            
            formatted_eventos.append((formatted_date, title))
        context['eventos'] = formatted_eventos
    else:
        context['error'] = eventos
    return render(request, 'calendar.html', context)

def fecha_a_string(date):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    date_obj = datetime.datetime.fromisoformat(date)
    # Formatear la fecha
    formatted_date = date_obj.strftime('%d de %B del %Y a las %I:%M')
    am_pm = date_obj.strftime('%p')
    am_pm_es = "a.m." if am_pm == 'AM' else "p.m."
    formatted_date = f"{formatted_date} {am_pm_es}"
    return formatted_date