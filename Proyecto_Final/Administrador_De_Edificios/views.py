from django.shortcuts import render

from .models import Edificio, Departamento, Inquilino

from .forms import EdificioFormulario, DepartamentoFormulario, InquilinoFormulario

from django.http import HttpResponse

# Create your views here.

def inicio(request):

    return render (request, "inicio.html")

def agregarDepartamento(request):

    if request.method == 'POST':

        miFormulario = DepartamentoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            departamento = Departamento (en_Edificio=informacion['en_Edificio'], piso_Y_Letra=informacion['piso_Y_Letra'], cantidad_De_Ambientes=informacion['cantidad_De_Ambientes'], esta_Ocupado=informacion['esta_Ocupado'])

            departamento.save()

            return render(request, "agregadoConExito.html")

    else:

        miFormulario = DepartamentoFormulario()

    return render (request, "agregarDepartamento.html", {"miFormulario":miFormulario})

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

    if request.method == 'POST':

        miFormulario = InquilinoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            inquilino = Inquilino (nombre=informacion['nombre'], apellido=informacion['apellido'], celular=informacion['celular'], mail=informacion['mail'], profesion=informacion['profesion'], vive_En_Edificio=informacion['vive_En_Edificio'], vive_En_Departamento=informacion['vive_En_Departamento'])

            inquilino.save()

            return render(request, "agregadoConExito.html")
    
    else:
        
        miFormulario = InquilinoFormulario()

    return render (request, "agregarInquilino.html", {"miFormulario": miFormulario})

def busquedaDepartamentosPorEdificio(request):

    return render (request, "busquedaDepartamentosPorEdificio.html")

def buscar(request):

    if request.GET["edificio"]:

        edificio = request.GET['edificio']
        departamentos = Departamento.objects.filter(en_Edificio__icontains=edificio)

        return render (request, "resultadosBusqueda.html", {"departamentos":departamentos, "edificio":edificio})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)




