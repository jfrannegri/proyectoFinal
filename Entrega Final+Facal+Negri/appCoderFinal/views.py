from django import http
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, response
from appCoderFinal.models import Enfermera, Paciente, Medico

from appCoderFinal.forms import MedicoFormulario, PacienteFormulario, EnfermeraFormulario, UserRegisterForm, UserEditForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

# TRABAJO SOBRE LA CARGA/MODIFICACÓN DE BASES DE DATOS.

#leer  enfermera(forma atajo django)
class EnfermeraList(ListView):
    model = Enfermera
    template_name = "appCoderFinal/enfermeras_list.html"

#ver enfermera
class EnfermeraDetalle(DetailView):
    model = Enfermera
    template_name = "appCoderFinal/enfermera_detalle.html"

#Crear enfermera
class EnfermeraCreacion(CreateView):
    model = Enfermera
    success_url = "../enfermera/list"
    fields = ["apellido", "activo", "profesional", "fechaDeIncorporacion"]

#Modificar paciente
class EnfermeraUpdate(UpdateView):
    model = Enfermera
    success_url = "../enfermera/list"
    fields = ["apellido", "activo", "profesional", "fechaDeIncorporacion"]

#Eliminar paciente
class EnfermeraDelete(DeleteView):
    model = Enfermera
    success_url = "../enfermera/list"



#leer  paciente(forma atajo django)
class PacienteList(ListView):
    model = Paciente
    template_name = "appCoderFinal/pacientes_list.html"

#ver paciente
class PacienteDetalle(DetailView):
    model = Paciente
    template_name = "appCoderFinal/paciente_detalle.html"

#Crear paciente
class PacienteCreacion(CreateView):
    model = Paciente
    success_url = "../paciente/list"
    fields = ["apellido", "obrasocial", "edad"]

#Modificar paciente
class PacienteUpdate(UpdateView):
    model = Paciente
    success_url = "../paciente/list"
    fields = ["apellido", "obrasocial", "edad"]

#Eliminar paciente
class PacienteDelete(DeleteView):
    model = Paciente
    success_url = "../paciente/list"




#leer  medicos(forma atajo django)
class MedicoList(ListView):
    model = Medico
    template_name = "appCoderFinal/medicos_list.html"

#verr médico
class MedicoDetalle(DetailView):
    model = Medico
    template_name = "appCoderFinal/medico_detalle.html"

#Crear médico
class MedicoCreacion(CreateView):
    model = Medico
    success_url = "../medico/list"
    fields = ["apellido", "especialidad", "activo", "fechaDeIncorporacion"]

#Modificar médico
class MedicoUpdate(UpdateView):
    model = Medico
    success_url = "../medico/list"
    fields = ["apellido", "especialidad", "activo", "fechaDeIncorporacion"]

#Eliminar médico
class MedicoDelete(DeleteView):
    model = Medico
    success_url = "../medico/list"
 









#listar enfermera (forma facil)
@login_required
def leerEnfermeras(request):

    enfermeras = Enfermera.objects.all()

    dir = {"enfermeras":enfermeras} #contexto

    return render(request, "appCoderFinal/leerEnfermeras.html", dir)

     
#busqueda paciente 

def busquedaPaciente(request):
   
   return render(request, 'appCoderFinal/busquedaPaciente.html')

def buscarPaciente(request):
    
    if request.GET["apellido"]: 

        apellido = request.GET["apellido"]

        pacientes = Paciente.objects.filter(apellido__icontains=apellido)

        return render(request, "appCoderFinal/resultadoBusquedaPaciente.html",{"pacientes":pacientes, "apellido":apellido})

    else:

        respuesta = "Cague información"
    
    return HttpResponse(respuesta)
    
    #respuesta = f"busco a : {request.GET['apellido']}"

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


def login_request(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')

            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "appCoderFinal/inicio.html",{"mensaje":f"Hola {usuario}"})

            else:

                return render(request, "appCoderFinal/inicio.html",{"mensaje":f"Datos incorrectos"})


        else:

            return render(request, "appCoderFinal/inicio.html",{"mensaje":f"Formulario incorrecto"})


    form = AuthenticationForm() #formulario vacio para logion

    return render(request, "appCoderFinal/login.html", {"form":form})

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']
                  
                  
                  form.save()
                  
                  return render(request,"appCoderFinal/inicio.html" ,  {"mensaje":f"{username} Creado :)"})


      else:
            #form = UserCreationForm()     
            
              
            form = UserRegisterForm()     

      return render(request,"appCoderFinal/register.html" ,  {"form":form})


#Modificar usuario

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request, "appCoderFinal/inicio.html")
    
    else:

        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "appCoderFinal/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})