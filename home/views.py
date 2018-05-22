from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

"""
def index(request):
    return HttpResponse("Estás en la página principal. </br><a href='/polls'>Enlace a pools</a>")
"""
def index(request):
    titulo="Mi título molón"
    template = loader.get_template('home/index.html')
    context = {'titulo': titulo}
    return HttpResponse(template.render(context, request))


def detail(request,n):
    template = loader.get_template('home/detail.html')
    context={
        'n':n,
        'param_post': request.POST,
    }
    return HttpResponse(template.render(context, request))


def nombre(request,nombre):
    template = loader.get_template('home/nombre.html')
    context = {
        'nombre': nombre
    }
    return HttpResponse(template.render(context, request))