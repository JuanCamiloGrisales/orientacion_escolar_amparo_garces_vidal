from django.urls import path
from .views import analiticas

urlpatterns = [
    path('', analiticas, name='analiticas'),
]