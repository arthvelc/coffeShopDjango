from django import forms

from products.models import Product


class FormProduct(forms.Form):
    name = forms.CharField(label='Nombre del producto', max_length=100, required=True)
    description = forms.CharField(label='Descripcion del producto', max_length=255, required=True)
    price = forms.DecimalField(label='Precio del producto', max_digits=10, decimal_places=2, required=True)
    available = forms.BooleanField(label='Disponibilidad del producto', required=True)
    photo = forms.ImageField(label='Foto del producto', required=False)


    def save(self):
        Product.objects.create(
            name = self.cleaned_data['name'],
            description = self.cleaned_data['description'],
            price = self.cleaned_data['price'],
            available = self.cleaned_data['available'],
            photo = self.cleaned_data['photo'],
        )