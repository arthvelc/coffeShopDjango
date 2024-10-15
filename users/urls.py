from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    #path('logout/', LogoutView.asview(), name='logout'),
    #path('register/', views.register, name='register'),
]