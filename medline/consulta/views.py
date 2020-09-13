from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from consulta.forms.form_login import UserLogin
from django.contrib.auth import logout

from .models import *
from .filters import EspecialidadeFilter

# Create your views here.

# ------------------------------ Register

def login_request(request):
    context = {}
    form = UserLogin(request.POST or None)
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('consultas')
    context['form'] = form
    return render(request, 'login.html', context)


def logout_request(request):
    logout(request)
    return redirect('login')

# ------------------------------


def home(request):
    context = {}
    return render(request, 'home.html', context)

def consultas(request):
    medicos_especialidade = Medicos_especialidade.objects.all()

    especialidades = Especialidades.objects.all()
    filtro_especialidade = EspecialidadeFilter(request.GET, queryset=especialidades)
    especialidades = filtro_especialidade.qs

    context = {
        'filtro_especialidade':filtro_especialidade,
        'especialidades':especialidades,
        'medicos_especialidade':medicos_especialidade,
        }
    return render(request, 'consultas.html', context)
