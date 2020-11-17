from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


from consulta.forms.form_login import UserLogin
from consulta.forms.form_registration import *


from .models import *
from .filters import EspecialidadeFilter


from django.http import JsonResponse
import json
import datetime

from .Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# ------------------------------ Login / Logout


def login_request(request):
    pacientes = Pacientes()
    context = {}
    form = UserLogin(request.POST or None)
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            try:
                if request.user.pacientes.role == 'paciente':
                    return redirect('consultas')

            except: 
                if request.user.medicos.role == 'medico':
                    return redirect('perfil_medico')

            
    context['form'] = form
    return render(request, 'login.html', context)


def logout_request(request):
    logout(request)
    return redirect('home')


# ------------------------------ CRUD Patient


def register_patient(request):
    
    if request.method == 'POST':
        patient_registration_form = patientRegistration(request.POST or None)
        if patient_registration_form.is_valid():
            patient_registration_form.save_user()
            service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
            emailMsg = 'Bem vindo a nossa plataforma medline para realizar sua consulta logue na plataforma!'
            mimeMessage = MIMEMultipart()
            destino = request.POST.get("email")
            mimeMessage['to'] = f'{destino}'
            mimeMessage['subject'] = 'Cadastro de Paciente realizado com sucesso!'
            mimeMessage.attach(MIMEText(emailMsg, 'plain'))
            raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

            message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
            print(message)
            
            try:
                username = request.POST.get("username")
                password = request.POST.get("password")
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('consultas')
            except:
                return redirect('home')
    else:
        patient_registration_form = patientRegistration()
    context = {'patient_registration_form': patient_registration_form}
    
    return render(request, 'patient_registration_form.html', context)


# ------------------------------ CRUD Doctor 


def register_doctor(request):    
    if request.method == 'POST':
        doctor_registration_form = doctorRegistration(request.POST or None, request.FILES)  
        if doctor_registration_form.is_valid():
            doctor_registration_form.save_user()
            service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
            emailMsg = 'Bem vindo a nossa plataforma medline para realizar sua consulta logue na plataforma!'
            mimeMessage = MIMEMultipart()
            destino = request.POST.get("email")
            mimeMessage['to'] = f'{destino}'
            mimeMessage['subject'] = 'Cadastro de Medico realizado com sucesso'
            mimeMessage.attach(MIMEText(emailMsg, 'plain'))
            raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

            message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
            print(message)
            
            try:
                username = request.POST.get("username")
                password = request.POST.get("password")
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('especialidades_medicas')
            except:
                return redirect('home')
    else:
        doctor_registration_form = doctorRegistration()
    context = {'doctor_registration_form': doctor_registration_form} 

    return render(request, 'doctor_registration_form.html', context)


# ------------------------------


def home(request):
    context = {}
    return render(request, 'home.html', context)


def perfil_medico(request):
    if request.method == 'POST':
        medicos_especialidades = medicosEspecialidades(request.POST or None, request.FILES)  
        localidade = localidades(request.POST or None, request.FILES)  
        if medicos_especialidades.is_valid() and localidade.is_valid():
            medicos_especialidades.save()
            localidade.save()
            return redirect('consultas_medicas')

    else:
        medicos_especialidades = medicosEspecialidades()
        localidade = localidades()
    context = {
               'medicos_especialidades': medicos_especialidades,
               'localidade':localidade
               } 
    return render(request, 'perfil_medico.html', context)


def consultas_medicas(request):
    if request.method == 'POST':
        agendas_form = agendasForm(request.POST or None)
        if agendas_form.is_valid():
            agendas_form.save()
            return redirect('consultas_medicas')
        
    else:
        agendas_form = agendasForm()
     
    medico = request.user.medicos
    agendas_all = Agendas.objects.all().filter(id_medico=medico)
    medico_especialidade = Medicos_especialidade.objects.all().filter(id_medico=medico)
    context = {'agendas_form':agendas_form,
               'agendas_all':agendas_all,
               'medico_especialidade':medico_especialidade,
              } 

    return render(request, 'consultas_medicas.html', context)


