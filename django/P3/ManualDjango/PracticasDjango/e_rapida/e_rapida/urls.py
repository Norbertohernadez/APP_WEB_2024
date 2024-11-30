from django.contrib import admin
from django.urls import path, include
from mainapp import views
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
]

handler404=views.redirigir_inicio