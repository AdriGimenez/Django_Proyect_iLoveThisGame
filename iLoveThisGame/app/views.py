from django.shortcuts import render
from django.contrib import messages


def contact(request):
    return render(request, 'app/pages/contact.html', {})

def home(request):
    return render(request, 'app/pages/index.html', {})

def empresa(request):
    return render(request,'app/pages/empresa.html', {})

def category(request, name):
    products = {name: name}
    return render(request,'app/pages/categoria.html', products)

def descripcion(request, producto):
    unproducto = {producto: producto}
    return render(request,'app/pages/descripcion.html', unproducto)

def oferta(request):
    return render(request,'app/pages/oferta.html', {})




