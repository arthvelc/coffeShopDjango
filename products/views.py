from django.views.generic import ListView  # Correcto
from django.urls import reverse_lazy
from django.views import generic
from products.forms import FormProduct
from products.models import Product


class ProductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = FormProduct
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'  # El template que quieres renderizar
    context_object_name = 'products'  # Nombre del contexto en la plantilla (opcional)

    # Si quisieras añadir algún filtro o lógica adicional
    def get_queryset(self):
        return Product.objects.all()

