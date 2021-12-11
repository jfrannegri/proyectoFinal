from django.http import HttpResponse
from django.http.response import HttpResponsePermanentRedirect
from datetime import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Proyecto final de CODER")

def segundaVista(request):
    return HttpResponse("Segunda vista-----Proyecto final de CODER")

def dia(request):
    variable = datetime.now()
    return HttpResponse(f"Hoy es el día<br> {variable}")

def apellido(request, ape):
    fecha = datetime.now()
    return HttpResponse(f"el profe de apellido {ape} nos dío clase el día {fecha}")

def probandoTemplate(request):

    mejorEstudiante = "FRAN"

    nota = 8.5

    fecha = datetime.now()

    dicc = {"nombre":mejorEstudiante, "nota":nota, "fecha":fecha}

    miHTML = open("C:/Users/Juan Francisco Negri/Desktop/proyectoFinal/proyectoFinal/proyectoFinal/plantillas/template1.html")

    plantilla = Template(miHTML.read())

    miHTML.close()

    miContexto = Context(dicc)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

