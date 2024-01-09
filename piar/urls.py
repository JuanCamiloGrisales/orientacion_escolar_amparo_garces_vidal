from django.urls import path
from .views import *

urlpatterns = [
    path('', piars, name='piars'),
    path('<slug>/', detailed_piar, name='detailed_piar'),
    path('delete/<int:id>/', delete_piar, name='delete_piar'),
]