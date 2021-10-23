from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
 
def index(request):
    return render(request, 'clinicaAurifono/cadastro.html')

