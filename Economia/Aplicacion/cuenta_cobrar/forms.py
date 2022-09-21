from django import forms
from django.forms import ModelForm

from Aplicacion.cuenta_cobrar.models import Cabecera


class CabeceraForm(ModelForm):
    class Meta:
        model = Cabecera
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control '}),
            'deuda': forms.NumberInput(attrs={'class':'form-control'}),
            'fecha_cobro': forms.DateInput(format=('%d/%m/%Y'),
                                    attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha', 'type': 'date'}),
        }