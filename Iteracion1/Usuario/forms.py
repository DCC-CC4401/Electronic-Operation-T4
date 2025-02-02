from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserModel

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class ModificarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']