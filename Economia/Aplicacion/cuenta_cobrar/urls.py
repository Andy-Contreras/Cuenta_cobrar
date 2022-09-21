from django.urls import path
from.views.menu.views import CobroTemplateView
from .views.cuenta.views import cobrocuentaListView, CrearCuenta, crearTemplateView, interesTemplateView

app_name = "cuenta_cobrar"
urlpatterns = [
    path('menu',CobroTemplateView.as_view(), name="menu"),
    path('cobro', cobrocuentaListView.as_view(), name="cobro"),
    path('crearcuenta/',CrearCuenta.as_view(), name="crearcuenta"),
    path('crear/<int:pk>', crearTemplateView.as_view(), name="crear"),
    path('interes', interesTemplateView.as_view(), name="interes"),

]