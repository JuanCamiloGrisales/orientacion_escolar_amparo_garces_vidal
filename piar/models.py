from django.db import models
from django.utils.text import slugify
import os

# Create your models here.
class Piar(models.Model):
    '''Model definition for Piar.'''
    alumno = models.CharField(max_length=500, verbose_name='Nombre')
    archivo = models.FileField(upload_to='piars/')
    slug = models.SlugField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''Meta definition for Piar.'''

        verbose_name = 'Piar'
        verbose_name_plural = 'Piars'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.alumno)
        super(Piar, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.archivo:
            if os.path.isfile(self.archivo.path):
                os.remove(self.archivo.path)
                print('piar eliminado')
        super(Piar, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.archivo.name)