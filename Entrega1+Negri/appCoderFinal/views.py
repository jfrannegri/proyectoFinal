from django.shortcuts import render
from django.http import HttpResponse, response
from appCoderFinal.models import Enfermera, Paciente, Medico

from appCoderFinal.forms import MedicoFormulario, PacienteFormulario, EnfermeraFormulario

# Create your views here.
def busquedaPaciente(request):
   
   return render(request, 'appCoderFinal/busquedaPaciente.html')

def buscarPaciente(request):
    
    respuesta = f"busco a : {request.GET['apellido']}"

    return HttpResponse(response)

def pacienteFormulario(request):

    #obtiene nombrepaciente, obra social y edad
    
    if request.method == "POST":

        miFormulario = PacienteFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
        
            pacienteInsta = Paciente(apellido=informacion["apellido"] ,obrasocial=informacion["obrasocial"] ,edad=informacion["edad"])
            
            pacienteInsta.save() #es el que guarda en BD
            
            return render(request, 'appCoderFinal/inicio.html')
   
    else:
   
        miFormulario = PacienteFormulario()

    #return
    return render(request, 'appCoderFinal/pacienteFormulario.html' ,{"miFormulario":miFormulario})



#MEDICO

def medicoFormulario(request):

    #obtiene nombremedico, especialidad, activo y  fecha de incorporacion
    #     
    if request.method == "POST":

        miFormulario = MedicoFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
           
            medicoInsta = Medico(apellido=informacion["apellido"] ,especialidad=informacion["especialidad"] ,activo=informacion["activo"] ,fechaDeIncorporacion=informacion["fechaDeIncorporacion"]
            )
            
            medicoInsta.save() #es el que guarda en BD
            
            return render(request, 'appCoderFinal/inicio.html')
   
    else:
   
        miFormulario = MedicoFormulario()

    #return
    return render(request, 'appCoderFinal/medicoFormulario.html' ,{"miFormulario":miFormulario})

 #ENFERMERA

def  enfermeraFormulario(request):

    #obtiene nombremedico, especialidad, activo y  fecha de incorporacion
    #     
    if request.method == "POST":

        miFormulario = EnfermeraFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
           
            enfermeraInsta = Enfermera(apellido=informacion["apellido"] ,activo=informacion["activo"] ,profesional=informacion["profesional"] ,fechaDeIncorporacion=informacion["fechaDeIncorporacion"])
            
            enfermeraInsta.save() #es el que guarda en BD
            
            return render(request, 'appCoderFinal/inicio.html')
   
    else:
   
        miFormulario = EnfermeraFormulario()

    #return
    return render(request, 'appCoderFinal/enfermeraFormulario.html' ,{"miFormulario":miFormulario})
    


#vista principal
def inicio(request):
    #return HttpResponse("INICIO")}
    return render(request, 'appCoderFinal/inicio.html')

def participantes(request):
    #return HttpResponse("INICIO")}
    return render(request, 'appCoderFinal/participantes.html')

def pacientes(request):
    #return HttpResponse("INICIO")}
    return render(request, 'appCoderFinal/pacientes.html')

def medicos(request):
    #return HttpResponse("INICIO")}
    return render(request, 'appCoderFinal/medicos.html')
    
def enfermeras(request):
    #return HttpResponse("INICIO")}
    return render(request, 'appCoderFinal/enfermeras.html')   