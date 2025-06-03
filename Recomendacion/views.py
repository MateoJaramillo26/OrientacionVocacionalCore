from django.shortcuts import render
from Academico.models import Calificacion, Clase, Facultad
from Usuarios.models import User
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from Academico.models import Calificacion, Clase, Facultad, Empleabilidad, InvestigacionYDescubrimiento
# Create your views here.

def obtenerPromedioPorFacultad(calificaciones):
    facultadNotas = defaultdict(list)
    for calificacion in calificaciones:
        for facultad in calificacion.clase.facultad_set.all():
            facultadNotas[facultad].append(calificacion.nota)
    return {facultad: sum(notas)/len(notas) for facultad, notas in facultadNotas.items()}

def obtenerMejorFacultad(promedioPorFacultad):
    if not promedioPorFacultad:
        return []
    maxNota = max(promedioPorFacultad.values())
    return [facultad for facultad, nota in promedioPorFacultad.items() if nota == maxNota]

def calcularRanking(facultades):
    ranking = []
    for facultad in facultades:
        for universidad in facultad.universidad_set.all():
            empleabilidad = Empleabilidad.objects.filter(facultad=facultad, universidad=universidad).first()
            investigacion = InvestigacionYDescubrimiento.objects.filter(facultad=facultad, universidad=universidad).first()
            score = 0
            if empleabilidad:
                score += empleabilidad.empleabilidad
            if investigacion:
                valorPromedioInvestigacion = (investigacion.citacionesPorEscrito + investigacion.citacionesPorInvestigacion + investigacion.reputacionAcademica)/3
                score += valorPromedioInvestigacion
                score = score/2
            ranking.append({'universidad': universidad, 'facultad': facultad, 'score': score})
    ranking.sort(key=lambda x: x['score'], reverse=True)
    return ranking
            
@login_required
def RecomendarCarrera(request):
    user = request.user
    calificaiones = Calificacion.objects.filter(estudiante=user).select_related('clase')
    promedioPorFacultad = obtenerPromedioPorFacultad(calificaiones)
    mejorFacultad = obtenerMejorFacultad(promedioPorFacultad)
    ranking = calcularRanking(mejorFacultad)
    return render(request, 'Core/recomendarCarrera.html', {'promedioPorFacultad': promedioPorFacultad,'ranking': ranking})