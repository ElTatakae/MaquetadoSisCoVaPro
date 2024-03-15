from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.urls import reverse_lazy


class IngresoAdminView(TemplateView):
    template_name = 'ingreso_administrador.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class InicioView(TemplateView):
    template_name = 'inicio.html'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('lider:inicio_lider')
