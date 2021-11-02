from django.urls import path
from django.urls.conf import include, include
from . import views

urlpatterns = [
    path('buscar/', views.buscaPaciente, name='Buscar Paciente'),
    path('paciente/<int:id>', views.paciente, name='paciente'),
    path('novo/', views.novoPaciente, name='Novo Paciente'),
    path('editar/<int:id>', views.editarPaciente, name='Editar Paciente'),
    path('excluir/<int:id>', views.excluirPaciente, name='Editar Paciente'),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
