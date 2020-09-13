from django.urls import path
from consulta import views as v


urlpatterns =[
    path('login', v.login_request, name="login"),
    path('logout/', v.logout_request, name='logout'),
    path('', v.home, name="home"),
    path('consultas/', v.consultas, name="consultas"),
]
