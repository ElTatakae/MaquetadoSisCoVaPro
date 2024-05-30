from django.urls import path
from . import views
from .views import MateriaPrimaView, crearGrupoView, procesosView, productoView, monitoreoView, \
    asignarVariableView, asignarEstandarEquipoView, variableView, RecepcionMateriaPrimaView

app_name = 'materia_prima'

urlpatterns = [
    path('inicio/', MateriaPrimaView.as_view(), name='inicio'),
    path('crear_grupo/', crearGrupoView.as_view(), name='crear_grupo'),
    path('procesos/', procesosView.as_view(), name='procesos'),
    path('registro_usuarios/', views.registroDeLideresYOperadoresView.as_view(),
         name='registroDeLideresYOperadores'),
    path('producto/', productoView.as_view(), name='producto'),
    path('producto/asignar_var', asignarVariableView.as_view(),
         name='asignar_var_producto'),
    path('monitoreo/', monitoreoView.as_view(), name='monitoreo'),
    # cambiar a vista de clase
    path('estadistico/', views.estadistico, name='estadistico'),
    path('equipo/', asignarEstandarEquipoView.as_view(),
         name='asignar_estandar_equipo'),
    path('variable/', variableView.as_view(), name='variable'),
    # Para el gráfico prueba de la vista
    path('get_chart/', views.get_chart, name='get_chart'),
    path('recepcion/', RecepcionMateriaPrimaView.as_view(), name='recepcion_materia_prima'),
]
