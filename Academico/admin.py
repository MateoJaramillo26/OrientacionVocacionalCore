from django.contrib import admin
from .models import Pais, Ciudad, Universidad, Clase, Calificacion, Facultad

admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Universidad)
admin.site.register(Clase)
admin.site.register(Calificacion)
admin.site.register(Facultad)
# Register your models here.