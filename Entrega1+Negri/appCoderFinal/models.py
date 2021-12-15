from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = IntegerField()
    def __str__(self):
        
        return f"Curso: {self.nombre} Camada: {self.camada}"

class Jugador(models.Model):
    apellido = models.CharField(max_length=40)
    numero  = IntegerField() 
    esBueno = models.BooleanField()

class Paciente(models.Model):
    apellido = models.CharField(max_length=40)
    obrasocial  =  models.CharField(max_length=40) 
    edad  = models.IntegerField() 

class Medico(models.Model):
    apellido = models.CharField(max_length=40)
    especialidad  =  models.CharField(max_length=40) 
    activo  =  models.BooleanField()
    fechaDeIncorporacion = models.DateField()

class Enfermera(models.Model):
    apellido = models.CharField(max_length=40) 
    activo  =  models.BooleanField()
    profesional = models.BooleanField()
    fechaDeIncorporacion = models.DateField()
