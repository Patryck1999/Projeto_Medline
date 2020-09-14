from django.urls import path
from consulta import views as v


urlpatterns =[
    path('', v.home, name="home"),
    path('login', v.login_request, name="login"),
    path('logout/', v.logout_request, name='logout'),
    path('consultas/', v.consultas, name="consultas"),
    path('cadastro/usuario', v.user_registration, name="user_registration"),
]
