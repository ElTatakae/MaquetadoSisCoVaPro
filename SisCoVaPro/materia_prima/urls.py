from django.urls import path
from . import views
import  materia_prima.views as views


app_name = 'materia_prima'

urlpatterns = [
    path('inicio/', views.VistaHome.as_view(), name='home'),
    path('crear_grupo/', views.crearGrupoView.as_view(), name='crear_grupo'),
    path('procesos/', views.procesosView.as_view(), name='procesos'),
    path('registro_usuarios/', views.registroDeLideresYOperadoresView.as_view(),
         name='registroDeLideresYOperadores'),
    path('producto/', views.productoView.as_view(), name='producto'),
    path('producto/asignar_var', views.asignarVariableView.as_view(),
         name='asignar_var_producto'),
    path('monitoreo/', views.monitoreoView.as_view(), name='monitoreo'),
    # cambiar a vista de clase
    path('estadistico/', views.estadistico, name='estadistico'),
    path('equipo/', views.asignarEstandarEquipoView.as_view(),
         name='asignar_estandar_equipo'),
    path('variable/', views.variableView.as_view(), name='variable'),
    # Para el gráfico prueba de la vista
    path('get_chart/', views.get_chart, name='get_chart'),
    path('recepcion/', views.RecepcionMateriaPrimaView.as_view(), name='recepcion_materia_prima'),
    path('control_de_calidad/', views.ControlCalidadView.as_view(), name='ControlCalidadView'),
    path('almacenamiento/', views.MateriaPrimaAlmacenView.as_view(), name='almacenamieno'),
]
