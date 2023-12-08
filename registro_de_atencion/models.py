from django.db import models

# Create your models here.

class Registro(models.Model):
    '''Model definition for Registro.'''
    consecutivo = models.IntegerField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    municipio = models.CharField(max_length=500, null=True, blank=True)
    institucion = models.CharField(max_length=500, null=True, blank=True)
    dane = models.CharField(max_length=500, null=True, blank=True)
    sede = models.CharField(max_length=500, null=True, blank=True)
    remitidoPor = models.TextField(null=True, blank=True)


    class Meta:
        '''Meta definition for Registro.'''

        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return str(self.id)