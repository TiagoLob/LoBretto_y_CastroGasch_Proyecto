from django import forms

class EdificioFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    calle = forms.CharField(max_length=50)
    cantidad_De_Pisos = forms.IntegerField()
    cantidad_De_Departamentos = forms.IntegerField()
    tiene_SUM = forms.BooleanField(required=False)

class DepartamentoFormulario(forms.Form):

    en_Edificio = forms.CharField(max_length=30)
    piso_Y_Letra = forms.CharField(max_length=3)
    cantidad_De_Ambientes = forms.IntegerField()
    esta_Ocupado = forms.BooleanField(required=False)

class InquilinoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    celular = forms.IntegerField()
    mail = forms.EmailField()
    profesion = forms.CharField(max_length=50)
    vive_En_Edificio = forms.CharField(max_length=30)
    vive_En_Departamento = forms.CharField(max_length=3)