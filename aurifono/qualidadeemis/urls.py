from django.urls import path
from . import views
from aurifono.urls import *


urlpatterns = [
    #path('', views.index, name='index'),
    #path("paciente/", views.paciente, name='paciente'),
    path("qualidadeemis/", views.qualidadeemis, name='qualidadeemis'),
    #path("update/<int:profissionalenc_id>/", views.update, name='update_profissionalenc'),    
]