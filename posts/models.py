from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='posts/photos')
    contenido = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)