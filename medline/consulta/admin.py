from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(tipos_usuario)
admin.site.register(pacientes)
admin.site.register(medicos)
admin.site.register(especialidades)
admin.site.register(medicos_especialidade)
admin.site.register(compras)
admin.site.register(consultas)
admin.site.register(compras_consulta)
