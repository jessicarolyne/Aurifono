from django.urls import path
from . import views
from clinicaAurifono.urls import *

urlpatterns = [
    path("avaliacaoAD/", views.avaliacaoad, name='avaliacaoad') 
]