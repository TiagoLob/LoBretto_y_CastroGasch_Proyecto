from django.db import models

# Create your models here.

class Edificio(models.Model):

    nombre = models.CharField(max_length=30) 
    calle = models.CharField(max_length=50)
    cantidad_De_Pisos = models.IntegerField()
    cantidad_De_Departamentos = models.IntegerField()
    tiene_SUM = models.BooleanField() 

    def __str__(self):
        return f"Nombre: {self.nombre} - Calle: {self.calle} - Cantidad de pisos: {self.cantidad_De_Pisos} - Cantidad de departamentos: {self.cantidad_De_Departamentos} - Tiene Sum (True = Si): {self.tiene_SUM} "

class Departamento(models.Model):

    en_Edificio = models.CharField(max_length=30) 
    piso_Y_Letra = models.CharField(max_length=3) 
    cantidad_De_Ambientes = models.IntegerField()
    esta_Ocupado = models.BooleanField()

    def __str__(self):
        return f"En edificio: {self.en_Edificio} - Piso y Letra: {self.piso_Y_Letra} - Cantidad de ambientes: {self.cantidad_De_Ambientes} - Esta Ocupado (True = Si): {self.esta_Ocupado}"

class Inquilino(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    celular = models.IntegerField()
    mail = models.EmailField(max_length=254)
    profesion = models.CharField(max_length=50)
    vive_En_Edificio = models.CharField(max_length=30) 
    vive_En_Departamento = models.CharField(max_length=3) 

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Celular: {self.celular} - Mail: {self.mail} - Profesion: {self.profesion} - Vive en el edificio: {self.vive_En_Edificio}, Vive en el departamento: {self.vive_En_Departamento}"