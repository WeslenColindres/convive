from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from general.models import *
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        
        :param value: password of a user
        :return: hashed version of a password
        """
        return make_password(value)
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'
        
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = '__all__'
        
class EntradaInventarioSerializer(serializers.ModelSerializer):
    
    ID_Proveedor = ProveedorSerializer()
    ID_Producto = ProductoSerializer()
    
    class Meta:
        model = EntradaInventario
        fields = '__all__'
        
    def create(self, validated_data):
        proveedor_data = validated_data.pop('ID_Proveedor')
        producto_data = validated_data.pop('ID_Producto')

        proveedor, _ = Proveedor.objects.get_or_create(**proveedor_data)
        producto, created = Producto.objects.get_or_create(**producto_data)
        if not created:
            cantidad_total_previa = producto.Cantidad_Stock
            cantidad_nueva = validated_data['Cantidad']
            precio_compra_nuevo = validated_data['Precio_Compra']

            if cantidad_total_previa > 0:
                precio_promedio_ponderado = (
                    (producto.Precio_Unitario * cantidad_total_previa) + 
                    (precio_compra_nuevo * cantidad_nueva)
                ) / (cantidad_total_previa + cantidad_nueva)
            else:
                precio_promedio_ponderado = precio_compra_nuevo

 
            producto.Precio_Unitario = precio_promedio_ponderado

            producto.Cantidad_Stock += cantidad_nueva
            producto.save()

        # Luego, crea la EntradaInventario
        entrada_inventario = EntradaInventario.objects.create(ID_Proveedor=proveedor, ID_Producto=producto,**validated_data)
        return entrada_inventario
        
class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'
        
class VentaUsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VentaUsuario
        fields = '__all__'
        
class DetalleVentaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DetalleVenta
        fields = '__all__'

