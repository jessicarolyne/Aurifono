from django.core import paginator
from django.forms.models import inlineformset_factory
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import AtaqueVocalCadForm, AtaqueVocalForm, AvaliacaoADForm, ComunicOralForm, ComunicOralidadeForm, LoudnessCadForm, LoudnessForm, ModulacaoCadForm, ModulacaoForm, PitchCadForm, PitchForm, QualidadeemissForm, RessonanciaCadForm, RessonanciaForm, TipoVozForm, TipodeVozCadForm, pacienteForm, profissionalForm
from .models import AtaqueVocal, AtaqueVocalCad, Loudness, LoudnessCad, Modulacao, ModulacaoCad, Pitch, PitchCad, Qualidadeemis, QualidadeemisCad, Ressonancia, RessonanciaCad, TipoVozCad, avaliacaoad_avaliacaoad, comunicoral_comunicoral, comunicoralidade_comunicoralidade, paciente_paciente, profissionalenc_profissionalenc, TipoVoz

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

@login_required
def ressonancia(request, id):
    ressonancia = get_object_or_404(TipoVoz, pk=id)
    return render(request, 'clinicaAurifono/ressonancia.html', {'ressonancia': ressonancia})


@login_required
def novoRessonancia(request):
    if request.method == 'POST':
        form = RessonanciaForm(request.POST)
        if form.is_valid():
            Ressonancia = form.save(commit=False)
            Ressonancia.save()
            return redirect('../buscarRessonancia')
    else:
        form = RessonanciaForm()
        return render(request, 'clinicaAurifono/novoRessonancia.html', {'form' : form})
    
@login_required
def editarRessonancia(request, id):
    ressonancia = get_object_or_404(Ressonancia, pk=id)
    form = RessonanciaForm(instance=ressonancia)
    if request.method == 'POST':
        form = RessonanciaForm(request.POST, instance=ressonancia)
        if form.is_valid():
            ressonancia.save()
            return redirect('../buscarRessonancia')
        else:
            return render(request, 'clinicaAurifono/editarRessoancia.html', {'form' : form, 'ressonancia' : ressonancia})
    else:
        return render(request, 'clinicaAurifono/editarRessonancia.html', {'form' : form, 'ressonancia' : ressonancia})
    
@login_required
def excluirRessonancia(request, id):
    ressonancia = get_object_or_404(Ressonancia, pk=id)
    ressonancia.delete()
    messages.info(request,'Ressonância excluído com sucesso!')
    return redirect('../buscarRessonancia')


@login_required
def buscaRessonancia(request):
    busca = request.GET.get('busca')
    if busca:
        ressonancias = Ressonancia.objects.filter(descricao__icontains=busca)
        
    else:
        ressonancias_lista = Ressonancia.objects.all()
        paginator = Paginator(ressonancias_lista, 8)
        page = request.GET.get('page')
        ressonancias = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscarRessonancia.html', {'ressonancias' : ressonancias })

@login_required
def ataquevocal(request, id):
    ataquevocal = get_object_or_404(TipoVoz, pk=id)
    return render(request, 'clinicaAurifono/ataquevocal.html', {'ataquevocal': ataquevocal})


@login_required
def novoAtaquevocal(request):
    if request.method == 'POST':
        form = AtaqueVocalForm(request.POST)
        if form.is_valid():
            AtaqueVocal = form.save(commit=False)
            AtaqueVocal.save()
            return redirect('../buscarAtaquevocal')
    else:
        form = AtaqueVocalForm()
        return render(request, 'clinicaAurifono/novoAtaquevocal.html', {'form' : form})
    
@login_required
def editarAtaquevocal(request, id):
    ataquevocal = get_object_or_404(AtaqueVocal, pk=id)
    form = AtaqueVocalForm(instance=ataquevocal)
    if request.method == 'POST':
        form = AtaqueVocalForm(request.POST, instance=ataquevocal)
        if form.is_valid():
            ataquevocal.save()
            return redirect('../buscarAtaquevocal')
        else:
            return render(request, 'clinicaAurifono/editarAtaquevocal.html', {'form' : form, 'ataquevocal' : ataquevocal})
    else:
        return render(request, 'clinicaAurifono/editarAtaquevocal.html', {'form' : form, 'ataquevocal' : ataquevocal})
    
@login_required
def excluirAtaquevocal(request, id):
    ataquevocal = get_object_or_404(AtaqueVocal, pk=id)
    ataquevocal.delete()
    messages.info(request,'Ataque Vocal excluído com sucesso!')
    return redirect('../buscarAtaquevocal')


