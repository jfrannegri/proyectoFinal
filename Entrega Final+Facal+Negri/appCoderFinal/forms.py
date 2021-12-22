from django import forms
import datetime
#from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserEditForm(UserCreationForm):
   
    email = forms.EmailField(label="Ingrese su email: ")
    password1 = forms.CharField(label='Contraseña') 
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 


    class Meta:
        model = User
        fields = ['email', 'password1', 'password2'] 
        
        #Saca los mensajes de ayuda
        #help_texts = {k:"" for k in fields}




class UserRegisterForm(UserCreationForm):

    #Obligatorios
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
   #Extra
    last_name = forms.CharField()
    first_name = forms.CharField()
    #imagen_avatar = forms.ImageField(required=False)

   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}




class PacienteFormulario(forms.Form):
    apellido = forms.CharField(required=True)
    obrasocial  =  forms.CharField() 
    edad  = forms.IntegerField()

class MedicoFormulario(forms.Form):
    apellido = forms.CharField(max_length=40)
    especialidad  =  forms.CharField(max_length=40) 
    activo  =  forms.BooleanField()
    fechaDeIncorporacion = forms.DateField()

class EnfermeraFormulario(forms.Form):
    apellido = forms.CharField(max_length=40) 
    activo  =  forms.BooleanField()
    profesional = forms.BooleanField()
    fechaDeIncorporacion = forms.DateField()