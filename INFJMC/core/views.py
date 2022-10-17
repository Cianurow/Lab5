from distutils import core
from django import views
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

menu = "<nav><ul><li><a href=''>Inicio</a></li><li><a href='carreras/'>Carreras</a></li><li><a href='docentes/'>Docentes</a></li></ul></nav>"

def home(request):
    #titulo = "<h1>Informática USM</h1> <hr>" + menu + "<hr> <p>Lorem</p>"
    #return HttpResponse(titulo)
    return render(request, 'core/home.html')


def carreras(request):
    titulo = "<h1>Carreras</h1> <hr> " + menu + " <hr> <p>Lorem</p>"
    return HttpResponse(titulo)

def docentes(request):
    titulo = "<h1>Docentes</h1> <hr> " + menu + " <hr> <p>Lorem</p>"
    return HttpResponse(titulo)