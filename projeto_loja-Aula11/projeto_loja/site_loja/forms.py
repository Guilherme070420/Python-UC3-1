# site_loja/forms.py - Aula 10

from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagem']


