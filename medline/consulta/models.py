from django.db import models
from consulta.models_login import User

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

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Medicos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_completo = models.CharField(max_length=100, null=True)
    data_nascimento = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200, null=True)
    cpf = models.CharField(max_length=14, null=True)
    crm = models.CharField(max_length=20, null=True)
    tipos = [('Medico','Medico')]
    tipo = models.CharField(max_length=30,choices=tipos)
    localidade = models.CharField(max_length=50, null=True)
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'


class Especialidades(models.Model):
    especialidade = models.CharField(max_length=50, null=True, blank=True)
    cbo = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.especialidade
    
    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'
    

class Agendas(models.Model):
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'


class Medicos_especialidade(models.Model):
    id_medico = models.ForeignKey(Medicos, on_delete=models.SET_NULL, null=True)
    id_especialidade = models.ForeignKey(Especialidades, on_delete=models.SET_NULL, null=True)
    certificado_especialidade = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'Médico Por Especialidade'
        verbose_name_plural = 'Médicos Por Especialidade'


class Consultas(models.Model):
    id_medicos_especialidade = models.ForeignKey(Medicos_especialidade, on_delete=models.SET_NULL, null=True)
    id_agenda = models.ForeignKey(Agendas, on_delete=models.SET_NULL, null=True)
    tipos = [('Presencial', 'Presencial'), ('Digital', 'Digital')]
    tipos_consulta = models.CharField(max_length=50, choices=tipos)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'


class Compras(models.Model):
    id_paciente = models.ForeignKey(Pacientes, on_delete=models.SET_NULL, null=True)
    data_emissao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class Compras_consulta(models.Model):
    id_compra = models.ForeignKey(Compras, on_delete=models.SET_NULL, null=True)
    id_consulta = models.ForeignKey(Consultas, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Consulta Por Compra'
        verbose_name_plural = 'Consultas Por Compra'
