from django.shortcuts import render

# Create your views here.

def index (requets):
    return render(requets,'mainapp/index.html',{
'title':'inicio pagina principal',
'content': '..::Bienvenidoas a mi pagina principal::..'
})


def about(requets):
    mensaje='Estamos aqui para ayudarte en tu desarrollo'
    return render(requets,'mainapp/about.html',{
'title':'Acerca de nosotros',
'content':'..::Somos desarrolladores de SW multiplataformas::..',
'mensaje':mensaje 
})

def vision (request):
    return render(request,'mainapp/vision.html',{
        'title_vision':'Vision'
    })

def mision (request):
    return render(request,'mainapp/vision.html',{
        'title_vision':'Vision'
    })
    