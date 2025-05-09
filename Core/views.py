from django.shortcuts import render

def home(request):  # This must be named 'home' to match urls.py
    return render(request, 'Core/index.html')

def login_view(request):  # Must be named 'login_view' to match urls.py
    return render(request, 'Core/login.html')

def register(request):
    return render(request, 'Core/register.html')