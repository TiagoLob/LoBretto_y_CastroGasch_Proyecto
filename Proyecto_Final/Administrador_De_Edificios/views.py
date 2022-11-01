from django.shortcuts import render

from .models import Edificio

from .forms import EdificioFormulario

# Create your views here.

def inicio(request):

    return render (request, "inicio.html")

def agregarDepartamento(request):

    return render (request, "agregarDepartamento.html")

def agregarEdificio(request):

    if request.method == 'POST':

        miFormulario = EdificioFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            edificio = Edificio (nombre=informacion['nombre'], calle=informacion['calle'], cantidad_De_Pisos=informacion['cantidad_De_Pisos'], cantidad_De_Departamentos=informacion['cantidad_De_Departamentos'], tiene_SUM=informacion['tiene_SUM'])

            edificio.save()

            return render(request, "agregadoConExito.html")

    else:

        miFormulario = EdificioFormulario()

    return render (request, "agregarEdificio.html", {"miFormulario":miFormulario})

def agregarInquilino(request):

    return render (request, "agregarInquilino.html") 
