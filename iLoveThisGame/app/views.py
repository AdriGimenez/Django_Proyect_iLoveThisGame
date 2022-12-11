from django.shortcuts import render
from django.contrib import messages

from app.forms import ContactoForm


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




