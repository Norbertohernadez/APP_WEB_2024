from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    return render(request, "mainapp/index.html", {
        'title':'Inicio ',
        'content':'Bienvenido al inicio'} )
    
def about(request):
    return render(request, "mainapp/about.html", {
        'title':'Acerca de ',
        'content':'Soy Acerca de '} )
    
def mision(request):
    return render(request, "mainapp/mision.html", {
        'title':'Mision ',
        'content':'Soy Misión '} )

def vision(request):
    return render(request, "mainapp/vision.html", {
        'title':'Visión',
        'content':'Soy Visión '} )
    
#def redirigir_inicio(request, exception=None):
#   return redirect('inicio/')

def redirigir_inicio(request, exception):
    return render(request,'mainapp/404.html')

def login_user(request):
    if request.user.is_authenticated:
       return redirect('inicio')
    else:  
     if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
           login(request,user)
           messages.success(request,"¡Bienvenido al Inicio de Sesion!")
           return redirect('inicio')
        else:
           messages.success(request,"No es posible iniciar sesion,por favor ingresa tus credenciales de acceso")

     return render(request, "user/login.html", {
        'title':'Inicio de sesion',
        } )
    
def logout_user(request):
   logout(request)
   return redirect ('login')
 
    