@login_required
def buscaAtaquevocal(request):
    busca = request.GET.get('busca')
    if busca:
        ataquevocals = AtaqueVocal.objects.filter(descricao__icontains=busca)
        
    else:
        ataquevocals_lista = AtaqueVocal.objects.all()
        paginator = Paginator(ataquevocals_lista, 8)
        page = request.GET.get('page')
        ataquevocals = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscarAtaquevocal.html', {'ataquevocals' : ataquevocals })

@login_required
def pitch(request, id):
    pitch = get_object_or_404(Pitch, pk=id)
    return render(request, 'clinicaAurifono/pitch.html', {'pitch': pitch})


@login_required
def novoPitch(request):
    if request.method == 'POST':
        form = PitchForm(request.POST)
        if form.is_valid():
            Pitch = form.save(commit=False)
            Pitch.save()
            return redirect('../buscarPitch')
    else:
        form = PitchForm()
        return render(request, 'clinicaAurifono/novoPitch.html', {'form' : form})
    
@login_required
def editarPitch(request, id):
    pitch = get_object_or_404(Pitch, pk=id)
    form = PitchForm(instance=pitch)
    if request.method == 'POST':
        form = PitchForm(request.POST, instance=pitch)
        if form.is_valid():
            pitch.save()
            return redirect('../buscarPitch')
        else:
            return render(request, 'clinicaAurifono/editarPitch.html', {'form' : form, 'pitch' : pitch})
    else:
        return render(request, 'clinicaAurifono/editarPitch.html', {'form' : form, 'pitch' : pitch})
    
@login_required
def excluirPitch(request, id):
    pitch = get_object_or_404(Pitch, pk=id)
    pitch.delete()
    messages.info(request,'Pitch excluído com sucesso!')
    return redirect('../buscarPitch')


@login_required
def buscaPitch(request):
    busca = request.GET.get('busca')
    if busca:
        pitchs =  Pitch.objects.filter(descricao__icontains=busca)
        
    else:
        pitchs_lista = Pitch.objects.all()
        paginator = Paginator(pitchs_lista, 8)
        page = request.GET.get('page')
        pitchs = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscarPitch.html', {'pitchs' : pitchs })

@login_required
def loudness(request, id):
    loudness = get_object_or_404(Loudness, pk=id)
    return render(request, 'clinicaAurifono/loudness.html', {'loudness': loudness})


@login_required
def novoLoudness(request):
    if request.method == 'POST':
        form = LoudnessForm(request.POST)
        if form.is_valid():
            Loudness = form.save(commit=False)
            Loudness.save()
            return redirect('../buscarLoudness')
    else:
        form = LoudnessForm()
        return render(request, 'clinicaAurifono/novoLoudness.html', {'form' : form})
    
@login_required
def editarLoudness(request, id):
    loudness = get_object_or_404(Loudness, pk=id)
    form = LoudnessForm(instance=loudness)
    if request.method == 'POST':
        form = LoudnessForm(request.POST, instance=loudness)
        if form.is_valid():
            loudness.save()
            return redirect('../buscarLoudness')
        else:
            return render(request, 'clinicaAurifono/editarLoudness.html', {'form' : form, 'loudness' : loudness})
    else:
        return render(request, 'clinicaAurifono/editarLoudness.html', {'form' : form, 'loudness' : loudness})
    
@login_required
def excluirLoudness(request, id):
    loudness = get_object_or_404(Loudness, pk=id)
    loudness.delete()
    messages.info(request,'Loudness excluído com sucesso!')
    return redirect('../buscarLoudness')


@login_required
def buscaLoudness(request):
    busca = request.GET.get('busca')
    if busca:
        loudnesss = Loudness.objects.filter(descricao__icontains=busca)
        
    else:
        loudnesss_lista = Loudness.objects.all()
        paginator = Paginator(loudnesss_lista, 8)
        page = request.GET.get('page')
        loudnesss = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscarLoudness.html', {'loudnesss' : loudnesss })

@login_required
def modulacao(request, id):
    modulacao = get_object_or_404(Modulacao, pk=id)
    return render(request, 'clinicaAurifono/modulacao.html', {'modulacao': modulacao})


@login_required
def novoModulacao(request):
    if request.method == 'POST':
        form = ModulacaoForm(request.POST)
        if form.is_valid():
            modulacao = form.save(commit=False)
            modulacao.save()
            return redirect('../buscarModulacao')
    else:
        form = ModulacaoForm()
        return render(request, 'clinicaAurifono/novoModulacao.html', {'form' : form})
    
@login_required
def editarModulacao(request, id):
    modulacao = get_object_or_404(Modulacao, pk=id)
    form = ModulacaoForm(instance=modulacao)
    if request.method == 'POST':
        form = ModulacaoForm(request.POST, instance=modulacao)
        if form.is_valid():
            modulacao.save()
            return redirect('../buscarModulacao')
        else:
            return render(request, 'clinicaAurifono/editarModulacao.html', {'form' : form, 'modulacao' : modulacao})
    else:
        return render(request, 'clinicaAurifono/editarModulacao.html', {'form' : form, 'modulacao' : modulacao})
    
