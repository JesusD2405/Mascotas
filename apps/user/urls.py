from django.urls import path

# Importación de Vistas
from apps.user.views import *

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', userRegister, name='user_register'),
]
