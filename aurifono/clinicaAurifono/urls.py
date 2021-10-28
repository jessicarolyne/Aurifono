from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscaPaciente, name='buscaPaciente'),
    path('paciente/<int:id>', views.paciente, name='paciente'),
    path('', views.novoPaciente, name='Novo Paciente'),
    path('', views.index, name='index'),
]
