import django
from django.urls import path
from appCoderFinal import forms, views

#Para el logout
from django.contrib.auth.views import LogoutView

urlpatterns = [  

    path('inicio', views.inicio, name="Inicio"),
    path('participantes', views.participantes, name="Participantes"),
    path('pacientes', views.pacientes, name="Pacientes"),
    path('medicos', views.medicos, name="Medicos"),
    path('enfermeras', views.enfermeras, name="Enfermeras"),
    
    path('pacienteFormulario', views.pacienteFormulario, name="pacienteFormulario"),
    path('busquedaPaciente', views.busquedaPaciente),
    path('buscarPaciente/', views.buscarPaciente),

    path('medicoFormulario', views.medicoFormulario, name="medicoFormulario"),

    path('enfermeraFormulario', views.enfermeraFormulario,name="enfermeraFormulario"),

    path('leerEnfermeras', views.leerEnfermeras, name="LeerEnfermeras"),

    #Clases en vistas

    #PARA CLASES BASADAS EN VISTAS

    path('enfermera/list', views.EnfermeraList.as_view(), name='List2'),
    path(r'^(?P<pk>\d+)$', views.EnfermeraDetalle.as_view(), name='Detail2'),    
    path(r'^nuevo$', views.EnfermeraCreacion.as_view(), name='New2'),
    path(r'^editar/(?P<pk>\d+)$', views.EnfermeraUpdate.as_view(), name='Edit2'),
    path(r'^borrar/(?P<pk>\d+)$', views.EnfermeraDelete.as_view(), name='Delete2'),

    path('paciente/list', views.PacienteList.as_view(), name='List1'),
    path(r'^p(?P<pk>\d+)$', views.PacienteDetalle.as_view(), name='Detail1'),    
    path(r'^nuevop$', views.PacienteCreacion.as_view(), name='New1'),
    path(r'^editarp/(?P<pk>\d+)$', views.PacienteUpdate.as_view(), name='Edit1'),
    path(r'^borrarp/(?P<pk>\d+)$', views.PacienteDelete.as_view(), name='Delete1'),
  
    path('medico/list', views.MedicoList.as_view(), name='List'),
    path(r'^m(?P<pk>\d+)$', views.MedicoDetalle.as_view(), name='Detail'),    
    path(r'^nuevom$', views.MedicoCreacion.as_view(), name='New'),
    path(r'^editarm/(?P<pk>\d+)$', views.MedicoUpdate.as_view(), name='Edit'),
    path(r'^borrarm/(?P<pk>\d+)$', views.MedicoDelete.as_view(), name='Delete'),

    

    #LOGIN

   

    path('login', views.login_request, name="Login"),

    path('register', views.register, name="register"),

    #Logout
    
    path('logout', LogoutView.as_view(template_name='AppCoderFinal/logout.html'), name="Logout"),

    path('editarPerfil', views.editarPerfil, name="editarPerfil"),
    ]
    
   
 

    


    


 