from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('ingreso.urls')),
    path('administrador/', include('administrador.urls')),
    path('materia_prima/', include('materia_prima.urls')),
    path('producto_en_proceso/', include('producto_en_proceso.urls')),
    path('operador/', include('operador.urls')),
    path('admin/', admin.site.urls),
    path('distribucion/', include('producto_distribuido.urls')),
]
