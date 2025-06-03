from django.shortcuts import render
from Academico.models import Calificacion, Clase, Facultad
from Usuarios.models import User
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from Academico.models import Calificacion, Clase, Facultad, Empleabilidad, InvestigacionYDescubrimiento
# Create your views here.

@login_required
def RecomendarCarrera(request):
    user = request.user
    calificaciones = Calificacion.objects.filter(estudiante=user).select_related('clase')
    facultad_notas = defaultdict(list)
    for cal in calificaciones:
        for facultad in cal.clase.facultad_set.all():
            facultad_notas[facultad].append(cal.nota)
    promedio_por_facultad = {facultad: sum(notas)/len(notas) for facultad, notas in facultad_notas.items()}

    # Encontrar la(s) mejor(es) nota(s)
    if promedio_por_facultad:
        max_nota = max(promedio_por_facultad.values())
        mejores_facultades = [fac for fac, nota in promedio_por_facultad.items() if nota == max_nota]
    else:
        mejores_facultades = []

    ranking = []
    for facultad in mejores_facultades:
        for uni in facultad.universidad_set.all():
            empleabilidad = Empleabilidad.objects.filter(facultad=facultad, universidad=uni).first()
            investigacion = InvestigacionYDescubrimiento.objects.filter(facultad=facultad, universidad=uni).first()
            score = 0
            if empleabilidad:
                score += empleabilidad.empleabilidad
            if investigacion:
                score += investigacion.citacionesPorEscrito + investigacion.citacionesPorInvestigacion + investigacion.reputacionAcademica
            ranking.append({'universidad': uni, 'facultad': facultad, 'score': score})
    ranking.sort(key=lambda x: x['score'], reverse=True)
    return render(request, 'Core/recomendarCarrera.html', {'promedio_por_facultad': promedio_por_facultad, 'ranking': ranking})