@login_required
def excluirModulacao(request, id):
    modulacao = get_object_or_404(Modulacao, pk=id)
    modulacao.delete()
    messages.info(request,'Modulação excluído com sucesso!')
    return redirect('../buscarModulacao')


@login_required
def buscaModulacao(request):
    busca = request.GET.get('busca')
    if busca:
        modulacaos = Modulacao.objects.filter(descricao__icontains=busca)
        
    else:
        modulacaos_lista = Modulacao.objects.all()
        paginator = Paginator(modulacaos_lista, 8)
        page = request.GET.get('page')
        modulacaos = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscarModulacao.html', {'modulacaos' : modulacaos })

@login_required
def excluirLoudness(request, id):
    loudness = get_object_or_404(Loudness, pk=id)
    loudness.delete()
    messages.info(request,'Loudness excluído com sucesso!')
    return redirect('../buscarLoudness')


@login_required
def buscaLoudness(request):
    busca = request.GET.get('busca')
    if busca:
        loudnesss = Loudness.objects.filter(descricao__icontains=busca)
        
    else:
        loudnesss_lista = Loudness.objects.all()
        paginator = Paginator(loudnesss_lista, 8)
        page = request.GET.get('page')
        loudnesss = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscarLoudness.html', {'loudnesss' : loudnesss })

@login_required
def qualidadeemiss(request, id):
    qualidadeemiss = get_object_or_404(Qualidadeemis, pk=id)
    return render(request, 'clinicaAurifono/qualidadeemiss.html', {'qualidadeemiss': qualidadeemiss})


@login_required
def novoQualidadeemiss(request):
    if request.method == 'POST':
        form = QualidadeemissForm(request.POST)
        if form.is_valid():
            qualidadeemiss = form.save(commit=False)
            qualidadeemiss.save()
            return redirect('../buscarQualidadeemiss')
    else:
        form = QualidadeemissForm()
        return render(request, 'clinicaAurifono/novoQualidadeemiss.html', {'form' : form})
    
@login_required
def editarQualidadeemiss(request, id):
    qualidadeemiss = get_object_or_404(Qualidadeemis, pk=id)
    form = QualidadeemissForm(instance=qualidadeemiss)
    if request.method == 'POST':
        form = QualidadeemissForm(request.POST, instance=qualidadeemiss)
        if form.is_valid():
            qualidadeemiss.save()
            return redirect('../buscarQualidadeemiss')
        else:
            return render(request, 'clinicaAurifono/editarModulacao.html', {'form' : form, 'qualidadeemiss' : qualidadeemiss})
    else:
        return render(request, 'clinicaAurifono/editarModulacao.html', {'form' : form, 'qualidadeemiss' : qualidadeemiss})
    
@login_required
def excluirQualidadeemiss(request, id):
    qualidadeemiss = get_object_or_404(Qualidadeemis, pk=id)
    qualidadeemiss.delete()
    messages.info(request,'Qualidade na Emissão excluído com sucesso!')
    return redirect('../buscarQualidadeemiss')


@login_required
def buscaQualidadeemiss(request):
    busca = request.GET.get('busca')
    if busca:
        qualidadeemisss = Qualidadeemis.objects.filter(descricao__icontains=busca)
        
    else:
        qualidadeemisss_lista = Qualidadeemis.objects.all()
        paginator = Paginator(qualidadeemisss_lista, 8)
        page = request.GET.get('page')
        qualidadeemisss = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscarQualidadeemiss.html', {'qualidadeemisss' : qualidadeemisss })

