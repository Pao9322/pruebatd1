"""
URL configuration for resena_libros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from resena.views import Inicio, Registrarse, IniciarSesion, PanelControl, ExplorarLibros
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio.as_view(), name='inicio'),
    path('registrarse/', Registrarse.as_view(), name='registrarse'),
    path('iniciar_sesion/', LoginView.as_view(template_name='iniciar_sesion.html'), name='iniciar_sesion'),
    path('cerrar_sesion/', LogoutView.as_view(next_page='/'), name='cerrar_sesion'),
    path('panel_control/', PanelControl.as_view(), name='panel_control'),
    path('explorar_libros/', ExplorarLibros.as_view(), name='explorar_libros'),
]
