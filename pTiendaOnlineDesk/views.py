from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import *

def search_Articule(request):
    return render(request, "search_articule.html")

def search_ArticulesC(request):
    if request.GET["search"]: #si obtengo una respuesta
        #Utiliza un request para obtener lo que hay en etiqueta de nombre "search" del formulario
        #msm = "El articulo buscado es: %r" %request.GET["search"] 
        producto = request.GET["search"]
        if len(producto)>20:
            msm= "Texto de busqueda demasiado largo"
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "result_search.html", {"articulos":articulos, "query":producto})
        #msm = "El articulo buscado es: %r" %articulos
    else:
        msm = "Debe ingresar un campo a buscar" 
    return HttpResponse(msm)

def contacto (request):
    if request.method == "POST":
        return render(request, "thank_you.html")
    return render(request ,"contacto.html")