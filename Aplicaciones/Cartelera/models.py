from django.db import models


#Creando modelo Genero: Terror, Comedia
class Cascada(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    altura=models.BooleanField(default=True)
    agua=models.BooleanField(default=True)
    ubicacion=models.CharField(max_length=150)
    acceso=models.CharField(max_length=75)
    imagen=models.FileField(upload_to='cascadas',null=True,blank=True)
    fecha=models.DateField()
#crear un metodo
    def __str__(self):
        #estructura para fila
        fila="{0}: {1} -{2}"
        return fila.format(self.id,self.nombre,self.altura,self.agua,self.ubicacion,self.acceso)
    
class Director(models.Model):
    id=models.AutoField(primary_key=True)
    dni=models.CharField(max_length=15)
    apellido = models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    estado=models.BooleanField(default=True)
    foto=models.FileField(upload_to='portadas',null=True,blank=True)

    def __str__(self):
            fila="{0}:{1} - {2} - {3} - {4}"
            return fila.format(self.id,self.dni,self.apellido,self.nombre,self.estado)

class Pais (models.Model):
     id=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=50)
     continente=models.CharField(max_length=20)
     capital=models.CharField(max_length=20)
     def __str__(self):
            fila="{0}:{1} - {2} - {3} "
            return fila.format(self.id,self.nombre,self.continente,self.capital) 

class Pelicula(models.Model):
     id=models.AutoField(primary_key=True)
     titulo=models.CharField(max_length=250)
     duracion=models.TimeField(null=True)
     sinopsis=models.TextField()
     genero=models.ForeignKey(Cascada,on_delete=models.CASCADE)
     director=models.ForeignKey(Director,on_delete=models.CASCADE)
     portada=models.FileField(upload_to='portadas',null=True,blank=True)
     def __str__(self):
            fila="{0}:{1}"
            return fila.format(self.id,self.titulo)
        
class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    direccion=models.CharField(max_length=150,default='')
    telefono=models.CharField(max_length=150,default='')
    def _str_(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.direccion)