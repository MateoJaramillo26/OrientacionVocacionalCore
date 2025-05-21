from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):  # This must be named 'home' to match urls.py
    return render(request, 'core/index.html')

def login_view(request):  # Must be named 'login_view' to match urls.py
    return render(request, 'core/login.html')

def register(request):
    return render(request, 'core/register.html')

@login_required
def calificaciones(request):
    return render(request, 'core/calificaciones.html')

@login_required
def asignarNota(request):
    return render(request, 'core/asignarNota.html')

def exit(request):
    logout (request)
    return redirect('index')