from django.shortcuts import render
from .models import Producto

def index(request):
    return render(request, 'commerce/products_highlights.html')

def lista_productos(request):
    productos = Producto.objects.all() #Obtengo todos los productos de la DB
    return render(request, 'commerce/products_highlights.html', 
        {'productos' : productos}
        )