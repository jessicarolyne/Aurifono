from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import paciente_paciente
 
def buscaPaciente(request):
    pacientes = paciente_paciente.objects.all() 
    return render(request, 'clinicaAurifono/buscaPaciente.html', {'pacientes' : pacientes})
    
def index(request):
    return render(request, 'clinicaAurifono/index.html')


