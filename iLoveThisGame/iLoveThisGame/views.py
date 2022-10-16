from django.http import HttpResponse
from django.template import Template, Context

#Views: Es la parte lógica.
#Request: Para realizar peticiones.
#HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

#Esto es una vista
def index (request):
    """
    Se encarga de renderizar el documento html.
    """
    #Abrimos documento que contiene el template.
    plantilla_Externa = open("H:\Mi unidad\Proyectos Web\Prácticas\iLoveThisGame\iLoveThisGame\iLoveThisGame\Templates\index.html")
    #Cargar el documento en una variable de tipo 'Template':
    template = Template(plantilla_Externa.read())
    #Cerrar el documento externo que abrimos:
    plantilla_Externa.close()
    #Crear un contexto:
    contexto = Context()
    #Renderizar el documento:
    documento = template.render(contexto)
    return HttpResponse(documento)