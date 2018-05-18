from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Estás en la página principal. </br><a href='/polls'>Enlace a pools</a>")