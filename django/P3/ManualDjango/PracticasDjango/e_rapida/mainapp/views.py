from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/Index.html', {
        'title': 'inicio pagina principal',
        'content': '..::Bienvenidos a mi página principal::..'
    })

def about(request):
    mensaje = 'Estamos aquí para ayudarte en tu desarrollo'
    return render(request, 'mainapp/about.html', {
        'title': 'Acerca de nosotros',
        'content': '..::Somos desarrolladores de SW multiplataformas::..',
        'mensaje': mensaje
    })

def vision(request):
    return render(request, 'mainapp/Vision.html', {
        'title': 'Visión',
        'content': 'soy vision'
        
        
    })

def mision(request):
    return render(request, 'mainapp/Mision.html', {
        'title': 'Misión',
        'content': 'soy mision'
    })


    
