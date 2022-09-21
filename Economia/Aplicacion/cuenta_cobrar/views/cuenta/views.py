from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView
from Aplicacion.cuenta_cobrar.models import Cabecera
from Aplicacion.cuenta_cobrar.forms import CabeceraForm


class cobrocuentaListView(ListView):
    template_name = "cobro.html"
    context_object_name = 'cobro'
    model = Cabecera

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(nombre__icontains=query)
        else:
            return self.model.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/'
        context['listar_url'] = '/menu'
        context['titulo'] = 'LISTADO DE CUENTAS X COBRAR'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearCuenta(CreateView):
    model = Cabecera
    template_name = "parte/form.html"
    success_url = reverse_lazy('cuenta_cobrar:cobro')
    form_class = CabeceraForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/cuenta_cobrar/crearcuenta/'
        context['titulo'] = 'Crear Cobro'
        context['url_anterior'] = '/cuenta_cobrar/cobro'
        context['listar_url'] = '/cuenta_cobrar/cobro'
        return context






class crearTemplateView(TemplateView):
    template_name = "parte/cobro_deuda.html"



class interesTemplateView(TemplateView):
    template_name = "parte/interes.html"


