from rest_framework import viewsets
from .serializers import *
from general.models import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import secrets
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, status
from rest_framework.response import Response

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

    
class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LargeResultsSetPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all() 
    serializer_class = UsuarioSerializer
    pagination_class = LargeResultsSetPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all() 
    serializer_class = CategoriaProductoSerializer
    pagination_class = LargeResultsSetPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all() 
    serializer_class = ProveedorSerializer
    pagination_class = LargeResultsSetPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    pagination_class = LargeResultsSetPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
class EntradaInventarioViewSet(viewsets.ModelViewSet):
    queryset = EntradaInventario.objects.prefetch_related('ID_Proveedor', 'ID_Producto').all() 
    serializer_class = EntradaInventarioSerializer
    pagination_class = LargeResultsSetPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()  
    serializer_class = VentaSerializer
    pagination_class = LargeResultsSetPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
class VentaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = VentaUsuario.objects.all()
    serializer_class = VentaUsuarioSerializer
    pagination_class = LargeResultsSetPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all() 
    serializer_class = DetalleVentaSerializer
    pagination_class = LargeResultsSetPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
