from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('ingreso.urls')),
    path('administrador/', include('administrador.urls')),
    path('lider/', include('lider.urls')),
    path('operador/', include('operador.urls')),
    path('admin/', admin.site.urls),
]
