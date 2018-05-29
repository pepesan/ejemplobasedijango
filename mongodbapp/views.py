from django.shortcuts import render
from django.views.generic.list import ListView
from mongodbapp.models import *
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def list_view(request):
    tools=Tool.objects
    print(tools)
    for t in tools:
        print (t.label)
    template = loader.get_template('mongodbapp/tool_list.html')
    context = {'listado': tools}
    return HttpResponse(template.render(context, request))


def detail_view(request,pk):
    tools=Tool.objects
    print(tools)
    for t in tools:
        print (t.label)
    template = loader.get_template('mongodbapp/tool_list.html')
    context = {'listado': tools}
    return HttpResponse(template.render(context, request))

def edit_view(request):
    tools=Tool.objects
    print(tools)
    for t in tools:
        print (t.label)
    template = loader.get_template('mongodbapp/tool_list.html')
    context = {'listado': tools}
    return HttpResponse(template.render(context, request))
def create_view(request):
    tools=Tool.objects
    print(tools)
    for t in tools:
        print (t.label)
    template = loader.get_template('mongodbapp/tool_list.html')
    context = {'listado': tools}
    return HttpResponse(template.render(context, request))

def delete_view(request):
    tools=Tool.objects
    print(tools)
    for t in tools:
        print (t.label)
    template = loader.get_template('mongodbapp/tool_list.html')
    context = {'listado': tools}
    return HttpResponse(template.render(context, request))