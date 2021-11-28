from django.urls import path
from . import views
from aurifono.urls import *


urlpatterns = [
    #path('', views.index, name='index'),
    #path("paciente/", views.paciente, name='paciente'),
    path("ataquevocal/", views.ataquevocal, name='ataquevocal'),
    path('verataquevocal/<int:pk>/', views.verataquevocal, name='verataquevocal'),
    path('editataquevocal/<int:pk>/', views.editataquevocal, name='editataquevocal'),
    path('updateataquevocal/<int:pk>/', views.updateataquevocal, name='updateataquevocal'),
    path('deleteataquevocal/<int:pk>/', views.deleteataquevocal, name='deleteataquevocal'),
    #path("update/<int:profissionalenc_id>/", views.update, name='update_profissionalenc'),    
]