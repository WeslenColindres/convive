from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

router = DefaultRouter()
router.register(r'User', UserList)
router.register(r'Usuario', UsuariosViewSet)
router.register(r'CategoriaProducto', CategoriaProductoViewSet)
router.register(r'Proveedor', ProveedorViewSet)
router.register(r'Producto', ProductoViewSet)
router.register(r'EntradaInventario', EntradaInventarioViewSet)
router.register(r'Venta', VentaViewSet)
router.register(r'VentaUsuario', VentaUsuarioViewSet)
router.register(r'DetalleVenta', DetalleVentaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]