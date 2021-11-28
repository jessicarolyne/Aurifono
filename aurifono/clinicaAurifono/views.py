from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# from .forms import pacienteForm, profissionalForm
# from .models import paciente_paciente, profissionalenc_profissionalenc

# @login_required
# def index(request):
#     return render(request, 'clinicaAurifono/index.html')

# @login_required
# def paciente(request, id):
#     paciente = get_object_or_404(paciente_paciente, pk=id)
#     return render(request, 'clinicaAurifono/paciente.html', {'paciente' : paciente})

# @login_required
# def novoPaciente(request):
#     if request.method == 'POST':
#         form = pacienteForm(request.POST)
#         if form.is_valid():
#             paciente_paciente = form.save(commit=False)
#             paciente_paciente.save()
#             return redirect('../buscar')
#     else:
#         form = pacienteForm()
#         return render(request, 'clinicaAurifono/novo.html', {'form' : form})

# @login_required
# def editarPaciente(request, id):
#     paciente = get_object_or_404(paciente_paciente, pk=id)
#     form = pacienteForm(instance=paciente)
#     if request.method == 'POST':
#         form = pacienteForm(request.POST, instance=paciente)
#         if form.is_valid():
#             paciente.save()
#             return redirect('../buscar')
#         else:
#             return render(request, 'clinicaAurifono/editar.html', {'form' : form, 'paciente' : paciente})
#     else:
#         return render(request, 'clinicaAurifono/editar.html', {'form' : form, 'paciente' : paciente})

# @login_required
# def excluirPaciente(request, id):
#     paciente = get_object_or_404(paciente_paciente, pk=id)
#     paciente.delete()
#     messages.info(request,'Paciente excluído com sucesso!')
#     return redirect('../buscar')

# @login_required
# def buscaPaciente(request):
#     busca = request.GET.get('busca')
#     if busca:
#         pacientes = paciente_paciente.objects.filter(nome__icontains=busca)
#     else:
#         pacientes_lista = paciente_paciente.objects.all().order_by('-DataCadastro')
#         paginator = Paginator(pacientes_lista, 8)
#         page = request.GET.get('page')
#         pacientes = paginator.get_page(page)
#     return render(request, 'clinicaAurifono/buscar.html', {'pacientes' : pacientes})


# @login_required
# def profissional(request, id):
#     profissional = get_object_or_404(profissionalenc_profissionalenc, pk=id)
#     return render(request, 'clinicaAurifono/profissional.html', {'profissional' : profissional})

# @login_required
# def novoProfissional(request):
#     if request.method == 'POST':
#         form = profissionalForm(request.POST)
#         if form.is_valid():
#             profissional_profissional = form.save(commit=False)
#             profissional_profissional.save()
#             return redirect('../buscarProfissional')
#     else:
#         form = profissionalForm()
#         return render(request, 'clinicaAurifono/novoProfissional.html', {'form' : form})

# @login_required
# def editarProfissional(request, id):
#     profissional = get_object_or_404(profissionalenc_profissionalenc, pk=id)
#     form = profissionalForm(instance=profissional)
#     if request.method == 'POST':
#         form = profissionalForm(request.POST, instance=profissional)
#         if form.is_valid():
#             profissional.save()
#             return redirect('../buscar')
#         else:
#             return render(request, 'clinicaAurifono/editar.html', {'form' : form, 'profissional' : profissional})
#     else:
#         return render(request, 'clinicaAurifono/editarProfissional.html', {'form' : form, 'profissional' : profissional})

# @login_required
# def excluirProfissional(request, id):
#     profissional = get_object_or_404(profissionalenc_profissionalenc, pk=id)
#     profissional.delete()
#     messages.info(request,'Profissional excluído com sucesso!')
#     return redirect('../buscarProfissional')

# @login_required
# def buscaProfissional(request):
#     busca = request.GET.get('busca')
#     if busca:
#         profissionais = profissionalenc_profissionalenc.objects.filter(nome__icontains=busca)
#     else:
#         profissionais_lista = profissionalenc_profissionalenc.objects.all()
#         paginator = Paginator(profissionais_lista, 8)
#         page = request.GET.get('page')
#         profissionais = paginator.get_page(page)
#     return render(request, 'clinicaAurifono/buscarProfissional.html', {'profissionais' : profissionais})