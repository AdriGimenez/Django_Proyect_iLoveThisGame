from django import forms
from django import forms
from django.forms import ModelForm
from .models import Articulo, Marca, Categoria


class ContactoForms(forms.Form):
    nombre = forms.CharField(label="Nombre:", required=True)
    apellido = forms.CharField(label = "Apellido:", required=True)
    email = forms.EmailField(label = "Email:", required=True)
    telefono = forms.CharField(label= "Telefono:")
    comentario = forms.CharField(label="Comentarios:")

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
    