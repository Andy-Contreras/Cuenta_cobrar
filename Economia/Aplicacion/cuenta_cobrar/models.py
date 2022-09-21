from django.db import models

# Create your models here.


class Cabecera(models.Model):
    nombre= models.CharField(max_length=200, unique=True)
    deuda = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Deuda')
    fecha_cobro = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {} - {}".format(self.nombre,self.deuda,self.estado)

    class Meta:
        verbose_name = "Cabecera"
        verbose_name_plural = "Cabeceras"
        ordering = ('nombre',)
