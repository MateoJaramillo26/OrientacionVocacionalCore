from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, CalificacionesForm
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from Academico.models import Clase, Calificacion
from Usuarios.models import User

User = get_user_model()

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
    # Recuperar solo los datos necesarios para el usuario actual.
    if request.user.is_superuser:
        calificaciones = (
            Calificacion.objects.select_related('clase', 'estudiante')
            .only('clase__nombre', 'nota', 'estudiante__first_name', 'estudiante__last_name')
            .all()
        )
    else:
        calificaciones = (
            Calificacion.objects.select_related('clase')
            .only('clase__nombre', 'nota')
            .filter(estudiante=request.user)
        )
    
    # Preprocesar los datos en un formato listo para usar en el template.
    data = [
        {
            'estudiante': f"{cal.estudiante.first_name} {cal.estudiante.last_name}" if request.user.is_superuser else None,
            'clase': cal.clase.nombre,
            'nota': cal.nota,
        }
        for cal in calificaciones
    ]
    
    return render(request, 'core/calificaciones.html', {'data': data, 'is_superuser': request.user.is_superuser})


@login_required
def asignarNota(request):
    if not (request.user.is_profesor() or request.user.is_superuser):
        return HttpResponseForbidden("No tienes los permisos para asignar notas.")
    
    grupos = Group.objects.all()
    estudiantes_por_grupo = {
        grupo.name: User.objects.filter(groups=grupo, role='estudiante') for grupo in grupos
    }
    
    clases = Clase.objects.all()
    
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante')
        clase_id = request.POST.get('clase')
        
        # Buscar si ya existe una calificación para el estudiante y la clase
        calificacion = Calificacion.objects.filter(estudiante_id=estudiante_id, clase_id=clase_id).first()
        
        if calificacion:
            form = CalificacionesForm(request.POST, instance=calificacion)  # Cargar el formulario con la instancia existente
        else:
            form = CalificacionesForm(request.POST)  # Crear una nueva calificación
        
        if form.is_valid():
            form.save()  # Guardar cambios en la base de datos
            return redirect('asignarNota')  # Redirigir a una página de éxito
    else:
        form = CalificacionesForm()

    calificaciones = Calificacion.objects.select_related('estudiante', 'clase').all()
    return render(request, 'core/asignarNota.html', {
        'form': form,
        'estudiantes_por_grupo': estudiantes_por_grupo,
        'clases': clases,
        'calificaciones': calificaciones,
    })

def verNota(request):
    if not (request.user.is_estudiante() or request.user.is_superuser):
        return HttpResponseForbidden("No tienes los permisos para ver las notas.")

def exit(request):
    logout (request)
    return redirect('index')

