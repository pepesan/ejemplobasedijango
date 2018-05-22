from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    return HttpResponse("Módulo de libros </br><a href='/libros/create'>Crear nuevo libro</a>")
