from django.db import models

# Create your models here.
class Metodo(models.Model):
    
    IdMetodo = models.CharField(max_length=4,primary_key=True)
    Nombre = models.CharField(max_length=20)
    Introduccion = models.TextField(default=None)
    ImagenIntroduccion=models.ImageField(upload_to=None,height_field=None,width_field=None,max_length=100,default=None)
    Descripcion = models.TextField(default=None)
    ImagenDescripcion=models.ImageField(upload_to=None,height_field=None,width_field=None,max_length=100,default=None)
    Ejemplos_Practicos = models.TextField(default=None)
    ImagenEjemplos_Practicos =models.ImageField(upload_to=None,height_field=None,width_field=None,max_length=100,default=None)
    def __str__(self):
        return self.Nombre +" "+ self.Introduccion
    

class Practica(models.Model):
    IdPractica=models.CharField(max_length=4,primary_key=True)
    Titulo= models.CharField(max_length=20)
    Contenido= models.TextField(default=None)
    IdMetodo=models.ForeignKey(Metodo,null=False,blank=False,on_delete=models.CASCADE)

