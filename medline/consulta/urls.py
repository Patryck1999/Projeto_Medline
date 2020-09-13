from django.urls import path
from consulta import views

urlpatterns =[
    path('login', views.login_request, name="login"),
    path('logout/', views.logout_request, name='logout'),
    path('', views.home, name="home"),
    path('consultas/', views.consultas, name="consultas"),
]
