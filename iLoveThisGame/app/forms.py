from django import forms
from django.forms import ValidationError
from django.core.validators import RegexValidator
from django.forms import ModelForm
from .models import Articulo, Marca, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
            widget= forms.TextInput(attrs={'class':'form-control input','type':'email', 'placeholder':'Ingrese el email...' })
            )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El número de teléfono debe ingresarse en el formato: '+999999999'. Se permiten hasta 15 dígitos.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    telefono = forms.CharField(label= "Telefono:", validators=[phone_regex],
                widget= forms.NumberInput(attrs={'class':'form-control input','placeholder':'Ingrese el numero...'}))
    comentario = forms.CharField(label="Comentarios:", max_length=500,
            widget=forms.Textarea(attrs={'class':'form-control input','rows':5, 'placeholder':"Dejanos tu comentario..."}))

class BuscarForm(forms.Form):
    cadenabuscar = forms.CharField(required=False, validators=(solo_caracteres,),
            widget= forms.TextInput(attrs={'class':'form-control me-2 buscar-margin','placeholder':'Buscar..', 'aria-label':"Search"})
            )

color_choice = [
        ('', '-Seleccionar Color-'),
        ('Amarillo', 'Amarillo'),
        ('Azul', 'Azul'),
        ('Celeste', 'Celeste'),
        ('Bordo', 'Bordo'),
        ('Rosado', 'Rosado'),
        ('Rojo', 'Rojo'),
        ('Marron', 'Marron'),
        ('Verde', 'Verde'),
        ('Violeta', 'Violeta'),
        ('Naranja', 'Naranja'),
        ('Blanco', 'Blanco'),
        ('Negro', 'Negro'),
        ('Morado', 'Morado'),
        ('Beige', 'Beige'),
        ('Dorado', 'Dorado'),
        ('Plateado', 'Plateado'),
        ('Gris', 'Gris')
    ]

talla_choice = [
        ('', '-Seleccionar Talla-'),
        ('Sin Talla','Sin Talla'),
        ('S', 'S'),
        ('S', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
        ('47', '47'),
        ('48', '48'),
        ('49', '49'),
        ('50', '50')
    ]

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ('nombre',)

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)

class ArticuloForm(ModelForm):
    
    nombre = forms.CharField(max_length=50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Nombre del Articulo'}))
    descripcion = forms.CharField(max_length=250, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Descripcion'}))
    precio = forms.IntegerField(widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Precio'}))
    cantidad = forms.IntegerField(widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Cantidad'}))
    colorPrincipal = forms.ChoiceField(choices=color_choice, initial='', widget = forms.Select(attrs={'class': 'form-control'}))
    talla = forms.ChoiceField(choices=talla_choice, initial='', widget = forms.Select(attrs={'class': 'form-control'}))
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), widget= forms.Select(attrs={'class': 'form-control'}))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget= forms.Select(attrs={'class': 'form-control'}))
        
    class Meta:
        model = Articulo
        fields = '__all__'

class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','email']