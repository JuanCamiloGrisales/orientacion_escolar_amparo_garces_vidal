from django.db import models
from django.utils.text import slugify

# Create your models here.

class Archivo(models.Model):
    '''Model definition for Archivo.'''
    archivo = models.FileField(upload_to='archivos/')

    class Meta:
        '''Meta definition for Archivo.'''

        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'

    def __str__(self):
        return str(self.id)

class Registro(models.Model):
    '''Model definition for Registro.'''
    consecutivo = models.IntegerField(blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    municipio = models.CharField(max_length=500, null=True, blank=True)
    institucion = models.CharField(max_length=500, null=True, blank=True)
    dane = models.CharField(max_length=500, null=True, blank=True)
    sede = models.CharField(max_length=500, null=True, blank=True)
    remitidoPor = models.TextField(null=True, blank=True)
    nombreRemitidoPor = models.CharField(max_length=500, null=True, blank=True)
    posiblesMotivosDeAtencion = models.TextField(null=True, blank=True)
    lineaDeAtencion = models.CharField(max_length=500, null=True, blank=True)
    tipoDeAtencion = models.CharField(max_length=500, null=True, blank=True)
    entidadPrestadoraDeSalud = models.CharField(max_length=500, null=True, blank=True)
    personaDeConfianza = models.CharField(max_length=500, null=True, blank=True)
    # ------------------
    nombreEstudiante = models.CharField(max_length=500, null=True, blank=True)
    tipoDocumentoEstudiante = models.CharField(max_length=500, null=True, blank=True)
    numeroDocumentoEstudiante = models.CharField(max_length=500, null=True, blank=True)
    gradoEscolaridad = models.CharField(max_length=500, null=True, blank=True)
    numeroTelefonoEstudiante = models.CharField(max_length=500, null=True, blank=True)
    epsEstudiante = models.CharField(max_length=500, null=True, blank=True)
    edadEstudiante = models.CharField(max_length=500, null=True, blank=True)
    fechaNacimientoEstudiante = models.CharField(max_length=500, null=True, blank=True)
    lugarNacimientoEstudiante = models.CharField(max_length=500, null=True, blank=True)
    telefonoAcudiente = models.CharField(max_length=500, null=True, blank=True)
    documentoAcudiente = models.CharField(max_length=500, null=True, blank=True)
    direccion = models.CharField(max_length=500, null=True, blank=True)
    parentescoAcudiente = models.CharField(max_length=500, null=True, blank=True)
    # ------------------
    sexo = models.CharField(max_length=500, null=True, blank=True)
    genero = models.CharField(max_length=500, null=True, blank=True)
    parentesco = models.CharField(max_length=500, null=True, blank=True)
    nombre = models.CharField(max_length=500, null=True, blank=True)
    edad = models.CharField(max_length=500, null=True, blank=True)
    ocupacion = models.CharField(max_length=500, null=True, blank=True)
    nivelEducativo = models.CharField(max_length=500, null=True, blank=True)
    estadoCivil = models.CharField(max_length=500, null=True, blank=True)
    numeroHijos = models.CharField(max_length=500, null=True, blank=True)
    telefono = models.CharField(max_length=500, null=True, blank=True)
    lugarResidencia = models.CharField(max_length=500, null=True, blank=True)
    tipoFamilia = models.CharField(max_length=500, null=True, blank=True)
    hogarYBienestar = models.TextField(null=True, blank=True)
    # ------------------
    espectativasEntrevistado = models.TextField(null=True, blank=True)
    acuerdosPrevios = models.ManyToManyField(Archivo, related_name='acuerdosPrevios', blank=True)
    # ------------------
    condicionDiscapacidad = models.CharField(max_length=500, null=True, blank=True)
    tipoDiscapacidad = models.CharField(max_length=500, null=True, blank=True)
    talentoYCapacidadesExepcionales = models.TextField(null=True, blank=True)
    relatoEntrevistado = models.TextField(null=True, blank=True)
    # ------------------
    observaciones = models.TextField(null=True, blank=True)
    activacionRuta = models.CharField(max_length=500, null=True, blank=True)
    procesosConvivencia = models.TextField(null=True, blank=True)
    remision = models.ManyToManyField(Archivo, related_name='remision', blank=True)
    piar = models.ManyToManyField(Archivo, related_name='piar', blank=True)
    estadoCaso = models.CharField(max_length=500, null=True, blank=True)
    compromisoPadres = models.ManyToManyField(Archivo, related_name='compromisoPadres', blank=True)
    compromisoEstudiantes = models.ManyToManyField(Archivo, related_name='compromisoEstudiantes', blank=True)
    fechaProximoSeguimiento = models.DateTimeField(null=True, blank=True)
    nombreOrientadora = models.CharField(max_length=500, null=True, blank=True)
    # ------------------
    created = models.DateTimeField(auto_now_add=True)
    form_data = models.JSONField(null=True, blank=True)
    resumen = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        '''Meta definition for Registro.'''

        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
    
    def save(self, *args, **kwargs):
        if not self.id:
            ultimo_consecutivo = Registro.objects.filter(nombreEstudiante=self.nombreEstudiante).order_by('consecutivo').last()
            self.consecutivo = (ultimo_consecutivo.consecutivo if ultimo_consecutivo else 0) + 1


        # Refactoring code to ensure none of the fields are saved as null, instead save as empty str
        for field in self._meta.fields:
            
            if getattr(self, field.name) is None and isinstance(field, (models.CharField, models.TextField)):
                # Establece el valor del campo a un str vacío
                setattr(self, field.name, '')
        
        if not self.slug:
            self.slug = slugify(self.nombreEstudiante)

        super(Registro, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)