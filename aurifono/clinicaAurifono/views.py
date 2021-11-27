from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import ComunicOralForm, TipoVozForm, pacienteForm, profissionalForm
from .models import comunicoral_comunicoral, paciente_paciente, profissionalenc_profissionalenc, TipoVoz

@login_required
def index(request):
    return render(request, 'clinicaAurifono/index.html')

@login_required
def paciente(request, id):
    paciente = get_object_or_404(paciente_paciente, pk=id)
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

@login_required
def excluirPaciente(request, id):
    paciente = get_object_or_404(paciente_paciente, pk=id)
    paciente.delete()
    messages.info(request,'Paciente excluído com sucesso!')
    return redirect('../buscar')

@login_required
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


@login_required
def profissional(request, id):
    profissional = get_object_or_404(profissionalenc_profissionalenc, pk=id)
    return render(request, 'clinicaAurifono/profissional.html', {'profissional' : profissional})

@login_required
def novoProfissional(request):
    if request.method == 'POST':
        form = profissionalForm(request.POST)
        if form.is_valid():
            profissional_profissional = form.save(commit=False)
            profissional_profissional.save()
            return redirect('../buscarProfissional')
    else:
        form = profissionalForm()
        return render(request, 'clinicaAurifono/novoProfissional.html', {'form' : form})

@login_required
def editarProfissional(request, id):
    profissional = get_object_or_404(profissionalenc_profissionalenc, pk=id)
    form = profissionalForm(instance=profissional)
    if request.method == 'POST':
        form = profissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            profissional.save()
            return redirect('../buscar')
        else:
            return render(request, 'clinicaAurifono/editar.html', {'form' : form, 'profissional' : profissional})
    else:
        return render(request, 'clinicaAurifono/editarProfissional.html', {'form' : form, 'profissional' : profissional})

@login_required
def excluirProfissional(request, id):
    profissional = get_object_or_404(profissionalenc_profissionalenc, pk=id)
    profissional.delete()
    messages.info(request,'Profissional excluído com sucesso!')
    return redirect('../buscarProfissional')

@login_required
def buscaProfissional(request):
    busca = request.GET.get('busca')
    if busca:
        profissionais = profissionalenc_profissionalenc.objects.filter(nome__icontains=busca)
    else:
        profissionais_lista = profissionalenc_profissionalenc.objects.all()
        paginator = Paginator(profissionais_lista, 8)
        page = request.GET.get('page')
        profissionais = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscarProfissional.html', {'profissionais' : profissionais})


@login_required
def comunicoral(request, id):
    comunicoral = get_object_or_404(comunicoral_comunicoral, pk=id)
    return render(request, 'clinicaAurifono/comunicoral.html', {'comunicoral': comunicoral})

@login_required
def novoComunicoral(request):
    if request.method == 'POST':
        form = ComunicOralForm(request.POST)
        if form.is_valid():
            comunicoral_comunicoral = form.save(commit=False)
            comunicoral_comunicoral.save()
            return redirect('../buscarComunicoral')
    else:
        form = ComunicOralForm()
        return render(request, 'clinicaAurifono/novoComunicoral.html', {'form' : form})
    
@login_required
def editarComunicoral(request, id):
    comunicoral = get_object_or_404(comunicoral_comunicoral, pk=id)
    form = ComunicOralForm(instance=comunicoral)
    if request.method == 'POST':
        form = ComunicOralForm(request.POST, instance=comunicoral)
        if form.is_valid():
            comunicoral.save()
            return redirect('../buscar')
        else:
            return render(request, 'clinicaAurifono/editar.html', {'form' : form, 'comunicoral' : comunicoral})
    else:
        return render(request, 'clinicaAurifono/editarComunicoral.html', {'form' : form, 'comunicoral' : comunicoral})
    
@login_required
def excluirComunicoral(request, id):
    comunicoral = get_object_or_404(comunicoral_comunicoral, pk=id)
    comunicoral.delete()
    messages.info(request,'Comunicação Oral excluído com sucesso!')
    return redirect('../buscarComunicoral')


@login_required
def buscaComunicoral(request):
    busca = request.GET.get('busca')
    if busca:
        comunicorals = comunicoral_comunicoral.objects.filter(dsc_habilidade__icontains=busca)
        print(comunicorals)
    else:
        comunicorals_lista = comunicoral_comunicoral.objects.all()
        paginator = Paginator(comunicorals_lista, 8)
        page = request.GET.get('page')
        comunicorals = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscarComunicoral.html', {'comunicorals' : comunicorals})



@login_required
def tipodevoz(request, id):
    tipodevoz = get_object_or_404(TipoVoz, pk=id)
    return render(request, 'clinicaAurifono/tipodevoz.html', {'tipodevoz': tipodevoz})


@login_required
def novoTipodevoz(request):
    if request.method == 'POST':
        form = TipoVozForm(request.POST)
        if form.is_valid():
            TipoVoz = form.save(commit=False)
            TipoVoz.save()
            return redirect('../buscarTipodevoz')
    else:
        form = TipoVozForm()
        return render(request, 'clinicaAurifono/novoTipodevoz.html', {'form' : form})
    
@login_required
def editarTipodevoz(request, id):
    tipodevoz = get_object_or_404(TipoVoz, pk=id)
    form = TipoVozForm(instance=tipodevoz)
    if request.method == 'POST':
        form = TipoVozForm(request.POST, instance=tipodevoz)
        if form.is_valid():
            tipodevoz.save()
            return redirect('../buscarTipodevoz')
        else:
            return render(request, 'clinicaAurifono/editarTipodevoz.html', {'form' : form, 'tipodevoz' : tipodevoz})
    else:
        return render(request, 'clinicaAurifono/editarTipodevoz.html', {'form' : form, 'tipodevoz' : tipodevoz})
    
@login_required
def excluirTipodevoz(request, id):
    tipodevoz = get_object_or_404(TipoVoz, pk=id)
    tipodevoz.delete()
    messages.info(request,'Tipo de Voz excluído com sucesso!')
    return redirect('../buscarTipodevoz')


@login_required
def buscaTipodevoz(request):
    busca = request.GET.get('busca')
    if busca:
        tipodevozs = TipoVoz.objects.filter(descricao__icontains=busca)
        
    else:
        tipodevozs_lista = TipoVoz.objects.all()
        paginator = Paginator(tipodevozs_lista, 8)
        page = request.GET.get('page')
        tipodevozs = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscarTipodevoz.html', {'tipodevozs' : tipodevozs })
