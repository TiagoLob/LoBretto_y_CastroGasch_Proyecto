from django.urls import path

from .views import agregarDepartamento, agregarEdificio, agregarInquilino, inicio


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('agregar-edificio', agregarEdificio, name="Agregar-Edificio"),
    path('agregar-departamento', agregarDepartamento, name="Agregar-Departamento"),
    path('agregar-inquilino', agregarInquilino, name = "Agregar-Inquilino"),
]
