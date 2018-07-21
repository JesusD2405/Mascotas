from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core import serializers
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Importacion de modelos
from apps.user.models import *

# Pagina principal
def index(request):
	return render(request, 'index.html')

# login
def login(request):
	return render(request, 'pagina.html')

# Registro de usuario
def userRegister(request):
	return render(request, 'pagina1.html')

# Crear Usuario
class user(CreateView):
    model = User
    #form_class = MascotaForm
    template_name = 'pagina1.html'
    #success_url = reverse_lazy('mascota_listar')
