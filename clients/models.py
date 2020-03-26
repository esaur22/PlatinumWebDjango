from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=50, blank=False)
    commentary = models.TextField(blank=True, null=True)
    attended = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)
    


