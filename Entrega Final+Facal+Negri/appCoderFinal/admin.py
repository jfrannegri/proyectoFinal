from django.contrib import admin

# Register your models here.

from .models import*

#admin.site.register(Curso)
#admin.site.register(Jugador)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Enfermera)