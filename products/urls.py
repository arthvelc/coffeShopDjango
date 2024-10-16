from django import views
from django.urls import path
from django.conf.urls.static import static
from coffeShop import settings
from products.views import ProductFormView, ProductListView, ProductListApi

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('agregar/', ProductFormView.as_view(), name='add_product'),
    path('api/', ProductListApi.as_view(), name='products_api'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)