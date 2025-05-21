from django import forms
from django.contrib.auth.forms import UserCreationForm

from Usuarios.models import User
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'cedula', 'first_name', 'last_name', 'email', 'telefono', 'password1', 'password2', 'role']
        widgets = {
            'role': forms.HiddenInput(),
        }
        