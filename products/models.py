from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=100, verbose_name= 'nombre del producto')
    description = models.TextField(max_length=255, verbose_name= 'descripcion del producto')
    price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name= 'precio del producto')
    available = models.BooleanField(default=True, verbose_name= 'disponibilidad del producto')
    photo = models.ImageField(upload_to='logos',blank= True, null=True, verbose_name= 'foto del producto')
    created = models.DateTimeField(auto_now_add=True, verbose_name= 'fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'fecha de actualizacion')

    def __str__(self):
        return self.name
