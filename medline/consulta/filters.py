import django_filters

from .models import *

class EspecialidadeFilter(django_filters.FilterSet):
    class Meta:
        model = Especialidades
        fields = '__all__'
        

