from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    """Profile model.
    Proxy model that extends the base data with other information."""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)#Aqui se crea la conexion entre el modelo User que trae por defecto django y el modelo que nosotros estamos creando
    
    
    def __str__(self):
        return self.user.username#recordar que estamos extendiendo la clase User que propone django, por eso la importamos
    