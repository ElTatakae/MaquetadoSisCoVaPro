from django.urls import path
from .views import inicioCalidadView

app_name = 'control_de_calidad'

urlpatterns = [
    path('', inicioCalidadView.as_view(), name='inicio'),
]
