from django.db import models

# Create your models here.

class User(models.Model):
    name = models.TextField(max_length=100, verbose_name= 'nombre del usuario')
    last_name = models.TextField(max_length=100, verbose_name= 'apellido del usuario')
    email = models.EmailField(max_length=100, verbose_name= 'correo del usuario')
    password = models.TextField(max_length=100, verbose_name= 'contraseña del usuario')
    created = models.DateTimeField(auto_now_add=True, verbose_name= 'fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'fecha de actualizacion')

    def __str__(self):
        return self.name
