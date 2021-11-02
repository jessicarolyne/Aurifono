from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import pacienteForm
from .models import paciente_paciente
 
def buscaPaciente(request):
    busca = request.GET.get('busca')
    if busca:
        pacientes = paciente_paciente.objects.filter(nome__icontains=busca)
    else:
        pacientes_lista = paciente_paciente.objects.all().order_by('-DataCadastro')
        paginator = Paginator(pacientes_lista, 8)
        page = request.GET.get('page')
        pacientes = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscar.html', {'pacientes' : pacientes})
    
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
            return redirect('../buscar')
    else:
        form = pacienteForm()
        return render(request, 'clinicaAurifono/novo.html', {'form' : form})

def editarPaciente(request, id):
    paciente = get_object_or_404(paciente_paciente, pk=id)
    form = pacienteForm(instance=paciente)
    if request.method == 'POST':
        form = pacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente.save()
            return redirect('../buscar')
        else:
            return render(request, 'clinicaAurifono/editar.html', {'form' : form, 'paciente' : paciente})
    else:
        return render(request, 'clinicaAurifono/editar.html', {'form' : form, 'paciente' : paciente})

def excluirPaciente(request, id):
    paciente = get_object_or_404(paciente_paciente, pk=id)
    paciente.delete()
    messages.info(request,'Paciente excluído com sucesso!')
    return redirect('../buscar')
