from django.urls import path

from .views import inicio, busquedaDepartamentosPorEdificio,buscar,EdificioList,EdificioDetalle,EdificioCreacion,EdificioUpdate,EdificioDelete,DepartamentoList,DepartamentoDetalle,DepartamentoCreacion,DepartamentoUpdate,DepartamentoDelete,InquilinoList,InquilinoDetalle,InquilinoCreacion,InquilinoUpdate,InquilinoDelete


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('busqueda-departamentos-por-edificio', busquedaDepartamentosPorEdificio, name = "Busqueda-Departamentos-Por-Edificio"),
    path('buscar', buscar, name = "Buscar"),
    path('lista-edificios', EdificioList.as_view(), name="ListaEdificios"),
    path('detalle-edificio/<pk>', EdificioDetalle.as_view(), name="DetalleEdificio"),
    path('crear-edificio', EdificioCreacion.as_view(), name="CrearEdificio"),
    path('modificar-edificio/<pk>', EdificioUpdate.as_view(), name="ModificarEdificio"),
    path('borrar-edificio/<pk>', EdificioDelete.as_view(), name="BorrarEdificio"),
    path('lista-departamentos', DepartamentoList.as_view(), name="ListaDepartamentos"),
    path('detalle-departamento/<pk>', DepartamentoDetalle.as_view(), name="DetalleDepartamento"),
    path('crear-departamento', DepartamentoCreacion.as_view(), name="CrearDepartamento"),
    path('modificar-departamento/<pk>', DepartamentoUpdate.as_view(), name="ModificarDepartamento"),
    path('borrar-departamento/<pk>', DepartamentoDelete.as_view(), name="BorrarDepartamento"),
    path('lista-inquilinos', InquilinoList.as_view(), name="ListaInquilinos"),
    path('detalle-inquilino/<pk>', InquilinoDetalle.as_view(), name="DetalleInquilino"),
    path('crear-inquilino', InquilinoCreacion.as_view(), name="CrearInquilino"),
    path('modificar-inquilino/<pk>', InquilinoUpdate.as_view(), name="ModificarInquilino"),
    path('borrar-inquilino/<pk>', InquilinoDelete.as_view(), name="BorrarInquilino"),
]

