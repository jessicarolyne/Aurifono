from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('clinicaAurifono.urls')),
    path('', include('avaliacaoAD.urls')),
    path('', include('ataquevocal.urls')),
    path('', include('ComunicOral.urls')),
    path('', include('loudness.urls')),
    path('', include('modulacao.urls')),
    path('', include('paciente.urls')),
    path('', include('pitch.urls')),
    path('', include('ProfissionalEnc.urls')),
    path('', include('qualidadeemis.urls')),
    path('', include('ressonancia.urls')),
    path('', include('tipodevoz.urls')),
]
