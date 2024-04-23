from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class InicioProductoDistribuido(TemplateView):
    template_name = 'inicio_distribucion.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

