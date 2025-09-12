from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {})
    
def login(request):
    return render(request, 'login.html', {})

def sign_up(request):
    return render(request, 'login.html', {})

