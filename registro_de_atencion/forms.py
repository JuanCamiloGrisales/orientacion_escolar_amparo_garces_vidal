from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        exclude = ('acuerdosPrevios', 'compromisoEstudiantes', 'compromisoPadres', 'remision', 'piar')