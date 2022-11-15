from django.forms import ModelForm
from controle.models import Usuarios
from django import forms

class UsuariosForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuarios
        fields = ['email', 'senha', 'nascimento']