from django.urls import path
from.views.menu.views import CobroTemplateView
from .views.cuenta.views import cobrocuentaListView, CrearCuenta, crearTemplateView, interesTemplateView,EliminarCuenta

app_name = "cuenta_cobrar"
urlpatterns = [
    path('menu',CobroTemplateView.as_view(), name="menu"),
    path('cobro', cobrocuentaListView.as_view(), name="cobro"),
    path('crearcuenta/',CrearCuenta.as_view(), name="crearcuenta"),
    path('crear', crearTemplateView.as_view(), name="crear"),
    path('eliminar/<int:pk>',EliminarCuenta.as_view(),name="eliminar"),
    path('interes', interesTemplateView.as_view(), name="interes"),

]