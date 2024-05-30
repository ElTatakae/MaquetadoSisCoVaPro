
from django.urls import path
from .views import InicioProductoDistribuido

app_name = 'producto_distribuido'

urlpatterns = [
    path('', InicioProductoDistribuido.as_view(), name='inicio'),

]
