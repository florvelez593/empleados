from django.shortcuts import render
from django.urls.base import reverse_lazy

# Create your views here.
from django.views.generic import( 
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView
    
)

#models
from.models import Empleado

#forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    template_name = "inicio.html"


class ListAllEmpleados(ListView):
    template_name='persona/list_all.html'
    paginate_by=4
    ordering='first_name'
    context_object_name='empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista= Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )     
        return lista
   

class ListByAreaEmpleado(ListView):
    """Lista de empleados de un area"""
    template_name='persona/list_by_area.html'
    context_object_name='empleados'
    
    def get_queryset(self):
        area=self.kwargs['shorname']
        lista= Empleado.objects.filter(
        departamento__shor_name=area
        )
        return lista


class ListaEmpleadoAdmin(ListView):
    template_name='persona/lista_empleados.html'
    paginate_by=10
    ordering='first_name'
    context_object_name='empleados'
    model= Empleado


class ListEmpleadosByWord(ListView):
    """Lista empleados por palabra clave"""
    template_name='persona/by_kword.html'
    context_object_name='empleados'

    def get_queryset(self):
        print('*********')
        palabra_clave = self.request.GET.get("kword",'')
        lista= Empleado.objects.filter(
        first_name = palabra_clave
        )     
        return lista


class ListHabilidadesEmpleados(ListView):
    template_name='persona/habilidades.html'
    context_object_name='habilidades'
    
    def get_queryset(self):
        print('*******')
        palabra=self.request.GET.get("kperson",'') 
        
        empleado=Empleado.objects.get(id=2)
        return empleado.habilidades.all()
        

class EmpleadoDetailView(DetailView):
    model=Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context
    

class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields=[
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url= reverse_lazy('persona_app:empleados_admin')
    

class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url= reverse_lazy('persona_app:empleados_admin')


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    form_class=EmpleadoForm
    model = Empleado
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name=empleado.first_name+' '+empleado.last_name
        empleado.save()
        return super().form_valid(form)
    success_url= reverse_lazy('persona_app:empleados_admin')
    
