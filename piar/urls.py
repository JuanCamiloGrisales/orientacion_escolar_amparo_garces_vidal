from django.urls import path
from .views import *

urlpatterns = [
    path('', piars, name='piars'),
]