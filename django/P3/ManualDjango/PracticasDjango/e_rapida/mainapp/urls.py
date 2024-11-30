from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.index, name='inicio'),
    path('inicio/', views.index, name='inicio'),
    path('acercade/', views.about, name="acercade"),
    path('mision/', views.mision, name='mision'),
    path('vision/', views.vision, name='vision'),
    path('login/',views.login_user,name='login'),
    # path('logout/',views.logout_user,name='logout'),
    
]