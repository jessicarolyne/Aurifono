from django.urls import path
from . import views
from clinicaAurifono.urls import *
 
urlpatterns = [
    #path('', views.index, name='index'),
    #path("paciente/", views.paciente, name='paciente'),
    path("comunicoral/", views.comunicoral, name='comunicoral'),
    path('vercomunicoral/<int:pk>/', views.vercomunicoral, name='vercomunicoral'),
    path('editcomunicoral/<int:pk>/', views.editcomunicoral, name='editcomunicoral'),
    path('updatecomunicoral/<int:pk>/', views.updatecomunicoral, name='updatecomunicoral'),
    path('deletecomunicoral/<int:pk>/', views.deletecomunicoral, name='deletecomunicoral'),
    #path("update/<int:profissionalenc_id>/", views.update, name='update_profissionalenc'),
    

    
]