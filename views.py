from django.shortcuts import render
from django.http import HttpResponse
from .models import Datos

def home(request):
    return render(request, 'prueba.html') #Los datos se agregan despues del html


def index(request):
    with open("datos.txt", "w") as archivo:
        resultados = archivo.readlines()
    return render(request, "prueba.html", resultados)
