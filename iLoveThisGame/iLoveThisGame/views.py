from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

#Views: Es la parte lógica.
#Request: Para realizar peticiones.
#HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

#Esto es una vista
def index (request):
    """
    Se encarga de renderizar el documento html.
    """
    #Abrimos documento que contiene el template.
    plantilla_Externa = open("./iLoveThisGame/Templates/index.html")
    #Cargar el documento en una variable de tipo 'Template':
    template = Template(plantilla_Externa.read())
    #Cerrar el documento externo que abrimos:
    plantilla_Externa.close()
    #Crear un contexto:
    contexto = Context()
    #Renderizar el documento:
    documento = template.render(contexto)
    return HttpResponse(documento)

def contacto(request):
    return render(request, "contacto.html", {})