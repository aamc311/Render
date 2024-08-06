from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from .models import Cine, Director, Cascada, Pelicula, Pais
# controlar mensaje
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")
#renderizando el template de listadoGeneros
def listadoCascadas(request):
    cascadasBdd=Cascada.objects.all()
    return render(request,"listadoCascadas.html",{'cascadas':cascadasBdd})
#SE RECIBE EL TD PARA ELIMINAR UN GENERO
def eliminarCascada(request,id):
    cascadaEliminar=Cascada.objects.get(id=id)
    cascadaEliminar.delete()
    messages.success(request,"Cascada eliminada exitosamente")
    return redirect('listadoCascadas')
#Renderizar formulario de nuevo genero
def nuevaCascada(request):
    return render(request, 'nuevaCascada.html')
#insetar generos en la base de datos
def guardarCascada(request):
    nom=request.POST["nombre"]
    alt=request.POST["altura"]
    agu=request.POST["agua"]
    ubi=request.POST["ubicacion"]
    acc=request.POST["acceso"]
    img=request.FILES.get("imagen")
    fec=request.POST["fecha"]
    nuevaCascada=Cascada.objects.create(nombre=nom,altura=alt,agua=agu,ubicacion=ubi,acceso=acc,imagen=img,fecha=fec)
    messages.success(request, "Cascada Registrado Exitosamente")
    return redirect('listadoCascadas')
# renderizar formulario de actualizacion de director
def editarCascada(request,id):
    cascadaEditar=Cascada.objects.get(id=id)
    return render(request,'editarCascada.html',{'cascadaEditar':cascadaEditar})
#Actualizando los nuevos datos en la base de datos  de director
def procesarActulizacionCascada(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    altura=request.POST['altura']
    agua=request.POST['agua']
    ubicacaion=request.POST['ubicacaion']
    altura=request.POST['altura']
    agua=request.POST['agua']
    ubicacion=request.POST['ubicacion']
    acceso=request.POST['acceso']
    fecha=request.POST['fecha']
    cascadaConsultado=Cascada.objects.get(id=id)
    cascadaConsultado.nombre=nombre
    cascadaConsultado.altura=altura
    cascadaConsultado.agua=agua
    cascadaConsultado.ubicacion=ubicacion
    cascadaConsultado.acceso=acceso
    cascadaConsultado.fecha=fecha
    cascadaConsultado.save()
    messages.success(request,'Cascada actualizado exitosamente.')
    return redirect('listadoCascadas')


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
    
    