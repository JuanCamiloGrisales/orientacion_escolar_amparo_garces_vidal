from django.shortcuts import render
from .models import EditarCampos

# Create your views here.
def editar_formulario(request):

    if not EditarCampos.objects.exists():
        EditarCampos.objects.create()
    
    configuracion = EditarCampos.objects.first()

    if request.method == 'POST':
        configuracion = EditarCampos.objects.first()
        
        for field in EditarCampos._meta.fields:
            if hasattr(field, 'attname'):
                field_name = field.attname
                default_key = f"{field_name}Default"
                opciones_key = f"{field_name}Opciones"
                
                # Actualizar el valor por defecto
                if default_key in request.POST:
                    json_data = getattr(configuracion, field_name)
                    json_data['default'] = request.POST[default_key]
                    setattr(configuracion, field_name, json_data)
                
                # Actualizar las opciones, eliminando opciones vacías
                if opciones_key in request.POST:
                    opciones = request.POST.getlist(opciones_key)
                    opciones = [opcion for opcion in opciones if opcion]  # Eliminar opciones vacías
                    json_data = getattr(configuracion, field_name)
                    json_data['opciones'] = opciones
                    setattr(configuracion, field_name, json_data)
        
        configuracion.save()  # Guardar los cambios en la base de datos
        return render(request, 'formEditor.html', {'configuracion': configuracion, 'success': True})

    context = {'configuracion': configuracion}
    
    return render(request, 'formEditor.html', context)