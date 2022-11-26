from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Edificio(models.Model):

    nombre = models.CharField(max_length=30) 
    calle = models.CharField(max_length=50)
    cantidad_De_Pisos = models.IntegerField()
    cantidad_De_Departamentos = models.IntegerField()
    tiene_SUM = models.BooleanField() 

    def __str__(self):
        return f"Nombre: {self.nombre} - Calle: {self.calle} - Cantidad de pisos: {self.cantidad_De_Pisos} - Cantidad de departamentos: {self.cantidad_De_Departamentos} - Tiene Sum (True = Si): {self.tiene_SUM} "

    class Meta:
        ordering = ['nombre']

class Departamento(models.Model):

    en_Edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE) 
    piso_Y_Letra = models.CharField(max_length=3) 
    cantidad_De_Ambientes = models.IntegerField()
    esta_Ocupado = models.BooleanField()

    def __str__(self):
        return f"En edificio: {self.en_Edificio.nombre} - Piso y Letra: {self.piso_Y_Letra} - Cantidad de ambientes: {self.cantidad_De_Ambientes} - Esta Ocupado (True = Si): {self.esta_Ocupado}"

    class Meta:
        ordering = ['en_Edificio', 'piso_Y_Letra']

class Inquilino(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    celular = models.IntegerField()
    mail = models.EmailField(max_length=254)
    profesion = models.CharField(max_length=50)
    vive_En_Edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)
    vive_En_Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
   

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Celular: {self.celular} - Mail: {self.mail} - Profesion: {self.profesion} - Vive en el edificio: {self.vive_En_Edificio.nombre} - Vive en el departamento: {self.vive_En_Departamento.piso_Y_Letra}"

    class Meta:
        ordering = ['vive_En_Edificio','apellido', 'nombre']

class Avatar (models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

class Noticia(models.Model):

    titulo = models.CharField(max_length=254)
    subtitulo = models.CharField(max_length=254)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='noticias')

    class Meta:
        ordering = ['-fecha']

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    mail = models.EmailField()
    texto = models.TextField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Mail: {self.mail}"
