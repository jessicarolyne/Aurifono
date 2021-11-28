from django.urls import path
from . import views
from aurifono.urls import *


urlpatterns = [
    # path('', views.index, name='index'),
    # path("paciente/", views.paciente, name='paciente'),
    # path('verpaciente/<int:pk>/', views.verpaciente, name='verpaciente'),
    # path('editpaciente/<int:pk>/', views.editpaciente, name='editpaciente'),
    # path('updatepaciente/<int:pk>/', views.updatepaciente, name='updatepaciente'),
    # path('deletepaciente/<int:pk>/', views.deletepaciente, name='deletepaciente'),
    path('buscar/', views.buscaPaciente, name='Buscar Paciente'),
    path('paciente/<int:id>', views.paciente, name='paciente'),
    path('novo/', views.novoPaciente, name='Novo Paciente'),
    path('editar/<int:id>', views.editarPaciente, name='Editar Paciente'),
    path('excluir/<int:id>', views.excluirPaciente, name='Editar Paciente'),
    #path("verpaciente/", views.verpaciente, name='verpaciente'),
    

    
]
