from django.urls import path, include
from . import views
from .views import operadorView, estadisticoView, crearProductoView

app_name = 'operador'
urlpatterns = [
    path('inicio/', operadorView.as_view(), name='inicio'),
    path('operador/estadisticos/', estadisticoView.as_view(), name='estadisticos'),
    path('operador/crear_producto/', crearProductoView.as_view(), name='crear_producto'),
]
