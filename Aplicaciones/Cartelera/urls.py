#configuracion redireccionamiento
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('listadoGeneros/', views.listadoGeneros, name='listadoGeneros'),
    path('eliminarGenero/<id>',views.eliminarGenero,name='eliminarGenero'),
    path('nuevoGenero/',views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero/',views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<id>',views.editarGenero, name='editarGenero'),
    path('procesarActulizacionGenero/',views.procesarActulizacionGenero, name='procesarActulizacionGenero'),
    path('gestionCines/',views.gestionCines, name='gestionCines'), 
    path('guardarCine/',views.guardarCine, name='guardarCine'), 
    path('listadoCines/',views.listadoCines, name='listadoCines'),
    
    path('listadoDirectores/', views.listadoDirectores),
    path('listadoPeliculas/', views.listadoPeliculas),
    path('listadoPais/', views.listadoPais)
]