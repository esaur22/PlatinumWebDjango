from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout #Funciones necesarias para el inicio de sesion de los usuarios
from django.shortcuts import render, redirect #Metodo que nos permite renderizar un template
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):#Recordar que las vistas siempre reciben un request para parametro
    if request.method == "POST":#Solo cuando haya un metodo post me mostraras esto
        
        username = request.POST['username']        
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        if user:#Todo esto esta en la documentacion, en el enlace que envie, esto significa "Si el usuario y contrasena con correctas:"
            login(request, user)
            return redirect('postcontroller')#Es necesario utilizar el metodo redirect si el usuario y contra son correctas, esto nos llevara a la pagina de portada una vez que hemos iniciado sesion
        else:
            return render(request, 'navigations/login.html', {'error': 'Invalid username and password'})#Si el usuario y contrasena no son buenos nos dirigira a la misma pagina pero con un error
    return render(request, 'navigations/login.html')

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')
