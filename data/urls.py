from django.urls import path
from .views import analiticas, export_database, backups

urlpatterns = [
    path('', analiticas, name='analiticas'),
    path('backups/', backups, name='backups'),
    path('export-database/', export_database, name='export_database'),
]