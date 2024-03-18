from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import JsonResponse
from random import randrange


class MateriaPrimaView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/login/'

    def get(self, request):
        return render(request, 'modulo_materia_prima.html')


class crearGrupoView(TemplateView):
    template_name = 'grupo/crear_grupo.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class registroDeLideresYOperadoresView(TemplateView):
    template_name = 'registro/registro_usuarios.html'

    def post(self, request, *args, **kwargs):
        # Aquí va tu lógica para manejar la solicitud POST
        return super().get(request, *args, **kwargs)


class procesosView(TemplateView):
    template_name = 'proceso/procesos.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class productoView(TemplateView):
    template_name = 'producto/producto.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class monitoreoView(TemplateView):
    template_name = 'monitoreo/monitoreo.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


def estadistico(request):
    return render(request, 'estadistico/estadistico.html')
   
def get_chart(_request):
    
    colors = ['red', 'blue', 'green', 'yellow', 'black', 'orange']
    randomColor=colors[randrange(0, (len(colors)-1))];
    serie = []
    counter = 0
    while (counter < 6):
        serie.append(randrange(100, 400))
        counter += 1

    chart = {
        'tooltip': {
            'show': True,
            'trigger': 'axis',
            'triggerOn': 'mousemove|click',
            },
        'xAxis': [
            {

                'type': "category",
                'data': ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
            }
        ],
        'yAxis': [
            {
                'type': "value"
            }
        ],
        'series': [{
            'data': serie,
            'type': 'line',
            'itemStyle': {
                'color': randomColor
            },
            'lineStyle': {
                   'color': randomColor
            }
        }]
    }
    return JsonResponse(chart)


class asignarVariableView(TemplateView):
    template_name = 'producto/asignar_variable_producto.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class asignarEstandarEquipoView(TemplateView):
    template_name = 'equipo/asignar_estandar_equipo.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class variableView(TemplateView):
    template_name = 'variable/variable.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class RecepcionMateriaPrimaView(TemplateView):
    template_name = 'recepcion_materia_prima/recepcion.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
