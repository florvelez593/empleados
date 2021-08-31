from django.contrib import admin
from django.urls import path
from django.views.generic.base import View

from . import views
app_name="persona_app"

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
    ),
    path(
        'lista-by-area/<shorname>/', 
        views.ListByAreaEmpleado.as_view(),
        name ='empleados_areas'
    ),
    path(
        'lista-empleados-admin/', 
        views.ListaEmpleadoAdmin.as_view(),
        name ='empleados_admin'
    ),
    path(
        'buscar-empleado/', 
        views.ListEmpleadosByWord.as_view()
    ),
    path('listar-habilidades-empleados/', views.ListHabilidadesEmpleados.as_view()),
    path(
        'ver-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),
    path(
        'add-empleado',
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
    ),


]
