from django.shortcuts import render


def contact(request):
    return render(request, 'app/pages/contact.html', {})

def home(request):
    return render(request, 'app/pages/index.html', {})

def empresa(request):
    return render(request,'app/pages/empresa.html', {})

def category(request,name):
    products = {name:'zapatila azul'}
    return render(request,'app/pages/categoria.html', products)

def oferta(request):
    return render(request,'app/pages/oferta.html', {})


