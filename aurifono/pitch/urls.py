from django.urls import path
from . import views
from clinicaAurifono.urls import *

urlpatterns = [
    #path('', views.index, name='index'),
    #path("paciente/", views.paciente, name='paciente'),
    path("pitch/", views.pitch, name='pitch'),
    #path("update/<int:profissionalenc_id>/", views.update, name='update_profissionalenc'),    
]