from django.contrib import admin

from consulta.models_login import User
from consulta.models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_full_name')
    fields = (('is_active', 'is_staff', 'is_admin', 'is_superuser'), 'username', ('first_name', 'last_name'),
               'email', 'date_joined', 'last_login', 'password')

admin.site.register(User, UserAdmin)


class PacientesAdmin(admin.ModelAdmin):
    readonly_fields = ['birth', 'cpf']

admin.site.register(Pacientes)


class MedicosAdmin(admin.ModelAdmin):
    readonly_fields = ['birth', 'cpf',  'crm', 'localidade', 'foto']

admin.site.register(Medicos)


admin.site.register(Especialidades)
admin.site.register(Agendas)
admin.site.register(Medicos_especialidade)
admin.site.register(Consultas)
admin.site.register(Compras)
admin.site.register(Compras_consulta)
