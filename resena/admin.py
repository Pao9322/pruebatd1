from django.contrib import admin
from .models import Contacto, Genero, Autor, Libro, Usuario, Reseña, SeguirAutor

admin.site.register(Contacto)
admin.site.register(Genero)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Reseña)
admin.site.register(SeguirAutor)

