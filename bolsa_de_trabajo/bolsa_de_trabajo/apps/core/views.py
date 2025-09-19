from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def sign_up(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        contrasena = request.POST.get("contrasena")
        
        Usuario.objects.create(correo,contrasena)
    return render(request, 'login.html', {})

def login(request):
    if request.method == "POST":
        
        pass
    return render(request, 'login.html', {})

