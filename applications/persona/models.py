from django.db import models
from django.db.models.fields import CharField
from ckeditor.fields import RichTextField

from applications.departamento.models import Departamento
# Create your models here.
class Habilidades(models.Model):
    habilidad= models.CharField('Habilidad', max_length=50)

    class meta:
        verbose_name= 'Habilidad'
        verbose_name_plural='Habiidades Epleados'

    def __str__(self):
        return str(self.id)+'-'+ self.habilidad


class Empleado(models.Model):
    """Modelo para tabla empleado"""
    JOB_CHOICES=(
    ('0','CONTADOR'),
    ('1','ADMINISTRADOR'),
    ('2', 'ECONOMISTA'),
    ('3','OTROS'),
    )

    #contador
    #administrador
    #economista
    #otro

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('apellido', max_length=60)   
    full_name= models.CharField(
        'nombres Completos',
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='empleado',blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida=RichTextField()



    class meta:
        verbose_name= 'Empleado'
        verbose_name_plural='Empleados de la Empresa'
    #imagen= models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name