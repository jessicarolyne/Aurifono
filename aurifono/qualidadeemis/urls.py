from django.urls import path
from . import views
from clinicaAurifono.urls import *

urlpatterns = [
    path("qualidadeemis/", views.qualidadeemis, name='qualidadeemis'),
]