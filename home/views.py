from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.http import JsonResponse
import json

"""
def index(request):
    return HttpResponse("Estás en la página principal. </br><a href='/polls'>Enlace a pools</a>")
"""
def index(request):
    titulo=_("Mi título molón")
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


def devuelveJson(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sendjson(request):
    if request.body:
        # Decode data to a dict object
        json_data = json.loads(request.body)

        # Do things with json_data ...
    else:
        json_data={
            'error': "No hay datos"
        }
    return JsonResponse(json_data)