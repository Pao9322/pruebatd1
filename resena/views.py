from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Usuario, Libro, Reseña, Actividad
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

class ListaUsuarios(ListView):
    model = Usuario

class CrearUsuario(CreateView):
    model = Usuario
    # Limitar los campos disponibles para crear usuarios
    fields = ['username', 'email', 'password']  

class ActualizarUsuario(UpdateView):
    model = Usuario
    # Limitar los campos disponibles para actualizar usuarios
    fields = ['username', 'email', 'password']  

class EliminarUsuario(DeleteView):
    model = Usuario

class ListaLibros(ListView):
    model = Libro

class CrearLibro(CreateView):
    model = Libro
    fields = '__all__'

class ActualizarLibro(UpdateView):
    model = Libro
    fields = '__all__'

class EliminarLibro(DeleteView):
    model = Libro

class ListaReseñas(ListView):
    model = Reseña

class CrearReseña(CreateView):
    model = Reseña
    fields = '__all__'

    def form_valid(self, form):
        # Asignar el usuario actual como autor de la reseña
        form.instance.usuario = self.request.user  
        actividad = Actividad(usuario=self.request.user, accion='Publicó una reseña', libro=form.instance.libro)
        # Registrar la actividad de publicar una reseña
        actividad.save()  
        return super().form_valid(form)

class ActualizarReseña(UpdateView):
    model = Reseña
    fields = '__all__'

class EliminarReseña(DeleteView):
    model = Reseña
    success_url = '/'

def libro_search(request):
    query = request.GET.get('q')
    if query:
        libros = Libro.objects.filter(titulo__icontains=query) | Libro.objects.filter(autor__nombre__icontains=query)
    else:
        libros = Libro.objects.all()
    return render(request, 'libro_search.html', {'libros': libros})

class Inicio(TemplateView):
    template_name = 'inicio.html'

class Registrarse(CreateView):
    form_class = UserCreationForm
    template_name = 'registrarse.html'
    success_url = reverse_lazy('panel_control')

class IniciarSesion(LoginView):
    template_name = 'iniciar_sesion.html'

class PanelControl(LoginRequiredMixin, TemplateView):
    template_name = 'panel_control.html'

class ExplorarLibros(LoginRequiredMixin, ListView):
    model = Libro
    template_name = 'explorar_libros.html'
    context_object_name = 'libros'