from django import forms
from django.forms import ValidationError
from django.core.validators import RegexValidator

def solo_caracteres(value):
    if any(char.isdigit() for char in value ):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            params={'valor':value})


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre:", required=False, validators=(solo_caracteres,),
            widget= forms.TextInput(attrs={'class':'form-control input','placeholder':'Ingrese el Nombre..'})
            )
    apellido = forms.CharField(label = "Apellido:", required=False, validators=(solo_caracteres,),
            widget= forms.TextInput(attrs={'class':'form-control input','placeholder':'Ingrese el Apellido...'})
            )
    email = forms.EmailField(label = "Email:", 
            error_messages={
                    'required': 'Por favor completa el campo',                    
                },
            widget= forms.TextInput(attrs={'class':'form-control input','type':'email'})
            )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El número de teléfono debe ingresarse en el formato: '+999999999'. Se permiten hasta 15 dígitos.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    telefono = forms.CharField(label= "Telefono:", validators=[phone_regex],
                widget= forms.NumberInput(attrs={'class':'form-control input','placeholder':'Ingrese el numero...'}))
    comentario = forms.CharField(label="Comentarios:", max_length=500,
            widget=forms.Textarea(attrs={'class':'form-control input','rows':5, 'placeholder':"Dejanos tu comentario..."}))