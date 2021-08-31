from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'first_name',
        'last_name',
        'full_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )
    #
    def full_name(self,obj):
        print(obj.first_name)
        return obj.first_name+'  '+obj.last_name

    search_fields = ('first_name',)
    list_filter=('job','habilidades','departamento')
    #
    filter_horizontal=('habilidades',)

    

admin.site.register(Empleado, EmpleadoAdmin)