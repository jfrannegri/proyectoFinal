from django.urls import path
from appCoderFinal import views

urlpatterns = [
   
    path('inicio', views.inicio, name="Inicio"),
    path('participantes', views.participantes, name="Participantes"),
    path('pacientes', views.pacientes, name="Pacientes"),
    path('medicos', views.medicos, name="Medicos"),
    path('enfermeras', views.enfermeras, name="Enfermeras"),
    
    path('pacienteFormulario', views.pacienteFormulario),
    path('busquedaPaciente', views.busquedaPaciente),
    path('buscarPaciente', views.buscarPaciente),

    path('medicoFormulario', views.medicoFormulario),

    path('enfermeraFormulario', views.enfermeraFormulario),

    
]

 