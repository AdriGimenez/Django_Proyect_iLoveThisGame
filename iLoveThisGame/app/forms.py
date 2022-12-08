from django import forms
from django import forms


class ContactoForms(forms.Form):
    nombre = forms.CharField(label="Nombre:", required=True)
    apellido = forms.CharField(label = "Apellido:", required=True)
    email = forms.EmailField(label = "Email:", required=True)
    telefono = forms.CharField(label= "Telefono:")
    comentario = forms.CharField(label="Comentarios:")