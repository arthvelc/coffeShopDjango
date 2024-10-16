from django.views.generic import ListView  # Correcto
from django.urls import reverse_lazy
from django.views import generic
from products.forms import FormProduct
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer



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
    
class ProductListApi(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all() # por medio de una query obtengo todos los productos
        serializer = ProductSerializer(products, many = True) # serializo los productos

        return Response(serializer.data)
    
    def post(self, request):
        #primero deserializo los datos
        serializer = ProductSerializer(data = request.data)
        # valido los datos
        if serializer.is_valid():
            # guardo los datos en la base de datos y devuelvo una respuesta
            serializer.save()
            return Response(serializer.data, status= 201)
            print(serializer.data)
        # si no es valido devuelvo una respuesta con el error
        return Response(serializer.errors, status=400)
        print(serializer.errors) 
    


