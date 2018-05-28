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
def SendJson(request):
    data={'error':'No hay datos'}
    try:
        data = json.loads(request.body)
        print (data)
    except:
        print ('nope')
    return JsonResponse(data)

@csrf_exempt
def sendForm(request):
    data={'error':'No hay datos'}
    try:
        post_data = request.POST
        keys=post_data.keys()

        #print (post_data)
        #print(keys)
        for key in keys:
            #print(post_data[key])
            data[key]=post_data[key]
        del data['error']
    except:
        print ('nope')
    return JsonResponse(data)
