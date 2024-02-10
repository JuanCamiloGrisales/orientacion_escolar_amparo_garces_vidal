from django.urls import path
from . import views

urlpatterns = [
    path("imprimir/", views.imprimir, name="imprimir"),
    path("informe-completo/<str:filtro>/", views.informe_completo, name="informe_completo"),
    path("informe-nombres/<str:filtro>/", views.informe_nombres, name="informe_nombres"),
    path("informe-orientacion/", views.informe_orientacion, name="informe_orientacion"),

    path("generar-pdf/<str:template_path>/", views.generar_pdf, name="generar_pdf"),
]