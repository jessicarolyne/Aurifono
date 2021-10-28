from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import paciente_paciente
from .forms import pacienteForm
 
def buscaPaciente(request):
    pacientes = paciente_paciente.objects.all() 
    return render(request, 'clinicaAurifono/buscaPaciente.html', {'pacientes' : pacientes})
    
def index(request):
    return render(request, 'clinicaAurifono/index.html')

def paciente(request, id):
    paciente = get_object_or_404(paciente_paciente, pk=id)
    return render(request, 'clinicaAurifono/paciente.html', {'paciente' : paciente})

def novoPaciente(request):
    form = pacienteForm()
    return render(request, 'clinicaAurifono/novoPaciente.html', {'form' : form})


