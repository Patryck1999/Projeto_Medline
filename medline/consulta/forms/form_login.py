from django import forms
from consulta.models_login import User


class UserLogin(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }