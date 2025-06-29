import decimal
from typing import override
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

User = get_user_model()

# Create your models here.
class Universidad(models.Model):
    id_universidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE)
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE)
    facultad = models.ManyToManyField('Facultad')
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    sitio_web = models.URLField(verbose_name="Sitio Web")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Universidad"
        verbose_name_plural = "Universidades"

class Clase(models.Model):
    id_clase = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    codigo = models.CharField(max_length=20, verbose_name="Código")
    creditos = models.IntegerField(verbose_name="Créditos")
    profesor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'profesor'})
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"

class Facultad(models.Model):
    id_facultad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    clases = models.ManyToManyField(Clase)
  
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"

class Empleabilidad(models.Model):
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)
    empleabilidad = models.FloatField(verbose_name="Valor de Empleabilidad", default=0, validators=[MaxValueValidator(100.0)])

    def __str__(self):
        return f"{self.empleabilidad} - {self.facultad.nombre} - {self.universidad.nombre}"

    class Meta:
        verbose_name = "Empleabilidad"
        verbose_name_plural = "Empleabilidad"
    
class InvestigacionYDescubrimiento(models.Model):
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)
    citacionesPorEscrito = models.FloatField(verbose_name="Citas por Escrito", default=0, validators=[MaxValueValidator(100.0)])
    citacionesPorInvestigacion = models.FloatField(verbose_name="Citas por Investigación", default=0, validators=[MaxValueValidator(100.0)])
    reputacionAcademica = models.FloatField(verbose_name="Reputación Académica", default=0, validators=[MaxValueValidator(100.0)])
    
    def __str__(self):
        return f"{self.citacionesPorEscrito} - {self.citacionesPorInvestigacion} - {self.reputacionAcademica} - {self.facultad.nombre} - {self.universidad.nombre}"

    class Meta:
        verbose_name = "Investigación y Descubrimiento"
        verbose_name_plural = "Investigación y Descubrimientos"

class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'estudiante'})
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    nota = models.FloatField(verbose_name="Nota", validators=[MaxValueValidator(10)], default=0)
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de Registro")
    comentario = models.TextField(blank=True, null=True, verbose_name="Comentario")

    def __str__(self):
        return f"{self.estudiante.username} - {self.clase.nombre} - {self.nota}"

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"
        
        
class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        
class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"