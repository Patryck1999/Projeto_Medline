from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tipos_usuario(models.Model):
    tipos = [('Medico','Medico'),('Cliente', 'Cliente'),]
    tipo = models.CharField(max_length=30,choices=tipos)

class pacientes(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, )
    nome_completo = models.CharField(max_length=100, null=True, blank=True)
    data_nascimento = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    tipo = models.ForeignKey(tipos_usuario, on_delete=models.CASCADE)

class medicos(models.Model):
    nome_completo = models.CharField(max_length=100, null=True, blank=True)
    data_nascimento = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    crm = models.CharField(max_length=20, null=True)
    certificado_especialidade = models.FileField()
    id_tipo = models.ForeignKey(tipos_usuario, on_delete=models.CASCADE)

class especialidades(models.Model):
    especialidade = models.CharField(max_length=50, null=True, blank=True)

class medicos_especialidade(models.Model):
    id_medico = models.ForeignKey(medicos, on_delete=models.SET_NULL, null=True)
    id_especialidade = models.ForeignKey(especialidades, on_delete=models.SET_NULL, null=True)

class compras(models.Model):
    id_paciente = models.ForeignKey(pacientes, on_delete=models.SET_NULL, null=True)
    data_emissao = models.DateTimeField(auto_now_add=True)

class consultas(models.Model):
    id_medicos_especialidade = models.ForeignKey(medicos_especialidade, on_delete=models.SET_NULL, null=True)

class compras_consulta(models.Model):
    id_compra = models.ForeignKey(compras, on_delete=models.SET_NULL, null=True)
    id_consulta = models.ForeignKey(consultas, on_delete=models.SET_NULL, null=True)
