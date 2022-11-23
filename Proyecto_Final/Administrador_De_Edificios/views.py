from django.shortcuts import render

from .models import Edificio, Departamento, Inquilino, Avatar, Noticia

from django.http import HttpResponse

from .forms import UserEditForm

from django.views.generic import ListView

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):

    avatar = Avatar.objects.get(user=request.user)
    return render (request, "inicio.html", {"url": avatar.imagen.url})

class EdificioList(ListView):

    model = Edificio
    template_name = "edificio_list.html"
    context_object_name = "edificios"

class EdificioDetalle(DetailView):

    model = Edificio
    template_name = "edificio_detalle.html"
    context_object_name = "edificio"

class EdificioCreacion(PermissionRequiredMixin,CreateView):

    model = Edificio
    permission_required = 'is_staff'
    template_name = "edificio_crear.html"
    success_url = "/BlogDepAdmin/lista-edificios"
    fields = ['nombre', 'calle', 'cantidad_De_Pisos', 'cantidad_De_Departamentos', 'tiene_SUM']

class EdificioUpdate(PermissionRequiredMixin,UpdateView):

    model = Edificio
    permission_required = 'is_staff'
    template_name = "edificio_modificar.html"
    success_url = "/BlogDepAdmin/lista-edificios"
    fields = ('__all__')

class EdificioDelete(PermissionRequiredMixin,DeleteView):

    model = Edificio
    permission_required = 'is_staff'
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

class DepartamentoCreacion(PermissionRequiredMixin,CreateView):

    model = Departamento
    permission_required = 'is_staff'
    template_name = "departamento_crear.html"
    success_url = "/BlogDepAdmin/lista-departamentos"
    fields = ('__all__')

class DepartamentoUpdate(PermissionRequiredMixin,UpdateView):

    model = Departamento
    permission_required = 'is_staff'
    template_name = "departamento_modificar.html"
    success_url = "/BlogDepAdmin/lista-departamentos"
    fields = ('__all__')

class DepartamentoDelete(PermissionRequiredMixin,DeleteView):

    model = Departamento
    permission_required = 'is_staff'
    template_name = "departamento_borrar.html"
    success_url = "/BlogDepAdmin/lista-departamentos"

class InquilinoList(PermissionRequiredMixin,ListView):

    model = Inquilino
    permission_required = 'is_staff'
    template_name = "inquilino_list.html"
    context_object_name = "inquilinos"

class InquilinoDetalle(PermissionRequiredMixin,DetailView):

    model = Inquilino
    permission_required = 'is_staff'
    template_name = "inquilino_detalle.html"
    context_object_name = "inquilino"

class InquilinoCreacion(PermissionRequiredMixin,CreateView):

    model = Inquilino
    permission_required = 'is_staff'
    template_name = "inquilino_crear.html"
    success_url = "/BlogDepAdmin/lista-inquilinos"
    fields = ('__all__')

class InquilinoUpdate(PermissionRequiredMixin,UpdateView):

    model = Inquilino
    permission_required = 'is_staff'
    template_name = "inquilino_modificar.html"
    success_url = "/BlogDepAdmin/lista-inquilinos"
    fields = ('__all__')

class InquilinoDelete(PermissionRequiredMixin,DeleteView):

    model = Inquilino
    permission_required = 'is_staff'
    template_name = "inquilino_borrar.html"
    success_url = "/BlogDepAdmin/lista-inquilinos"

class NoticiaList(ListView):

    model = Noticia
    template_name = "noticia_list.html"
    context_object_name = "noticias"

class NoticiaDetalle(DetailView):

    model = Noticia
    template_name = "noticia_detalle.html"
    context_object_name = "noticia"

class NoticiaCreacion(PermissionRequiredMixin,CreateView):

    model = Noticia
    permission_required = 'is_staff'
    template_name = "noticia_crear.html"
    success_url = "/BlogDepAdmin/lista-noticias"
    fields = ('__all__')

class NoticiaUpdate(PermissionRequiredMixin,UpdateView):

    model = Noticia
    permission_required = 'is_staff'
    template_name = "noticia_modificar.html"
    success_url = "/BlogDepAdmin/lista-noticias"
    fields = ('__all__')

class NoticiaDelete(PermissionRequiredMixin,DeleteView):

    model = Noticia
    permission_required = 'is_staff'
    template_name = "noticia_borrar.html"
    success_url = "/BlogDepAdmin/lista-noticias"

def login_request(request):

    if request.method == 'POST':

        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username = usuario, password = psw)

            if user:

                login (request, user)
                avatar = Avatar.objects.get(user=request.user)
                return render(request, "inicio.html", {"mensaje": f'Bienvenido {usuario}', "url": avatar.imagen.url})

            else:

                return render(request, "inicio.html", {"mensaje": f'Error, datos incorrectos'})

        return render(request, "inicio.html", {"mensaje": f'Error, formulario invalido'})

    else:

        miFormulario = AuthenticationForm()

        return render(request, "login.html", {"miFormulario": miFormulario})

def register (request):

    if request.method == 'POST':

        miFormulario = UserCreationForm(request.POST)

        if miFormulario.is_valid():

            username = miFormulario.cleaned_data["username"]

            miFormulario.save()

            return render(request, "inicio.html", {"mensaje": f'Usuario {username} creado con exito'})

        else:

            return render(request, "inicio.html", {"mensaje": f'Error al crear el usuario'})

    else:

        miFormulario = UserCreationForm()
        
        return render(request, "registro.html", {"miFormulario": miFormulario})


def editar_perfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.email = informacion['email']
            usuario.set_password(informacion['password1'])

            usuario.save()

            return render(request, "inicio.html", {"mensaje": f'Datos actualizados'})

        return render(request,"editarPerfil.html",{"mensaje": "Contraseñas no coinciden"} )

    else:

        miFormulario = UserEditForm(instance=request.user)

    return render(request, "editarPerfil.html", {"miFormulario": miFormulario, "usuario":usuario})

def terminosYCondiciones(request):

    return render (request, "terminosYCondiciones.html")

def sobreNosotros(request):

    return render (request, "sobreNosotros.html")
