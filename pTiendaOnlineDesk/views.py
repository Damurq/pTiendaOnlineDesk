from django.shortcuts import render
from django.http import HttpResponse

def search_Articule(request):
    return render(request, "search_articule.html")

def search_ArticulesC(request):
    msm = "El articulo buscado es: %r" %request.GET["search"]
    return HttpResponse(msm)