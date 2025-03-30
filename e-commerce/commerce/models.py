from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    imagen = models.ImageField(upload_to="productos/")  # Guarda en MEDIA_ROOT/productos/
    descripcion = models.TextField(blank=True, null=True)


class Marca(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to="marcas/")  # Guarda en MEDIA_ROOT/productos/
