from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import InicioView, IngresoAdminView


urlpatterns = [
    path('', InicioView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('ingreso_admin/', IngresoAdminView.as_view(), name='ingreso_administrador'),
]
