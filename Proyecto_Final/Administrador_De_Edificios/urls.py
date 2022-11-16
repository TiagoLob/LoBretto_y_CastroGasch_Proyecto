from django.urls import path

from .views import agregarDepartamento, agregarEdificio, agregarInquilino, inicio, busquedaDepartamentosPorEdificio,buscar,EdificioList,EdificioDetalle,EdificioCreacion


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('agregar-edificio', agregarEdificio, name="Agregar-Edificio"),
    path('agregar-departamento', agregarDepartamento, name="Agregar-Departamento"),
    path('agregar-inquilino', agregarInquilino, name = "Agregar-Inquilino"),
    path('busqueda-departamentos-por-edificio', busquedaDepartamentosPorEdificio, name = "Busqueda-Departamentos-Por-Edificio"),
    path('buscar', buscar, name = "Buscar"),
    path('lista-edificios', EdificioList.as_view(), name="ListaEdificios"),
    path('detalle-edificio/<pk>', EdificioDetalle.as_view(), name="DetalleEdificio"),
    path('crear-edificio', EdificioCreacion.as_view(), name="CrearEdificio"),
]

