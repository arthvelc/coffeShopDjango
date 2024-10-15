from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = 'user/Register.html'
    template_name = reverse_lazy('login')
    

