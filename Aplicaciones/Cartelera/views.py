from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from .models import Cine, Director, Genero, Pelicula, Pais
# controlar mensaje
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")
#renderizando el template de listadoGeneros
def listadoGeneros(request):
    generosBdd=Genero.objects.all()
    return render(request,"listadoGeneros.html",{'generos':generosBdd})
#SE RECIBE EL TD PARA ELIMINAR UN GENERO
def eliminarGenero(request,id):
    generoEliminar=Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request,"Genero eliminado exitosamente")
    return redirect('listadoGeneros')
#Renderizar formulario de nuevo genero
def nuevoGenero(request):
    return render(request, 'nuevoGenero.html')
#insetar generos en la base de datos
def guardarGenero(request):
    nom=request.POST["nombre"]
    des=request.POST["descripcion"]
    fot=request.FILES.get("foto")
    nuevoGenero=Genero.objects.create(nombre=nom,descripcion=des,foto=fot)
    messages.success(request, "Género Registrado Exitosamente")
    return redirect('listadoGeneros')
# renderizar formulario de actualizacion de director
def editarGenero(request,id):
    generoEditar=Genero.objects.get(id=id)
    return render(request,'editarGenero.html',{'generoEditar':generoEditar})
#Actualizando los nuevos datos en la base de datos  de director
def procesarActulizacionGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.save()
    messages.success(request,'Genero actualizado exitosamente.')
    return redirect('listadoGeneros')


#renderizar el template de listadoDirectores
def listadoDirectores(request):
    directoresBdd=Director.objects.all()
    return render(request,"listadoDirectores.html",{'directores':directoresBdd})
#SE RECIBE EL TD PARA ELIMINAR UN DIRECTOR
def eliminarDirectores(request,id):
    directorEliminar=Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request,"Director eliminado exitosamente")
    return redirect('listadoDirectores')
#Renderizar formulario de nuevo director
def nuevoDirector(request):
    return render(request, 'nuevoDirector.html')
#insetar directores en la base de datos
def guardarDirector(request):
    ndi=request.POST["ndi"]
    ape=request.POST["apellido"]
    nom=request.POST['nombre']
    est=request.POST['estado']
    fot=request.FILES.get("foto")
    nuevoDirector=Director.objects.create(ndi=ndi,apellido=ape,nombre=nom,estado=est,foto=fot)
    messages.success(request, "Director Registrado Exitosamente")
    return redirect('listadoDirector')
# renderizar formulario de actualizacion de director
def editarDirector(request,id):
    directorEditar=Director.objects.get(id=id)
    return render(request,'editarDirector.html',{'directorEditar':directorEditar})
#Actualizando los nuevos datos en la base de datos  de director
def procesarActulizacionDirector(request):
    id=request.POST['id']
    dni=request.POST['dni']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    estado=request.POST['estado']
    
    directorConsultado=Director.objects.get(id=id)
    directorConsultado.dni=dni
    directorConsultado.apellido=apellido
    directorConsultado.nombre=nombre
    directorConsultado.estado=estado
    directorConsultado.save()
    messages.success(request,'Director actualizado exitosamente.')
    return redirect('listadoDirectores')




#renderizar el template de listadoPeliculas
def listadoPeliculas(request):
    peliculasBdd=Pelicula.objects.all()
    return render(request,"listadoPeliculas.html",{'peliculas':peliculasBdd})
#renderizar el template de listadoPais
def listadoPais(request):
    paisesBdd=Pais.objects.all()
    return render(request,"listadoPeliculas.html",{'peliculas':paisesBdd})

#Funcion para gestionar el CRUD de Cine
def gestionCines(request):
    cinesBdd=Cine.objects.all()
    return render(request,"gestionCines.html",{'cines':cinesBdd})
#Insertar cine mediante AJAX en la Base de Datos
@csrf_exempt
def guardarCine(request):
    nom=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)    
   
    return JsonResponse(
        {
            'estado': True,
            'mensaje': 'Género registrado exitosamente.'
        }
    )
#Renderizar el listado de cines
def listadoCines(request):
    cines=Cine.objects.all()
    return render(request,"listadoCines.html",
                  {'cine':cines})
    
    