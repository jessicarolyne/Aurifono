from django.core import paginator
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Paciente
from django.core.paginator import Paginator
from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import pacienteForm

@login_required
def index(request):
    return render(request, 'clinicaAurifono/index.html')

@login_required
def paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    return render(request, 'clinicaAurifono/paciente.html', {'paciente' : paciente})

@login_required
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

@login_required
def editarPaciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
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

@login_required
def excluirPaciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    paciente.delete()
    messages.info(request,'Paciente excluído com sucesso!')
    return redirect('../buscar')

@login_required
def buscaPaciente(request):
    busca = request.GET.get('busca')
    if busca:
        pacientes = Paciente.objects.filter(nome__icontains=busca)
    else:
        pacientes_lista = Paciente.objects.all().order_by('-DataCadastro')
        paginator = Paginator(pacientes_lista, 8)
        page = request.GET.get('page')
        pacientes = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscar.html', {'pacientes' : pacientes})


# def index(request):
#     #return HttpResponse('<h1>Clinica de Fonoaudiologia</h1')
#     return render(request, 'index.html')

# def paciente(request):
    
#     if request.method == 'GET':
#         pacientes = Paciente.objects.all()
        
#         form = PacienteForm()
#         context = {
#             'pacientes': pacientes,
#             'form': form,
#         }
#         return render(request, 'paciente.html', context)
#     elif request.method == 'POST':
#          form = PacienteForm(request.POST)
#          if  form.is_valid():
#              cad_paciente = form.save()
#              form = PacienteForm()
         
                
#         #form = PacienteForm()
#          context = {
#             'form': form,
#              }
#          return render(request, 'paciente.html', context=context)
     
# def verpaciente(request, pk):
#     data = {}
#     data['paci'] = Paciente.objects.get(pk=pk)
#     return render(request, 'verpaciente.html', data)     

# def editpaciente(request, pk):
#     data = {}
#     data['paci'] = Paciente.objects.get(pk=pk)
#     data['form'] = PacienteForm(instance=data['paci'])
#     return render(request, 'paciente.html', data)

# def updatepaciente(request, pk):
#     data = {}
#     data['paci'] = Paciente.objects.get(pk=pk)
#     form = PacienteForm(request.POST, instance=data['paci'])
#     if form.is_valid():
#         form.save()
#         return redirect('paciente')    
    
# def deletepaciente(request, pk):
#     paci = Paciente.objects.get(pk = pk)
#     paci.delete() 
#     return redirect('paciente') 

# def paginacao(request):
#     data = {}
#     all = Paciente.objects.all()
#     paginator = Paginator(all, 5)
#     pages = request.GET.get('page')
#     data['db'] = paginator.get_page(pages)
#     return render(request, 'paciente.html', data)

# def busca(request):
#     data = {}
#     search = request.GET.get('search')
#     if search:
#         data['db'] = Paciente.objects.filter(nome__icontains=search)
#     else:
#         data['db'] = Paciente.objects.all()
     
#     return render(request, 'paciente.html', data)