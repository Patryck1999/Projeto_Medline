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
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
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
            'localidade',
            'foto',
        ]

        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


    # Encrypt password before saving it to User Model
    def save_user(self, commit=True):
        user = super(doctorRegistration, self).save(commit=False)
        user.password = make_password(user.password)
        if commit:
            user.save()

        return user
