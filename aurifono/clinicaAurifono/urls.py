from django.urls import path, include
from django.urls.conf import include, include
from . import views


urlpatterns = [
<<<<<<< HEAD
    # path('buscar/', views.buscaPaciente, name='Buscar Paciente'),
    # path('buscarProfissional/', views.buscaProfissional, name='Buscar Profissional'),
    # path('paciente/<int:id>', views.paciente, name='paciente'),
    # path('profissional/<int:id>', views.profissional, name='profissional'),
    # path('novo/', views.novoPaciente, name='Novo Paciente'),
    # path('novoProfissional/', views.novoProfissional, name='Novo Profissional'),
    # path('editar/<int:id>', views.editarPaciente, name='Editar Paciente'),
    # path('editarProfissional/<int:id>', views.editarProfissional, name='Editar Profissional'),
    # path('excluir/<int:id>', views.excluirPaciente, name='Editar Paciente'),
    # path('excluirProfissional/<int:id>', views.excluirProfissional, name='Editar Profissional'),
    # path('', views.index, name='index'),
=======
    path('buscar/', views.buscaPaciente, name='Buscar Paciente'),
    path('buscarProfissional/', views.buscaProfissional, name='Buscar Profissional'),
    path('paciente/<int:id>', views.paciente, name='paciente'),
    path('profissional/<int:id>', views.profissional, name='profissional'),
    
    path('comunicoral/<int:id>', views.comunicoral, name='comunicoral'),
    path('novoComunicoral/', views.novoComunicoral, name='Novo Comunicação Oral'),
    path('buscarComunicoral/', views.buscaComunicoral, name='Buscar Comunicacao'),
    path('editarComunicoral/<int:id>', views.editarComunicoral, name='Editar Comunicação Oral'),
    path('excluirComunicoral/<int:id>', views.excluirComunicoral, name='Excluir Comunicação Oral'),
    
    path('tipodevoz/<int:id>', views.tipodevoz, name='tipodevoz'),
    path('novoTipodevoz/', views.novoTipodevoz, name='Novo Aspecto Vocal - Tipo de Voz'),
    path('buscarTipodevoz/', views.buscaTipodevoz, name='Buscar Aspector Vocal - Tipo de Voz'),
    path('editarTipodevoz/<int:id>', views.editarTipodevoz, name='Editar Aspector Vocal - Tipo de Voz'),
    path('excluirTipodevoz/<int:id>', views.excluirTipodevoz, name='Excluir Aspector Vocal - Tipo de Voz'),

    path('novo/', views.novoPaciente, name='Novo Paciente'),
    path('novoProfissional/', views.novoProfissional, name='Novo Profissional'),
    path('editar/<int:id>', views.editarPaciente, name='Editar Paciente'),
    path('editarProfissional/<int:id>', views.editarProfissional, name='Editar Profissional'),
    path('excluir/<int:id>', views.excluirPaciente, name='Editar Paciente'),
    path('excluirProfissional/<int:id>', views.excluirProfissional, name='Editar Profissional'),
    path('', views.index, name='index'),
>>>>>>> origin/master
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
