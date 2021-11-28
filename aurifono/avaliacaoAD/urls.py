from django.urls import path
from . import views
from aurifono.urls import *


urlpatterns = [
path("avaliacaoAD/", views.avaliacaoad, name='avaliacaoad')
    

    
]