from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('filtrar/<filter>/', filter, name='filter'),
    path('actualizar/', actualizar, name='actualizar'),
]