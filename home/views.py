from django.shortcuts import render
from django.conf import settings
import os

# Create your views here.
def home(request):
    context = {}
    
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
        
    
    return render(request, 'actualizar.html')