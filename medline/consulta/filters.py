import django_filters
# from django.forms.widgets import TextInput

from .models import *

class EspecialidadeFilter(django_filters.FilterSet):
    especialidade = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Especialidades
        fields = ['especialidade']
        

