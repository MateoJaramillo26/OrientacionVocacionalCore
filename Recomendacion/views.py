from django.shortcuts import render
from Academico.models import Calificacion, Clase, Facultad
from Usuarios.models import User

# Create your views here.
@login_required
def RecomendarCarrera(request):
    facultad = Facultad.objects.all()
    
    recomendacion = [facultad]
    
    
    if request.user.is_estudiante():
        return render(request, 'Core/RecomendarCarrera.html', {'facultad': facultad})
    