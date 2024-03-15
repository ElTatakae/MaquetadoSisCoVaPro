from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView


class operadorView(TemplateView):
    template_name = 'modulo_operador.html'


class estadisticoView(TemplateView):
    template_name = 'estadistico/estadisticos.html'


class crearProductoView(TemplateView):
    template_name = 'producto/crear_producto.html'
