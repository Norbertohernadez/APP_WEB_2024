from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  
        else:
            return HttpResponse("Usuario o contraseña incorrectos.")
    return render(request, 'login.html') 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
def vista_protegida(request):
    return render(request, 'inicio.html')
# Create your views here.
