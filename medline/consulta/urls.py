from django.urls import path
from consulta import views as v


urlpatterns =[
    path('', v.home, name="home"),
    path('login', v.login_request, name='login_request'),
    path('logout/', v.logout_request, name='logout_request'),
    path('cadastro/paciente', v.register_patient, name="register_patient"),
    path('cadastro/medico', v.register_doctor, name="register_doctor"),
    path('perfil/medico', v.perfil_medico, name="perfil_medico"),
    path('consultas_medicas/', v.consultas_medicas, name="consultas_medicas"),
    path('consultas_medicas/excluir_horario/<int:id>', v.excluir_horario, name="excluir_horario"),
    path('consultas/', v.consultas, name="consultas"),
    path('consultas/detalhes_consulta/<int:id>', v.detalhes_consulta, name="detalhes_consulta"),
    path('especialidades/', v.especialidades, name="especialidades"),
    path('cidades/', v.cidades, name="cidades"),
    path('carrinho/', v.carrinho, name="carrinho"),
    path('update_item/', v.updateItem, name="update_item"),
]
