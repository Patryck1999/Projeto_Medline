from django.urls import path
from consulta import views as v


urlpatterns =[
    path('', v.home, name="home"),
    path('cadastro/usuario', v.user_registration, name="user_registration"),
    path('login', v.login_request, name='login_request'),
    path('logout/', v.logout_request, name='logout_request'),
    path('consultas/', v.consultas, name="consultas"),
    path('especialidades/', v.especialidades, name="especialidades"),
    path('cidades/', v.cidades, name="cidades"),
    path('carrinho/', v.carrinho, name="carrinho"),
    path('update_item/', v.updateItem, name="update_item"),

]
