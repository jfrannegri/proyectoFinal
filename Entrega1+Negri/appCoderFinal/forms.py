from django import forms
#from django.forms import ModelForm

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