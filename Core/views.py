from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, CalificacionesForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from Academico.models import Clase

def index(request):  # This must be named 'home' to match urls.py
    return render(request, 'core/index.html')

def login_view(request):  # Must be named 'login_view' to match urls.py
    return render(request, 'core/login.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user = user_creation_form.save(commit=False)
            user.role = 'estudiante'
            user.save()
            estudiantes_group, created = Group.objects.get_or_create(name='estudiantes')
            user.groups.add(estudiantes_group)
            user.save()
            
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
        data['form'] = user_creation_form  # Solo actualiza aquí si hay POST y errores
    return render(request, 'registration/register.html', data)

@login_required
def calificaciones(request):
    return render(request, 'core/calificaciones.html')

@login_required
def asignarNota(request):
    return render(request, 'core/asignarNota.html')

def exit(request):
    logout (request)
    return redirect('index')

def inscribirClases(request):
    return render(request, 'core/inscribirClases.html')

@login_required
def asignarNota(request):
    if not (request.user.is_profesor() or request.user.is_superuser):
        return HttpResponseForbidden("No tienes los permisos para asignar notas.")
    
    grupos = Group.objects.all()
    estudiantes = {
        grupo.name: grupo.custom_user_set.filter(role='estudiante') for grupo in grupos
    }
    
    clases = Clase.objects.all()
    
    if request.method == 'POST':
        form = CalificacionesForm(request.POST)
        
        if form.is_valid():
            calificacion = form.save(commit=False)
            calificacion.superuser = request.user
            calificacion.profesor = request.user
            calificacion.save()
            return redirect('calificaciones')
    else:
        form = CalificacionesForm()

    return render(request, 'core/asignarNota.html', {
        'form': form,
        'estudiantes': estudiantes,
        'clases': clases,
    })