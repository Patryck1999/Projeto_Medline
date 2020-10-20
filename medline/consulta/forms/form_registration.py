# -*- coding:utf-8 -*-

from django import forms
from django.contrib.auth.hashers import make_password

from consulta.models_login import User
# from consulta.models import Pacientes, Medicos
from consulta.models import *


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
        fields = '__all__'
        exclude = ['user_permissions','groups', 'last_login','is_staff', 'is_active', 'is_admin',
                   'is_superuser', 'date_joined','role']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Insira seu nome de usuário'}),
            'password': forms.PasswordInput(attrs={'class': 'inputs', 'placeholder': 'Insira sua senha'}),
            'first_name': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Insira seu primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Insira seu sobrenome'}),
            'email': forms.TextInput(attrs={'class': 'inputs', 'type': 'email', 'placeholder': 'Insira seu email'}),
            'birth': forms.TextInput(attrs={'class': 'inputs', 'type': 'date', 'title': 'Data de Nascimento'}),
            'cpf': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'CPF'}),
            'crm': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'CRM'}),
            'foto': forms.FileInput(attrs={'class': 'inputs'}),
        }


    # Encrypt password before saving it to User Model
    def save_user(self, commit=True):
        user = super(doctorRegistration, self).save(commit=False)
        user.password = make_password(user.password)
        if commit:
            user.save()

        return user

class medicosEspecialidades(forms.ModelForm):

    class Meta:
        model = Medicos_especialidade
        fields = '__all__'
        

        widgets = {
            'id_especialidade': forms.Select(attrs={'class': 'inputs', 'class': 'custom-select'}),
            'preco': forms.TextInput(attrs={'class': 'inputs','class': 'form-control'}),
            'certificado_especialidade': forms.FileInput(attrs={'class': 'inputs','class': 'custom-file-input', 'id':"inputGroupFile01" }),
        }

class agendasForm(forms.ModelForm):

    class Meta:
        model = Agendas
        fields = '__all__'
        

        widgets = {
            'id_medico': forms.Select(attrs={'class':'custom-select'}),
            'id_especialidade': forms.Select(attrs={'class':'form-control'}),
            'tipos_consulta': forms.Select(attrs={'class':'form-control'}),
            'data': forms.TextInput(attrs={'class':'form-control', 'type': 'date'}),
            'hora': forms.TextInput(attrs={'class':'form-control', 'type': 'time'}),
        }

class localidades(forms.ModelForm):

    class Meta:
        model = Localidades
        fields = '__all__'
        

        widgets = {
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
        }