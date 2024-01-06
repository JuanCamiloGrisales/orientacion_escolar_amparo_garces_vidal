from django.urls import path
from .views import *

urlpatterns = [
    path('', FormularioDeRegistroDeAtencion, name='form'),
    path('<alumno>/', Alumno, name='detail'),
    path('registro/<int:id>/', UsarRegistroComoPlantilla, name='registro'),
    path('crear/<alumno>/', CrearNuevoRegistro, name='create'),
    path('editar/<int:id>/', EditarRegistro, name='edit'),
    path('archivos/<int:id>/', VerArchivos, name='archivos'),
]