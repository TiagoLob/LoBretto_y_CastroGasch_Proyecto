from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

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

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget= forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_password(self):

        print("self\n", self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        return password2