def avaliacaoad(request):
    if request.method == "GET":
        form = AvaliacaoADForm()
        formoralidade_factory = inlineformset_factory(avaliacaoad_avaliacaoad, comunicoralidade_comunicoralidade, form=ComunicOralidadeForm, extra=9, can_delete=False)
        formtipodevozcad_factory = inlineformset_factory(avaliacaoad_avaliacaoad, TipoVozCad, form=TipodeVozCadForm,extra=11, can_delete=False)
        formressoanacia_factory = inlineformset_factory(avaliacaoad_avaliacaoad, RessonanciaCad, form=RessonanciaCadForm,extra=4, can_delete=False)
        formataquevocal_factory = inlineformset_factory(avaliacaoad_avaliacaoad, AtaqueVocalCad, form=AtaqueVocalCadForm,extra=3, can_delete=False)
        formpitch_factory = inlineformset_factory(avaliacaoad_avaliacaoad, PitchCad, form=PitchCadForm,extra=4, can_delete=False)
        formloudness_factory = inlineformset_factory(avaliacaoad_avaliacaoad, LoudnessCad, form=LoudnessCadForm,extra=4, can_delete=False)
        formmodulacao_factory = inlineformset_factory(avaliacaoad_avaliacaoad, ModulacaoCad, form=ModulacaoCadForm,extra=3, can_delete=False)
        formqualidadeemis_factory = inlineformset_factory(avaliacaoad_avaliacaoad, QualidadeemisCad, form=QualidadeemissForm,extra=4, can_delete=False)
        formoralidade = formoralidade_factory()
        formtipodevozcad = formtipodevozcad_factory()
        formressoanacia = formressoanacia_factory()
        formataquevocal = formataquevocal_factory()
        formpitch = formpitch_factory()
        formloudness = formloudness_factory()
        formmodulacao = formmodulacao_factory()
        formqualidadeemis = formqualidadeemis_factory()
        context = {
            'form': form, 
            'formoralidade': formoralidade,
            'formtipodevozcad' : formtipodevozcad,
            'formressoanacia' : formressoanacia,
            'formataquevocal' : formataquevocal,
            'formpitch' : formpitch,
            'formloudness': formloudness,
            'formmodulacao' : formmodulacao,
            'formqualidadeemis' : formqualidadeemis,
        }
        return render(request, 'clinicaAurifono/avaliacaoad.html', context)
    elif request.method == "POST":
        form = AvaliacaoADForm(request.POST)
        formoralidade_factory = inlineformset_factory(avaliacaoad_avaliacaoad, comunicoralidade_comunicoralidade, form=ComunicOralidadeForm, can_delete=False)
        formtipodevozcad_factory = inlineformset_factory(avaliacaoad_avaliacaoad, TipoVozCad, form=TipoVozForm,extra=11, can_delete=False)
        formressoanacia_factory = inlineformset_factory(avaliacaoad_avaliacaoad, RessonanciaCad, form=RessonanciaCadForm,extra=11, can_delete=False)
        formataquevocal_factory = inlineformset_factory(avaliacaoad_avaliacaoad, AtaqueVocalCad, form=AtaqueVocalCadForm,extra=3, can_delete=False)
        formpitch_factory = inlineformset_factory(avaliacaoad_avaliacaoad, PitchCad, form=PitchCadForm,extra=3, can_delete=False)
        formloudness_factory = inlineformset_factory(avaliacaoad_avaliacaoad, LoudnessCad, form=LoudnessCadForm,extra=3, can_delete=False)
        formmodulacao_factory = inlineformset_factory(avaliacaoad_avaliacaoad, ModulacaoCad, form=ModulacaoCadForm,extra=3, can_delete=False)
        formqualidadeemis_factory = inlineformset_factory(avaliacaoad_avaliacaoad, QualidadeemisCad, form=QualidadeemissForm,extra=4, can_delete=False)
        formoralidade = formoralidade_factory(request.POST)
        formtipodevozcad = formtipodevozcad_factory(request.POST)
        formressoanacia = formressoanacia_factory(request.POST)
        formataquevocal = formataquevocal_factory(request.POST)
        formpitch = formpitch_factory(request.POST)
        formloudness = formloudness_factory(request.POST)
        formmodulacao = formmodulacao_factory(request.POST)
        formqualidadeemis = formqualidadeemis_factory(request.POST)
        if form.is_valid() and formoralidade.is_valid() and formtipodevozcad.is_valid() and formressoanacia.is_valid() and formataquevocal.is_valid() and formpitch.is_valid() and formloudness.is_valid() and formmodulacao.is_valid() and formqualidadeemis.is_valid():
            avaliacao = form.save()
            formoralidade.instance = avaliacao
            formtipodevozcad.instance = avaliacao
            formressoanacia.instance = avaliacao
            formataquevocal.instance = avaliacao
            formpitch.instance = avaliacao
            formloudness.instance = avaliacao
            formmodulacao.instance = avaliacao
            formqualidadeemis.instance = avaliacao
            formoralidade.save()
            formtipodevozcad.save()
            formressoanacia.save()
            formataquevocal.save()
            formpitch.save()
            formloudness.save()
            formmodulacao.save()
            formqualidadeemis.save()
            #return redirect('avaliacaoad')
            return render(request, 'clinicaAurifono/avaliacaoad.html', context=context)
        else:
            context = {'form': form,
                       'formoralidade' :formoralidade,
                       'formtipodevozcad' : formtipodevozcad,
                       'formressoanacia' : formressoanacia,
                       'formataquevocal' : formataquevocal,
                       'formpitch': formpitch,
                       'formloudness': formloudness,
                       'formmodulacao': formmodulacao,
                       'formqualidadeemis': formqualidadeemis
            }

            return render(request, 'clinicaAurifono/avaliacaoad.html', context)

             