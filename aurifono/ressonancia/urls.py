from django.urls import path
from . import views
from aurifono.urls import *

 
urlpatterns = [
    #path('', views.index, name='index'),
    #path("paciente/", views.paciente, name='paciente'),
    path("ressonancia/", views.ressonancia, name='ressonancia'),
    path('verressonancia/<int:pk>/', views.verressonancia, name='verressonancia'),
    path('editressonancia/<int:pk>/', views.editressonancia, name='editressonancia'),
    path('updateressonancia/<int:pk>/', views.updateressonancia, name='updateressonancia'),
    path('deleteressonancia/<int:pk>/', views.deleteressonancia, name='deleteressonancia'),
    #path("update/<int:profissionalenc_id>/", views.update, name='update_profissionalenc'),

]