from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pacientes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_completo = models.CharField(max_length=100, null=True)
    data_nascimento = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200, null=True)
    cpf = models.CharField(max_length=14, null=True)
    tipos = [('Paciente', 'Paciente'),]
    tipo = models.CharField(max_length=30,choices=tipos)

    def __str__(self):
        return self.nome_completo

class Medicos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_completo = models.CharField(max_length=100, null=True)
    data_nascimento = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200, null=True)
    cpf = models.CharField(max_length=14, null=True)
    crm = models.CharField(max_length=20, null=True)
    tipos = [('Medico','Medico')]
    tipo = models.CharField(max_length=30,choices=tipos)

    def __str__(self):
        return self.nome_completo

class Especialidades(models.Model):
    especialidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.especialidade

class Medicos_especialidade(models.Model):
    id_medico = models.ForeignKey(Medicos, on_delete=models.SET_NULL, null=True)
    id_especialidade = models.ForeignKey(Especialidades, on_delete=models.SET_NULL, null=True)
    certificado_especialidade = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Compras(models.Model):
    id_paciente = models.ForeignKey(Pacientes, on_delete=models.SET_NULL, null=True)
    data_emissao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Consultas(models.Model):
    id_medicos_especialidade = models.ForeignKey(Medicos_especialidade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)

class Compras_consulta(models.Model):
    id_compra = models.ForeignKey(Compras, on_delete=models.SET_NULL, null=True)
    id_consulta = models.ForeignKey(Consultas, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)