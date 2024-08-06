#configuracion redireccionamiento
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('listadoCascadas/', views.listadoCascadas, name='listadoCascadas'),
    path('eliminarCascada/<id>',views.eliminarCascada,name='eliminarCascada'),
    path('nuevaCascada/',views.nuevaCascada, name='nuevaCascada'),
    path('guardarCascada/',views.guardarCascada, name='guardarCascada'),
    path('editarCascada/<id>',views.editarCascada, name='editarCascada'),
    path('procesarActulizacionCascada/',views.procesarActulizacionCascada, name='procesarActulizacionCascada'),
    path('gestionCines/',views.gestionCines, name='gestionCines'), 
    path('guardarCine/',views.guardarCine, name='guardarCine'), 
    path('listadoCines/',views.listadoCines, name='listadoCines'),
    
    path('listadoDirectores/', views.listadoDirectores),
    path('listadoPeliculas/', views.listadoPeliculas),
    path('listadoPais/', views.listadoPais)
]