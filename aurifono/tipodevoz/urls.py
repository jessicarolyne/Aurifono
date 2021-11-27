from django.urls import path
from . import views
from clinicaAurifono.urls import *
  
urlpatterns = [
    #path('', views.index, name='index'),
    #path("paciente/", views.paciente, name='paciente'),
    path("tipodevoz/", views.tipodevoz, name='tipodevoz'),
    path('vertipodevoz/<int:pk>/', views.vertipodevoz, name='vertipodevoz'),
    path('edittipodevoz/<int:pk>/', views.edittipodevoz, name='edittipodevoz'),
    path('updatetipodevoz/<int:pk>/', views.updatetipodevoz, name='updatetipodevoz'),
    path('deletetipodevoz/<int:pk>/', views.deletetipodevoz, name='deletetipodevoz'),
    #path("update/<int:profissionalenc_id>/", views.update, name='update_profissionalenc'),    
]