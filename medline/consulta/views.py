from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from consulta.forms.form_login import UserLogin
from consulta.forms.form_registration import patientRegistration, doctorRegistration

from .models import *
from .filters import EspecialidadeFilter

# Create your views here.

# ------------------------------ Login / Logout

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
    return redirect('home')


# ------------------------------ CRUD Patient

def register_patient(request):
    patient_registration_form = patientRegistration(request.POST or None)
    context = {'patient_registration_form': patient_registration_form}
    if request.method == 'POST':
        if patient_registration_form.is_valid():
            patient_registration_form.save_user()
            
            try:
                username = request.POST.get("username")
                password = request.POST.get("password")
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('consultas')
            except:
                return redirect('home')
       
    return render(request, 'patient_registration_form.html', context)


# ------------------------------ CRUD Doctor 

def register_doctor(request):
    doctor_registration_form = doctorRegistration(request.POST or None)
    context = {'doctor_registration_form': doctor_registration_form}
    if request.method == 'POST':
        if doctor_registration_form.is_valid():
            doctor_registration_form.save_user()
            
            try:
                username = request.POST.get("username")
                password = request.POST.get("password")
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('consultas')
            except:
                return redirect('home')
       
    return render(request, 'doctor_registration_form.html', context)


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

def carrinho(request):
    if request.user.is_authenticated:
        paciente = request.user.pacientes
        compras, created = Compras.objects.get_or_create(id_paciente=paciente, complete=False)
        items = compras.compras_consulta_set.all()
        # cartItems = compras.get_cart_items

    context = {
        'compras':compras
    }
    return render(request, 'carrinho.html', context)
