from django.urls import path
from consulta import views as v


urlpatterns =[
    path('', v.home, name="home"),
    path('login', v.login_request, name='login_request'),
    path('logout/', v.logout_request, name='logout_request'),
    path('cadastro/paciente', v.register_patient, name="register_patient"),
    path('cadastro/medico', v.register_doctor, name="register_doctor"),
    path('consultas/', v.consultas, name="consultas"),
    path('especialidades/', v.especialidades, name="especialidades"),
    path('cidades/', v.cidades, name="cidades"),
    path('especialidades_medicas/', v.especialidades_medicas, name="especialidades_medicas"),
    path('carrinho/', v.carrinho, name="carrinho"),
    path('update_item/', v.updateItem, name="update_item"),
    
]
