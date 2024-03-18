from django.urls import path
from .views import InicioProductoEnProcesoView

app_name = 'producto_en_proceso'

urlpatterns = [
    path('', InicioProductoEnProcesoView.as_view(), name='inicio'),

]
