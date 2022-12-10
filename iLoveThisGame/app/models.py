from django.db import models


class Marca(models.Model):
    nombre = models.CharField( max_length=20, verbose_name='Marca')

    def __str__(self):
        return self.nombre

class Categoria (models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Categoria')

    def __str__(self):
        return self.nombre

class Articulo (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Articulo')
    descripcion = models.TextField(max_length=250, null=True, blank=True, verbose_name='Descripcion')
    precio = models.PositiveIntegerField(verbose_name='Precio')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    colorPrincipal = models.CharField(max_length=10)
    talla = models.CharField(max_length=10)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
