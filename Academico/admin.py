from django.contrib import admin
from .models import Pais, Ciudad, Universidad, Clase, Calificacion, Facultad, Empleabilidad, InvestigacionYDescubrimiento

admin.site.register(Pais)
admin.site.register(Universidad)
admin.site.register(Facultad)

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'profesor')
    search_fields = ('nombre', 'profesor__username')

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('clase', 'estudiante', 'nota')
    list_filter = ('clase', 'estudiante')
    search_fields = ('clase__nombre', 'estudiante__username')

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    list_filter = ('pais',)
    search_fields = ('nombre', 'pais__nombre')

@admin.register(Empleabilidad)
class EmpleabilidadAdmin(admin.ModelAdmin):
    list_display = ('facultad', 'universidad', 'empleabilidad')
    list_filter = ('facultad', 'universidad')
    search_fields = ('facultad__nombre', 'universidad__nombre')

@admin.register(InvestigacionYDescubrimiento)
class InvestigacionYDescubrimientoAdmin(admin.ModelAdmin):
    list_display = ('facultad', 'universidad', 'citacionesPorEscrito', 'citacionesPorInvestigacion', 'reputacionAcademica')
    list_filter = ('facultad', 'universidad')
    search_fields = ('facultad__nombre', 'universidad__nombre')
# Register your models here.