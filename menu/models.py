from django.db import models
from django.contrib.auth.models import User
from djongo import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title

class Producto(models.Model):
    numeroProducto = models.CharField(max_length=24, primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'

class Orden(models.Model):
    numeroOrden = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField()
    mesa = models.IntegerField()
    mesero = models.IntegerField()
    codigoEstado = models.IntegerField()
    productos = models.ManyToManyField(Producto, through='OrdenProducto', blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numeroOrden

    class Meta:
        db_table = 'orden' 

class OrdenProducto(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE,db_column='numeroOrden')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,db_column='numeroProducto')
    cantidad = models.IntegerField(default=1)
    notas = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.orden} - {self.producto} - {self.cantidad}"
    