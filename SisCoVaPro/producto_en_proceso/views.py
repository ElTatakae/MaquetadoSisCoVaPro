from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class InicioProductoEnProcesoView(TemplateView):
    template_name = 'inicio_producto_en_proceso.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

