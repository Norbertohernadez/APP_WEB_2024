from django.urls import path
from . import views

urlpatterns = [
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('inicio/', views.vista_protegida, name='inicio'),
    path('', views.vista_protegida, name='home'),
]
