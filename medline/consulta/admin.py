from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Pacientes)
admin.site.register(Medicos)
admin.site.register(Especialidades)
admin.site.register(Medicos_especialidade)
admin.site.register(Compras)
admin.site.register(Consultas)
admin.site.register(Compras_consulta)
