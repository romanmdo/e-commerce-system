from django.shortcuts import render
from .models import Producto, Marca

def index(request):
    return render(request, 'commerce/products_highlights.html')

def lista_destacados(request):   
    productos = Producto.objects.all() #Obtengo todos los productos de la DB
    marcas = Marca.objects.all() #Obtengo todas las marcas de la DB
    return render(request, 'commerce/products_highlights.html', 
        {'productos' : productos,
        'marcas': marcas
        })