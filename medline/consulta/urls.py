from django.urls import path
from consulta import views as v


urlpatterns =[
    path('', v.home, name="home"),
    path('login', v.login_request, name='login_request'),
    path('logout/', v.logout_request, name='logout_request'),
    path('cadastro/paciente', v.register_patient, name="register_patient"),
    path('cadastro/paciente', v.register_patient, name="register_doctor"),
    path('consultas/', v.consultas, name="consultas"),
    path('carrinho/', v.carrinho, name="carrinho"),
]