def excluir_horario(request, id):
    agendas_all = Agendas.objects.get(pk=id)
    agendas_all.delete()
    return redirect('consultas_medicas')

def consultas(request):
    if request.user.is_authenticated:
        try:
            if request.user.pacientes.role == 'paciente':
                paciente = request.user.pacientes
                compras, created = Compras.objects.get_or_create(id_paciente=paciente, complete=False)
                items = compras.compras_consulta_set.all()
                cartItems = compras.get_cart_items
        except:
            if request.user.medicos.role == 'medico':
                cartItems = {}
    else:
        cartItems = {}

    
    medicos_especialidade = Medicos_especialidade.objects.all()
    medicos = Medicos.objects.all()


    especialidade_query = request.GET.get('especialidade')
    cidade_query = request.GET.get('cidade')

    if especialidade_query != '' and especialidade_query is not None:
        medicos_especialidade = medicos_especialidade.filter(id_especialidade__especialidade__icontains=especialidade_query)

    if cidade_query != '' and cidade_query is not None:
        medicos_especialidade = medicos_especialidade.filter(id_medico__localidade__icontains=cidade_query)

    context = {
        'medicos_especialidade':medicos_especialidade,
        'cartItems':cartItems,
        'medicos':medicos
        }
    return render(request, 'consultas.html', context)


def detalhes_consulta(request, id):
    if request.user.is_authenticated:
        paciente = request.user.pacientes
        compras, created = Compras.objects.get_or_create(id_paciente=paciente, complete=False)
        items = compras.compras_consulta_set.all()
        cartItems = compras.get_cart_items

    medicos_especialidades_all = Medicos_especialidade.objects.get(id=id)
    medicos_especialidades_diferente = Medicos_especialidade.objects.all()
    medico = medicos_especialidades_all.id_medico.id
    especialidade = medicos_especialidades_all.id_especialidade
    localidades = Localidades.objects.all().filter(user=medico)
    agenda = Agendas.objects.all().filter(id_medico=medico, id_especialidade=especialidade)
    context = {'agenda':agenda,'cartItems':cartItems,'medicos_especialidades_all':medicos_especialidades_all,
               'localidades': localidades}
    
    return render(request, 'detalhes_consulta.html', context)


def excluir_horario(request, id):
    agendas_all = Agendas.objects.get(id=id)
    agendas_all.delete()
    return redirect('consultas_medicas')


def especialidades(request):
    if request.user.is_authenticated:
        paciente = request.user.pacientes
        compras, created = Compras.objects.get_or_create(id_paciente=paciente, complete=False)
        items = compras.compras_consulta_set.all()
        cartItems = compras.get_cart_items

    especialidades = Especialidades.objects.all()
    filtro_especialidade = EspecialidadeFilter(request.GET, queryset=especialidades)
    especialidades = filtro_especialidade.qs

    context={'cartItems':cartItems,'filtro_especialidade':filtro_especialidade,
            'especialidades':especialidades
            }
    return render(request, 'especialidades.html', context)


def cidades(request):
    if request.user.is_authenticated:
        paciente = request.user.pacientes
        compras, created = Compras.objects.get_or_create(id_paciente=paciente, complete=False)
        items = compras.compras_consulta_set.all()
        cartItems = compras.get_cart_items

    localidades = Localidades.objects.all()
    
    context={'cartItems':cartItems,'localidades':localidades}
    return render(request, 'cidades.html', context)
   

def carrinho(request):
    if request.user.is_authenticated:
        paciente = request.user.pacientes
        compras, created = Compras.objects.get_or_create(id_paciente=paciente, complete=False)
        items = compras.compras_consulta_set.all()
        cartItems = compras.get_cart_items

    context = {'compras':compras,'items':items, 'cartItems':cartItems}
    return render(request, 'carrinho.html', context)


