from django.views.generic import TemplateView

# Create your views here.


class inicioCalidadView(TemplateView):
    template_name = 'inicio_calidad.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
