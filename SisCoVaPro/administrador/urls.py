from django.urls import path
from .views import AdminInicioView, registroEmpresaView, registroAdminView, registroLiderView, crudEmpresaView

app_name = 'administrador'

urlpatterns = [
    path('', AdminInicioView.as_view(), name='inicio_administrador'),
    path('registro_de_empresa/', registroEmpresaView.as_view(), name='registro_empresa'),
    path('registro_de_lider/', registroLiderView.as_view(), name='registro_lider'),
    path('registro_de_admin/', registroAdminView.as_view(), name='registro_de_administrador'),
    path('menu_empresa/', crudEmpresaView.as_view(), name='menu_empresa'),
]
