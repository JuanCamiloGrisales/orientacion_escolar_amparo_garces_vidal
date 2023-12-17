from django.urls import path
from .views import *

urlpatterns = [
    path('', FormularioDeRegistroDeAtencion, name='form'),
    path('<alumno>/', Alumno, name='detail'),
]