from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='inicio'),  # Página de inicio, para la ruta '/'
    path('inicio/', views.index, name='inicio'),  # Página de inicio también con '/inicio/'
    path('acercade/', views.about, name='acercade'),
    path('mision/', views.mision, name='mision'),
    path('vision/', views.vision, name='vision'),
]
