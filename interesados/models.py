from django.db import models

# Create your models here.
class interesado(models.Model):
    telefono = models.CharField(unique = True,  max_length=50, blank = False, null = False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    compro = models.BooleanField(default = False)
    vendedor = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    ciudad = models.CharField(max_length=50, default = 'Juticalpa')
    estatus = models.CharField(max_length=50, blank=True, null=True)
    modificado = models.TextField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)