def checagem(request):
    if request.user.is_authenticated:
        paciente = request.user.pacientes
        compras = Compras.objects.get(id_paciente=paciente, complete=False)
        items = compras.compras_consulta_set.all()
        cartItems = compras.get_cart_items


    context = {'compras':compras,'items':items, 'cartItems':cartItems}
    return render(request, 'checagem.html', context)

def pedidos(request):
    if request.user.is_authenticated:
        paciente = request.user.pacientes
        compras, created = Compras.objects.get_or_create(id_paciente=paciente, complete=False)
        items = compras.compras_consulta_set.all()
        cartItems = compras.get_cart_items

    paciente = request.user.pacientes
    contato_paciente = Contato_paciente.objects.all().filter(id_paciente=paciente)
    context = {'cartItems':cartItems,'contato_paciente':contato_paciente}
    return render(request, 'pedidos.html', context)

def detalhes_pedido(request, id):
    dados = Contato_paciente.objects.get(id_compra=id)
    cabecalho = 'Medline - O marketpace de consultas médicas'
    titulo = f'pedido_{str(dados.id_compra)}'
    enfeite= 125 * '-'
    subtitulo = 'Resumo do pedido'
    data_compra = f'Data e hora da compra: {str(dados.data_compra.day)}/{str(dados.data_compra.month)}/{str(dados.data_compra.year)} {str(dados.data_compra.hour)}:{str(dados.data_compra.minute)}:{str(dados.data_compra.second)}'
    items = dados.items_pedido
    detalhes_total = "Total da Compra"
    total = dados.total

    buffer = io.BytesIO()

    pdf = canvas.Canvas(buffer)

    pdf.setTitle(titulo)
    pdf.drawString(50, 830, cabecalho)
    pdf.drawString(320, 830, data_compra)
    pdf.drawString(50, 810, enfeite)
    pdf.drawString(50, 800, subtitulo)
    pdf.drawString(50, 780, items)
    pdf.drawString(50, 760, detalhes_total)
    pdf.drawString(50, 750, enfeite)
    pdf.drawString(50, 740, total)

    # Quando acabamos de inserir coisas no pdf
    pdf.showPage()
    pdf.save()

    # Por fim, retornamos o buffer para o inicio do arquivo
    buffer.seek(0)

    # abre o PDF direto no navegador
    return FileResponse(buffer, filename='pedido.pdf')


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    pacientes = request.user.pacientes
    compras, created = Compras.objects.get_or_create(id_paciente=pacientes, complete=False)
    medicos_especialidade = Medicos_especialidade.objects.get(id=productId)
    comprasItem, created = Compras_consulta.objects.get_or_create(id_compra=compras, id_medicos_especialidade=medicos_especialidade)
    
    if action == 'add':
        comprasItem.quantity = 1
    elif action == 'remove':
        comprasItem.quantity = (comprasItem.quantity - 1)
    comprasItem.save()

    if comprasItem.quantity <= 0:
        comprasItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    lista = []
    if request.user.is_authenticated:
        paciente = request.user.pacientes
        compras, created = Compras.objects.get_or_create(id_paciente=paciente, complete=False)
        compras.transaction_id = transaction_id
        compras.complete = True
        items = compras.compras_consulta_set.all()
        total = data['shipping']['total']
        print(total)
        for item in items:
            lista.append(f'{item.id_medicos_especialidade.id_medico}, {item.id_medicos_especialidade.id_especialidade}, {item.id_medicos_especialidade.preco}')
        print(lista)
        
    compras.save()

    Contato_paciente.objects.create(
        id_paciente=paciente,
        id_compra=compras,
        nome_completo=data['shipping']['nome'],
        email=data['shipping']['email'],
        cep=data['shipping']['cep'],
        rua=data['shipping']['rua'],
        bairro=data['shipping']['bairro'],
        cidade=data['shipping']['cidade'],
        estado=data['shipping']['estado'],
        items_pedido=lista,
        total=total,
    )
    return JsonResponse('Payment complete!', safe=False)