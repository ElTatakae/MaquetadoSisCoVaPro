from django.views.generic import TemplateView


class AdminInicioView(TemplateView):
    template_name = 'modulo_administrador.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class registroEmpresaView(TemplateView):
    template_name = 'inicio/empresa/registro/registro_de_empresa.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class registroLiderView(TemplateView):
        template_name = 'inicio/empresa/registro/registro_de_lider.html'

        def post(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)


class registroAdminView(TemplateView):
    template_name = 'inicio/administrador/registro/registro_de_administrador.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class crudEmpresaView(TemplateView):
    template_name = 'crud_empresa.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class verEmpresaView(TemplateView):
    template_name = 'inicio/empresa/visualizar/visualizar_empresa.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)




