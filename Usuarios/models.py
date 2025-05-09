from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

class User(AbstractUser):
    ROLES = (
        ('estudiante', 'Estudiante'),
        ('profesor', 'Profesor'),
    )
    role = models.CharField(max_length=10, choices=ROLES, verbose_name="Rol")
    cedula = models.CharField(max_length=10, unique=True, verbose_name="Cédula")
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")

    # Campos opcionales para perfiles específicos
    especialidad = models.CharField(max_length=100, null=True, blank=True, verbose_name="Especialidad")
    departamento = models.CharField(max_length=100, null=True, blank=True, verbose_name="Departamento")
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de Nacimiento")
    direccion = models.TextField(null=True, blank=True, verbose_name="Dirección")

    # Override groups and user_permissions with related_name
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

    def is_estudiante(self):
        return self.role == 'estudiante'

    def is_profesor(self):
        return self.role == 'profesor'

    def __str__(self):
        return f"{self.username} ({self.role})"

    def clean(self):
        super().clean()
        if self.cedula:
            if not self.validar_cedula_ecuatoriana(self.cedula):
                raise ValidationError({'cedula': 'La cédula ingresada no es una cédula ecuatoriana válida'})
        
        if self.telefono:
            # Asegurar que el teléfono contenga solo dígitos
            if not self.telefono.isdigit():
                raise ValidationError({'telefono': 'El teléfono debe contener solo números.'})
            # Asegurar que el teléfono tenga exactamente 10 dígitos
            # Esta validación es redundante si max_length=10 y el campo es obligatorio,
            # pero es buena práctica tenerla para claridad y si el campo fuera opcional.
            if len(self.telefono) != 10:
                raise ValidationError({'telefono': 'El teléfono debe tener exactamente 10 dígitos.'})

    def validar_cedula_ecuatoriana(self, cedula):
        # Verificar longitud
        if len(cedula) != 10:
            return False

        # Verificar que todos sean dígitos
        if not cedula.isdigit():
            return False

        # Verificar provincia (dos primeros dígitos)
        provincia = int(cedula[:2])
        if provincia < 1 or provincia > 24:
            return False

        # Algoritmo de validación
        coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        total = 0
        
        # Verificar dígito verificador
        for i in range(9):
            valor = int(cedula[i]) * coeficientes[i]
            if valor > 9:
                valor -= 9
            total += valor

        verificador = 10 - (total % 10)
        if verificador == 10:
            verificador = 0

        return verificador == int(cedula[-1])
