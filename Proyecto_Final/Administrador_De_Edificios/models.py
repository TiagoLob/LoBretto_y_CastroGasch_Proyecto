from django.db import models

# Create your models here.

class Edificio(models.Model):

    nombre = models.CharField(max_length=30) 
    calle = models.CharField(max_length=50)
    cantidad_De_Pisos = models.IntegerField()
    cantidad_De_Departamentos = models.IntegerField()
    tiene_SUM = models.BooleanField() 

class Departamento(models.Model):

    en_Edificio = models.CharField(max_length=30) 
    piso_Y_Letra = models.CharField(max_length=3) 
    cantidad_De_Ambientes = models.IntegerField()
    esta_Ocupado = models.BooleanField()

class Inquilino(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    celular = models.IntegerField()
    mail = models.EmailField(max_length=254)
    profesion = models.CharField(max_length=50)
    vive_En_Edificio = models.CharField(max_length=30) 
    vive_En_Departamento = models.CharField(max_length=3) 