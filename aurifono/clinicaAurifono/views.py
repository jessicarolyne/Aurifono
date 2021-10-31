from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import pacienteForm
from .models import paciente_paciente
 
def buscaPaciente(request):
    pacientes = paciente_paciente.objects.all().order_by('-DataCadastro')
    return render(request, 'clinicaAurifono/buscaPaciente.html', {'pacientes' : pacientes})
    
def index(request):
    return render(request, 'clinicaAurifono/index.html')

def paciente(request, id):
    paciente = get_object_or_404(paciente_paciente, pk=id)
    return render(request, 'clinicaAurifono/paciente.html', {'paciente' : paciente})

def novoPaciente(request):
    if request.method == 'POST':
        form = pacienteForm(request.POST)
        if form.is_valid():
            paciente_paciente = form.save(commit=False)
            paciente_paciente.save()
            return redirect('/')
    else:
        form = pacienteForm()
        return render(request, 'clinicaAurifono/novoPaciente.html', {'form' : form})

def editarPaciente(request, id):
    paciente = get_object_or_404(paciente_paciente, pk=id)
    form = pacienteForm(instance=paciente)
    if request.method == 'POST':
        form = pacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente.save()
            return redirect('/')
        else:
            return render(request, 'clinicaAurifono/editar.html', {'form' : form, 'paciente' : paciente})
    else:
        return render(request, 'clinicaAurifono/editar.html', {'form' : form, 'paciente' : paciente})
