from django.db import models
from users.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuario')
    is_active = models.BooleanField(default=True, verbose_name='estado')
    quantity = models.IntegerField(verbose_name='cantidad')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')


    def __str__(self):
        return self.product.name
    

class OrderProduct(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, verbose_name='pedido')
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, verbose_name='producto')
    quantity = models.IntegerField(verbose_name='cantidad')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='total')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')

    def __str__(self):
        return self.product.name

