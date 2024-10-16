from .views import OrderView
from django.urls import path

urlpatterns = [
    path('my_order/', OrderView.as_view(), name='my_order'),
]
