from django import forms

#Models
from clients.models import Client

class ClientForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = ("name", "phone", "commentary")


