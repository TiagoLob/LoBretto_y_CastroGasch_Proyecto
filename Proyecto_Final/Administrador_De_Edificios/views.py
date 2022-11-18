from django.shortcuts import render

from .models import Edificio, Departamento, Inquilino

from .forms import EdificioFormulario, DepartamentoFormulario, InquilinoFormulario

from django.http import HttpResponse

from django.views.generic import ListView

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def inicio(request):

    return render (request, "inicio.html")

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


class EdificioList(ListView):

    model = Edificio
    template_name = "edificio_list.html"
    context_object_name = "edificios"

class EdificioDetalle(DetailView):

    model = Edificio
    template_name = "edificio_detalle.html"
    context_object_name = "edificio"

class EdificioCreacion(CreateView):

    model = Edificio
    template_name = "edificio_crear.html"
    success_url = "/BlogDepAdmin/lista-edificios"
    fields = ['nombre', 'calle', 'cantidad_De_Pisos', 'cantidad_De_Departamentos', 'tiene_SUM']

class EdificioUpdate(UpdateView):

    model = Edificio
    template_name = "edificio_modificar.html"
    success_url = "/BlogDepAdmin/lista-edificios"
    fields = ('__all__')

class EdificioDelete(DeleteView):

    model = Edificio
    template_name = "edificio_borrar.html"
    success_url = "/BlogDepAdmin/lista-edificios"

class DepartamentoList(ListView):

    model = Departamento
    template_name = "departamento_list.html"
    context_object_name = "departamentos"

class DepartamentoDetalle(DetailView):

    model = Departamento
    template_name = "departamento_detalle.html"
    context_object_name = "departamento"

class DepartamentoCreacion(CreateView):

    model = Departamento
    template_name = "departamento_crear.html"
    success_url = "/BlogDepAdmin/lista-departamentos"
    fields = ('__all__')

class DepartamentoUpdate(UpdateView):

    model = Departamento
    template_name = "departamento_modificar.html"
    success_url = "/BlogDepAdmin/lista-departamentos"
    fields = ('__all__')

class DepartamentoDelete(DeleteView):

    model = Departamento
    template_name = "departamento_borrar.html"
    success_url = "/BlogDepAdmin/lista-departamentos"

class InquilinoList(ListView):

    model = Inquilino
    template_name = "inquilino_list.html"
    context_object_name = "inquilinos"

class InquilinoDetalle(DetailView):

    model = Inquilino
    template_name = "inquilino_detalle.html"
    context_object_name = "inquilino"

class InquilinoCreacion(CreateView):

    model = Inquilino
    template_name = "inquilino_crear.html"
    success_url = "/BlogDepAdmin/lista-inquilinos"
    fields = ('__all__')

class InquilinoUpdate(UpdateView):

    model = Inquilino
    template_name = "inquilino_modificar.html"
    success_url = "/BlogDepAdmin/lista-inquilinos"
    fields = ('__all__')

class InquilinoDelete(DeleteView):

    model = Inquilino
    template_name = "inquilino_borrar.html"
    success_url = "/BlogDepAdmin/lista-inquilinos"
