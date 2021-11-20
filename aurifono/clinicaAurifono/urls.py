from django.urls import path
from django.urls.conf import include, include
from . import views

urlpatterns = [
    path('buscar/', views.buscaPaciente, name='Buscar Paciente'),
    path('buscarProfissional/', views.buscaProfissional, name='Buscar Profissional'),
    path('paciente/<int:id>', views.paciente, name='paciente'),
    path('profissional/<int:id>', views.profissional, name='profissional'),
    path('novo/', views.novoPaciente, name='Novo Paciente'),
    path('novoProfissional/', views.novoProfissional, name='Novo Profissional'),
    path('editar/<int:id>', views.editarPaciente, name='Editar Paciente'),
    path('editarProfissional/<int:id>', views.editarProfissional, name='Editar Profissional'),
    path('excluir/<int:id>', views.excluirPaciente, name='Editar Paciente'),
    path('excluirProfissional/<int:id>', views.excluirProfissional, name='Editar Profissional'),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
