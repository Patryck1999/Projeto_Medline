from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    context = {}
    return render(request, 'base.html', context)

def consultas(request):
    context = {}
    return render(request, 'consultas.html', context)