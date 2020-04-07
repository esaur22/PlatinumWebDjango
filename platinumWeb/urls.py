"""platinumWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clients.views import home, projects, about, contact, convivienda, milan, siena, catania
from posts.views import postcontroller, posts
from users.views import login_view, logout_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name = 'home'),
    path('projects/', projects, name = 'projects'),
    path('projects/milan/', milan, name = 'milan'),
    path('projects/siena/', siena, name = 'siena'),
    path('projects/catania/', catania, name = 'catania'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('convivienda/', convivienda, name = 'convivienda'),
    path('login/', login_view, name = 'login'),
    path('postcontroller/', postcontroller, name = 'postcontroller'),
    path('logout/', logout_view, name = 'logout'),
    path('posts/', posts, name = 'posts'),

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#Le suma al urlpattern una url estatica, con el valor de la media que tenemos y donde estamos parados en la media

admin.site.site_header = "PLATINUM BASE"
admin.site.site_title = "PLATINUM BASE"
admin.site.index_title = "Bienvenidos al panel de administracion de PLATINUM BASE "