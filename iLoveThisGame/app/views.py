from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Articulo, Marca, Categoria
from .forms import ArticuloForm, MarcaForm, CategoriaForm
from django.views import View
from django.views.generic import ListView
from app.forms import ContactoForm, RegistrarUsuarioForm, BuscarForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Vistas publicas
def contact(request):
    if request.method =="POST":
        contacto_form = ContactoForm(request.POST)
        if(contacto_form.is_valid()):
             messages.success(request,'Mensaje enviado con exito')
        else:
            messages.warning(request,'Por favor revisa los errores')
    else:
        contacto_form = ContactoForm()
    return render(request, 'app/pages/contact.html', {'contacto_form':contacto_form})

def buscar(request):
    if request.method =="POST":
        buscar_form = BuscarForm(request.POST)
        texto = request.POST.get("cadenabuscar")

        ## Mostramos una lista de coincidencias
        return render(request,'app/pages/buscar.html', {'cadenabuscar': texto})

    else:
        buscar_form = BuscarForm()

    return render(request,'app/pages/buscar.html', {})

def home(request):
    buscar_form = BuscarForm()
    return render(request, 'app/pages/index.html', {'buscar_form':buscar_form})

def empresa(request):
    return render(request,'app/pages/empresa.html', {})

def category(request, name):
    products = {name: name}
    return render(request,'app/pages/categoria.html', products)

def descripcion(request, id_articulo):
    try:
        articulo = Articulo.objects.get(id=id_articulo)
    except Articulo.DoesNotExist:
        return render(request, 'app/administracion/404_admin.html')
    
    # if request.method == "GET":
    #     formulario = ArticuloForm(instance=articulo)

    return render(request, 'app/pages/descripcion.html', {'articulo': articulo, 'id_articulo': id_articulo})

def oferta(request):
    return render(request,'app/pages/oferta.html', {})

def perfil(request):
    return render(request,'app/pages/perfil.html', {})

### Vistas Protegidas.
def index_administracion(request):
    variable = 'test variable'
    return render(request, 'app/administracion/index_administracion.html', {'variable': variable})

#Login y registracion de nuevos usuarios.
def login(request):
    return render(request,'app/registration/login.html', {})

def iniciar_sesion(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            nxt = request.GET.get("next",None)
            messages.success(request, f' Bienvenido/a {username} !!')
            if nxt is None:
                return redirect('home')
            else:
                return redirect(nxt)
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    form = AuthenticationForm()
    return render(request, 'app/registration/login.html', {'form': form})

def registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'app/registration/registrarse.html', {'form': form})

#Views Articulos 
def articulos_index(request):
    articulos = Articulo.objects.all()
    return render(request, 'app/administracion/articulos/index.html', {'articulos': articulos})

class ArticulosListView(ListView):
    model = Articulo
    context_object_name = 'articulos'
    template_name = 'app/administracion/articulos/index.html'
    ordering = ['id']


class ArticulosView(View):
    form_class = ArticuloForm
    template_name = 'app/administracion/articulos/nuevo.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulos_index')

        return render(request, self.template_name, {'formulario': form})


def articulos_editar(request, id_articulo):
    try:
        articulo = Articulo.objects.get(id=id_articulo)
    except Articulo.DoesNotExist:
        return render(request, 'app/administracion/404_admin.html')
    
    if request.method == "POST":
        formulario = ArticuloForm(request.POST, instance=articulo)
        if formulario.is_valid():
            formulario.save()
            return redirect('articulos_index')
    else:
        formulario = ArticuloForm(instance=articulo)

    return render(request, 'app/administracion/articulos/editar.html', {'formulario': formulario, 'id_articulo': id_articulo})


def articulos_eliminar(request, id_articulo):
    try:
        articulo = Articulo.objects.get(id=id_articulo)
    except Articulo.DoesNotExist:
        return render(request, 'app/administracion/404_admin.html')
    
    try:
        articulo.delete()
    except ValueError as ve:
        messages.error(request=request, message="No se puede borrar")
    return redirect('articulos_index')


#Views Marca
def marcas_index(request):
    marcas = Marca.objects.all()
    return render(request, 'app/administracion/marcas/index.html', {'marcas': marcas})

class MarcasListView(ListView):
    model = Marca
    context_object_name = 'marcas'
    template_name = 'app/administracion/marcas/index.html'
    ordering = ['id']

class MarcasView(View):
    form_class = MarcaForm
    template_name = 'app/administracion/marcas/nuevo.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marcas_index')

        return render(request, self.template_name, {'formulario': form})


def marcas_editar(request, id_marca):
    try:
        marca = Marca.objects.get(id=id_marca)
    except Marca.DoesNotExist:
        return render(request, 'app/administracion/404_admin.html')
    
    if request.method == "POST":
        formulario = MarcaForm(request.POST, instance=marca)
        if formulario.is_valid():
            formulario.save()
            return redirect('marcas_index')
    else:
        formulario = MarcaForm(instance=marca)

    return render(request, 'app/administracion/marcas/editar.html', {'formulario': formulario, 'id_marca': id_marca})


def marcas_eliminar(request, id_marca):
    try:
        marca = Marca.objects.get(id=id_marca)
    except Marca.DoesNotExist:
        return render(request, 'app/administracion/404_admin.html')
    
    try:
        marca.delete()
    except ValueError as ve:
        messages.error(request=request, message="No se puede borrar")
    return redirect('marcas_index')


#Views Categoria
def categorias_index(request):
    categorias = Categoria.objects.all()
    return render(request, 'app/administracion/categorias/index.html', {'categorias': categorias})

class CategoriasListView(ListView):
    model = Categoria
    context_object_name = 'categorias'
    template_name = 'app/administracion/categorias/index.html'
    ordering = ['id']

class CategoriasView(View):
    form_class = CategoriaForm
    template_name = 'app/administracion/categorias/nuevo.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias_index')

        return render(request, self.template_name, {'formulario': form})


def categorias_editar(request, id_categoria):
    try:
        categoria = Categoria.objects.get(id=id_categoria)
    except Categoria.DoesNotExist:
        return render(request, 'app/administracion/404_admin.html')
    
    if request.method == "POST":
        formulario = CategoriaForm(request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm(instance=categoria)

    return render(request, 'app/administracion/categorias/editar.html', {'formulario': formulario, 'id_categoria': id_categoria})


def categorias_eliminar(request, id_categoria):
    try:
        categoria = Categoria.objects.get(id=id_categoria)
    except Categoria.DoesNotExist:
        return render(request, 'app/administracion/404_admin.html')
    
    try:
        categoria.delete()
    except ValueError as ve:
        messages.error(request=request, message="No se puede borrar")
    return redirect('categorias_index')



