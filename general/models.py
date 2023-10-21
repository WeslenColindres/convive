from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    ID_Usuario = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=200)
    NIT = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)

class CategoriaProducto(models.Model):
    ID_Categoria = models.AutoField(primary_key=True)
    Nombre_Categoria = models.CharField(max_length=100)

class Proveedor(models.Model):
    ID_Proveedor = models.AutoField(primary_key=True)
    Nombre_Proveedor = models.CharField(max_length=100)
    Contacto = models.CharField(max_length=100)
    Teléfono = models.CharField(max_length=15)
    Dirección = models.CharField(max_length=255)

class Producto(models.Model):
    ID_Producto = models.AutoField(primary_key=True)
    Nombre_Producto = models.CharField(max_length=100)
    Descripción = models.TextField()
    Precio_Unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    Cantidad_Stock = models.IntegerField(default=0)
    ID_Categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)

class EntradaInventario(models.Model):
    ID_Entrada  = models.AutoField(primary_key=True)
    ID_Proveedor  = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    ID_Producto  = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad  = models.IntegerField()
    Precio_Compra  = models.DecimalField(max_digits=10, decimal_places=2)
    

class Venta(models.Model):
    ID_Venta = models.AutoField(primary_key=True)
    Fecha_Hora = models.DateTimeField(auto_now_add=True)
    Total = models.DecimalField(max_digits=10, decimal_places=2)

class VentaUsuario(models.Model):
    ID_VentasUsuario = models.AutoField(primary_key=True)
    ID_Venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    ID_Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

class DetalleVenta(models.Model):
    ID_Detalle = models.AutoField(primary_key=True)
    ID_VentasUsuario = models.ForeignKey(VentaUsuario, on_delete=models.CASCADE)
    ID_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    Precio_Unitario = models.DecimalField(max_digits=10, decimal_places=2)


