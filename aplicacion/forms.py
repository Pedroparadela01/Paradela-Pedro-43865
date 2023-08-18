from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BuzoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del buzo", max_length=50, required=True)
    color = forms.CharField(label="Color", required=True)
    talle = forms.CharField(label="talle", required=True)

class RemeraForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la remera", max_length=50, required=True)
    color = forms.CharField(label="Color", required=True)
    talle = forms.CharField(label="talle", required=True)

class CargoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del cargo", max_length=50, required=True)
    color = forms.CharField(label="Color", required=True)
    talle = forms.CharField(label="talle", required=True)

class BermudaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la bermuda", max_length=50, required=True)
    color = forms.CharField(label="Color", required=True)
    talle = forms.CharField(label="talle", required=True)

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}   

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name' ] 
        help_texts = { k:"" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True) 