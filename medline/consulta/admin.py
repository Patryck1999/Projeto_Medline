from django.contrib import admin

from consulta.models_login import User
from consulta.models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_full_name')
    fields = (('is_active', 'is_staff', 'is_admin', 'is_superuser'),
            ('username'), ('password'),
            ('first_name', 'last_name'),
            ('email'),
            ('date_joined'), ('last_login'))

admin.site.register(User, UserAdmin)


class PacientesAdmin(admin.ModelAdmin):
    fields = (
             'is_active',
             'username', 
             'password',
             ('first_name', 'last_name'),
             'email',
             'birth', 
             'cpf',
            )

admin.site.register(Pacientes, PacientesAdmin)


class MedicosAdmin(admin.ModelAdmin):
    fields = (
                'is_active',
                'username', 
                'password',
                ('first_name', 'last_name'),
                'email',
                'birth', 
                'cpf',
                'crm',
                'foto',              
                )
admin.site.register(Medicos, MedicosAdmin)


admin.site.register(Especialidades)
admin.site.register(Localidades)
admin.site.register(Agendas)
admin.site.register(Medicos_especialidade)
admin.site.register(Compras)
admin.site.register(Compras_consulta)
admin.site.register(Contato_paciente)
