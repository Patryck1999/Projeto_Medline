# -*- coding:utf-8 -*-

from django import forms
from consulta.models_login import User


class UserRegistration(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'role',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
        ]

        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
