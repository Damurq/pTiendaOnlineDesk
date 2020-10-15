from django.contrib import admin
from gestionPedidos.models import Clientes,Articulos,Pedidos

class Articulos_Admin(admin.ModelAdmin):
    search_fields=("seccion","nombre")
    list_filter=("seccion",) 

class Pedidos_Admin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"

#No tienen que ser todas las tablas
admin.site.register(Clientes)
admin.site.register(Articulos,Articulos_Admin)
admin.site.register(Pedidos,Pedidos_Admin)
