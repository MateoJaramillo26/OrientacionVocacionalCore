from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from Academico.models import Calificacion, Clase
from Usuarios.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'cedula', 'first_name', 'last_name', 'email', 'telefono', 'fecha_nacimiento', 'password1', 'password2', 'role']
        widgets = {
            'role': forms.HiddenInput(),
            'fecha_nacimiento': forms.DateInput(attrs = {'type': 'date'}),
        }
        
        
class CalificacionesForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['estudiante', 'clase', 'nota', 'comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['estudiante'].queryset = User.objects.filter(role='estudiante')
        self.fields['clase'].queryset = Clase.objects.all()
        
