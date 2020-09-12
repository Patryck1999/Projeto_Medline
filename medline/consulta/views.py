from django.shortcuts import render
from .models import *

from .filters import EspecialidadeFilter
# Create your views here.

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
