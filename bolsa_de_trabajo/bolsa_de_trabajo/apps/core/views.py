from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

def index(request):
    lista_nombres = ['Leonardo','Gabriel','Santiago','Leandro']
    lista_apellido = ['Nina','Campos Kray','Palleres','Perez Pignolo']
    contexto = {
        'nombres':lista_nombres,
        'apellidos':lista_apellido,
    }
    return render(request, 'index.html', contexto)

def home(request):
    return render(request, 'home.html', {})
    
def login(request):
    return render(request, 'login.html', {})

def sign_up(request):
    return render(request, 'login.html', {})

