from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def login(request):
    contexto = {}
    if request.method == "POST":
        correo = request.POST.get("correo")
        contrasena = request.POST.get("contrasena")
        contexto = {
            "correo":correo,
            "contrasena":contrasena
        }

    return render(request, 'login.html', contexto)

