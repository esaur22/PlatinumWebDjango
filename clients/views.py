from django.shortcuts import render, redirect, reverse
from clients.forms import ClientForm
from django.http import HttpResponseRedirect
from clients.models import Client



# Create your views here.
def home(request):
    # client = Client
    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            form.save()

            return render(request, 'navigations/index.html', {'mensaje':'Información recibida, te contactaremos pronto'})
    else:

        form = ClientForm()

    return render(request, 'navigations/index.html', {'form':form})    

def projects(request):
    return render(request, 'navigations/projects.html')    

def about(request):
    return render(request, 'navigations/about.html')    

def contact(request):
        # client = Client
    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            form.save()

            return render(request, 'navigations/contact.html', {'mensaje':'Informacion recibida'})
    else:

        form = ClientForm()

  
    return render(request, 'navigations/contact.html', {'form':form})    

def convivienda(request):
    return render(request, 'navigations/convivienda.html')    

def milan(request):
    return render(request, 'navigations/milan.html')    

def siena(request):
    return render(request, 'navigations/siena.html')    

def catania(request):
    return render(request, 'navigations/catania.html')    

#def get_data(request):
    
