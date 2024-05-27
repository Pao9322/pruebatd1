from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('admin', 'Admin'),
        ('lector', 'Lector'),
    ]
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES, default='lector')

# Se agrega related_name para evitar conflictos con el modelo auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios',
        blank=True,
        help_text=('Los grupos a los que pertenece este usuario. Un usuario obtendrá todos los permisos '
                   'concedidos a cada uno de sus grupos.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
# Esto define el nombre de la relación inversa desde Permission hacia Usuario 
        related_name='usuarios',      
        blank=True,
        help_text=('Permisos específicos para este usuario.'),
        verbose_name=('permisos de usuario'),
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['username']

    def __str__(self):
        return self.username    

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    año_publicacion = models.IntegerField()
    portada_url = models.TextField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

class Reseña(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField()
    fecha_resena = models.DateField()

    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
        ordering = ['-fecha_resena']

    def __str__(self):
        return f'{self.libro.titulo} - {self.usuario.username}'

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class SeguirAutor(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Seguir Autor"
        verbose_name_plural = "Seguir Autores"
        unique_together = ('usuario', 'autor')

    def __str__(self):
        return f'{self.usuario.username} sigue a {self.autor.nombre}'

class Actividad(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    accion = models.CharField(max_length=100)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ['-fecha']