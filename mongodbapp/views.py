from django.shortcuts import render
from django.views.generic.list import ListView
from mongodbapp.models import *
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ToolForm
from django.views.generic.edit import CreateView

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
    tool=Tool.objects.get(pk=pk)
    print(tool)
    template = loader.get_template('mongodbapp/tool_detail.html')
    context = {'objeto': tool}
    return HttpResponse(template.render(context, request))

def tool_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ToolForm(request.POST)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            tool=Tool(label=form.cleaned_data['label'],description=form.cleaned_data['description'])
            tool.save()
            return HttpResponseRedirect('/mongodb/tool')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ToolForm()
    template = loader.get_template('mongodbapp/tool_form.html')
    context= {'form':form}
    return HttpResponse(template.render(context, request))

def edit_view(request,pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ToolForm(request.POST)
        print(form)
        print(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            tool = Tool.objects.get(pk=pk)
            tool.label=form.cleaned_data['label']
            tool.description = form.cleaned_data['description']
            #Tool(label=form.cleaned_data['label'],description=form.cleaned_data['description'])
            tool.save()
            return HttpResponseRedirect('/mongodb/tool')

    # if a GET (or any other method) we'll create a blank form
    else:
        tool = Tool.objects.get(pk=pk)

        form = ToolForm(initial={'label':tool.label,'description':tool.description})
        print(form)
    template = loader.get_template('mongodbapp/tool_update_form.html')
    context= {'form':form,'pk':pk}
    return HttpResponse(template.render(context, request))

def delete_view(request,pk):
    tools=Tool.objects
    print(tools)
    for t in tools:
        print (t.label)
    template = loader.get_template('mongodbapp/tool_list.html')
    context = {'listado': tools}
    return HttpResponse(template.render(context, request))