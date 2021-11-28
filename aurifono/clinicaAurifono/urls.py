from django.urls import path
from django.urls.conf import include, include
from . import views

urlpatterns = [
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
    
    path('ressonancia/<int:id>', views.ressonancia, name='ressonancia'),
    path('novoRessonancia/', views.novoRessonancia, name='Novo Aspecto Vocal - Ressoancia'),
    path('buscarRessonancia/', views.buscaRessonancia, name='Buscar Aspector Vocal - Ressonancia'),
    path('editarRessonancia/<int:id>', views.editarRessonancia, name='Editar Aspector Vocal - Ressonancia'),
    path('excluirRessonancia/<int:id>', views.excluirRessonancia, name='Excluir Aspector Vocal - Ressonancia'),
    
    path('ataquevocal/<int:id>', views.ataquevocal, name='ataquevocal'),
    path('novoAtaquevocal/', views.novoAtaquevocal, name='Novo Aspecto Vocal - Ataque Vocal'),
    path('buscarAtaquevocal/', views.buscaAtaquevocal, name='Buscar Aspector Vocal - Ataque Vocal'),
    path('editarAtaquevocal/<int:id>', views.editarAtaquevocal, name='Editar Aspector Vocal - Ataque Vocal'),
    path('excluirAtaquevocal/<int:id>', views.excluirAtaquevocal, name='Excluir Aspector Vocal - Ataque Vocal'),
    
    path('pitch/<int:id>', views.pitch, name='pitch'),
    path('novoPitch/', views.novoPitch, name='Novo Aspecto Vocal - Pitch'),
    path('buscarPitch/', views.buscaPitch, name='Buscar Aspector Vocal - Pitch'),
    path('editarPitch/<int:id>', views.editarPitch, name='Editar Aspector Vocal - Pitch'),
    path('excluirPitch/<int:id>', views.excluirPitch, name='Excluir Aspector Vocal - Pitch'),
    
    path('loudness/<int:id>', views.loudness, name='loudness'),
    path('novoLoudness/', views.novoLoudness, name='Novo Aspecto Vocal - Loudness'),
    path('buscarLoudness/', views.buscaLoudness, name='Buscar Aspector Vocal - Loudness'),
    path('editarLoudness/<int:id>', views.editarLoudness, name='Editar Aspector Vocal - Loudness'),
    path('excluirLoudness/<int:id>', views.excluirLoudness, name='Excluir Aspector Vocal - Loudness'),
    
    path('modulacao/<int:id>', views.modulacao, name='modulacao'),
    path('novoModulacao/', views.novoModulacao, name='Novo Aspecto Vocal - Modulacao'),
    path('buscarModulacao/', views.buscaModulacao, name='Buscar Aspector Vocal - Modulacao'),
    path('editarModulacao/<int:id>', views.editarModulacao, name='Editar Aspector Vocal - Modulacao'),
    path('excluirModulacao/<int:id>', views.excluirModulacao, name='Excluir Aspector Vocal - Modulacao'),
    
    path('qualidadeemiss/<int:id>', views.qualidadeemiss, name='qualidadeemiss'),
    path('novoQualidadeemiss/', views.novoQualidadeemiss, name='Novo Aspecto Vocal - Qualidade na Emissão'),
    path('buscarQualidadeemiss/', views.buscaQualidadeemiss, name='Buscar Aspector Vocal - Qualidade na Emissão'),
    path('editarQualidadeemiss/<int:id>', views.editarQualidadeemiss, name='Editar Aspector Vocal - Qualidade na Emissão'),
    path('excluirQualidadeemiss/<int:id>', views.excluirQualidadeemiss, name='Excluir Aspector Vocal - Qualidade na Emissão'),
    
    
    path('novo/', views.novoPaciente, name='Novo Paciente'),
    path('novoProfissional/', views.novoProfissional, name='Novo Profissional'),
    path('editar/<int:id>', views.editarPaciente, name='Editar Paciente'),
    path('editarProfissional/<int:id>', views.editarProfissional, name='Editar Profissional'),
    path('excluir/<int:id>', views.excluirPaciente, name='Editar Paciente'),
    path('excluirProfissional/<int:id>', views.excluirProfissional, name='Editar Profissional'),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('avaliacaoad/', views.avaliacaoad, name='Avaliação do Paciente'),
    
]
