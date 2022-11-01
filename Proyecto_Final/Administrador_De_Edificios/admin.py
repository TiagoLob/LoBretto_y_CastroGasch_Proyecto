from django.contrib import admin

from .models import Edificio, Departamento, Inquilino
# Register your models here.

admin.site.register(Edificio)

admin.site.register(Departamento)

admin.site.register(Inquilino)