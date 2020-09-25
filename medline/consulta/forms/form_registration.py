# -*- coding:utf-8 -*-

from django import forms
from django.contrib.auth.hashers import make_password

from consulta.models_login import User
from consulta.models import Pacientes, Medicos


class patientRegistration(forms.ModelForm):

    class Meta:
        model = Pacientes
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'birth',
            'cpf',
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Insira seu nome de usuário'}),
            'password': forms.PasswordInput(attrs={'class': 'inputs', 'placeholder': 'Insira sua senha'}),
            'first_name': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Insira seu primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Insira seu sobrenome'}),
            'email': forms.TextInput(attrs={'class': 'inputs', 'type': 'email', 'placeholder': 'Insira seu email'}),
            'birth': forms.TextInput(attrs={'class': 'inputs', 'type': 'date', 'title': 'Data de Nascimento'}),
            'cpf': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'CPF'}),
        }


    # Encrypt password before saving it to User Model
    def save_user(self, commit=True):
        user = super(patientRegistration, self).save(commit=False)
        user.password = make_password(user.password)
        if commit:
            user.save()

        return user        


class doctorRegistration(forms.ModelForm):

    class Meta:
        model = Medicos
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'birth',
            'cpf',
            'crm',
            'foto',
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Insira seu nome de usuário'}),
            'password': forms.PasswordInput(attrs={'class': 'inputs', 'placeholder': 'Insira sua senha'}),
            'first_name': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Insira seu primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Insira seu sobrenome'}),
            'email': forms.TextInput(attrs={'class': 'inputs', 'type': 'email', 'placeholder': 'Insira seu email'}),
            'birth': forms.TextInput(attrs={'class': 'inputs', 'type': 'date', 'title': 'Data de Nascimento'}),
            'cpf': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'CPF'}),
            'crm': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'CRM'}),
            'foto': forms.TextInput(attrs={'class': 'inputs','type': 'file'}),
        }


    # Encrypt password before saving it to User Model
    def save_user(self, commit=True):
        user = super(doctorRegistration, self).save(commit=False)
        user.password = make_password(user.password)
        if commit:
            user.save()

        return user
