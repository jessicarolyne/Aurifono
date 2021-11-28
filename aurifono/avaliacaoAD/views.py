from django.db.models.enums import TextChoices
from django.db.models.fields import TextField
from django.db.models.query import QuerySet
from django.forms.models import inlineformset_factory, modelform_factory
from django.forms.widgets import CheckboxSelectMultiple, RadioSelect, SelectMultiple, TextInput, Textarea
from django.shortcuts import render, get_object_or_404

from ComunicOral.forms import ComunicOralForm
from ressonancia.models import Ressonancia
from tipodevoz.forms import TipoVozForm
from .models import AtaqueVocalCad, AvaliacaoAD, ComunicOralidade, ComunicOral, LoudnessCad, PitchCad, RessonanciaCad, TipoVozCad, AtaqueVocalCad, PitchCad, ModulacaoCad, QualidadeemisCad
from avaliacaoAD.forms import AtaqueVocalCadForm, AvaliacaoAD, AvaliacaoADForm, ComunicOralidadeForm, PitchCadForm, RessonanciaCadForm, TipodeVozCadForm, AtaqueVocalCadForm, PitchCadForm, ModulacaoCadForm, QualidadeemisCadForm

def avaliacaoad(request):
    if request.method == 'GET':
        avaliacaoads = AvaliacaoAD.objects.all()
        #comunicoralidades = ComunicOralidade.objects.all()
        form = AvaliacaoADForm()
        formoralidade_factory = inlineformset_factory(AvaliacaoAD, ComunicOralidade, form=ComunicOralidadeForm, extra=9, can_delete=False, widgets={"ComunicOral": TextInput(), "resp_oralidade": RadioSelect()}, fields=('ComunicOral','resp_oralidade',), labels={'ComunicOral' : 'Pergunta','resp_oralidade': 'Resposta'})
        #formoralidade_factory = inlineformset_factory(AvaliacaoAD, ComunicOralidade, form=ComunicOralidadeForm, extra=9, can_delete=False)
        #formoralidade_factory = modelform_factory(AvaliacaoAD, ComunicOralidade, form=ComunicOralidadeForm)
       
        formtipodevozcad_factory = inlineformset_factory(AvaliacaoAD, TipoVozCad, form=TipodeVozCadForm, extra=11, can_delete=False)
        formressoanacia_factory = inlineformset_factory(AvaliacaoAD, RessonanciaCad, form=RessonanciaCadForm, extra=4, can_delete=False)
        formataquevocal_factory = inlineformset_factory(AvaliacaoAD, AtaqueVocalCad, form=AtaqueVocalCadForm, extra=3, can_delete=False)
        formpitch_factory = inlineformset_factory(AvaliacaoAD, PitchCad, form=PitchCadForm, extra=3, can_delete=False)
        formloudness_factory = inlineformset_factory(AvaliacaoAD, LoudnessCad, form=PitchCadForm, extra=3, can_delete=False)
        formmodulacao_factory = inlineformset_factory(AvaliacaoAD, ModulacaoCad, form=PitchCadForm, extra=3, can_delete=False)
        formqualidadeemis_factory = inlineformset_factory(AvaliacaoAD, QualidadeemisCad, form=QualidadeemisCadForm, extra=4, can_delete=False)
        
        formoralidade = formoralidade_factory()      
        formtipodevozcad = formtipodevozcad_factory()
        formressonanciacad = formressoanacia_factory()
        formataquevocalcad = formataquevocal_factory()
        formpitchcad = formpitch_factory()
        formloudnesscad = formloudness_factory()
        formmodulacaocad = formmodulacao_factory()
        formqualidadeemis  = formqualidadeemis_factory()
        
        context = {
            'avaliacaoads': avaliacaoads,
            'form': form,
            'formoralidade': formoralidade,
            'formtipodevozcad' : formtipodevozcad,
            'formressonanciacad' : formressonanciacad,
            'formataquevocalcad' : formataquevocalcad,
            'formpitchcad' : formpitchcad,
            'formloudnesscad' : formloudnesscad, 
            'formmodulacaocad' : formmodulacaocad,
            'formqualidadeemis' : formqualidadeemis,
        }
        return render(request, 'clinicaAurifono/avaliacaoad.html', context=context)
    elif request.method == 'POST':
        form = AvaliacaoADForm(request.POST)
        #formoralidade_factory = inlineformset_factory(AvaliacaoAD, ComunicOralidade, form=ComunicOralidadeForm, can_delete=False, widgets={"ComunicOral": Textarea(), "resp_oralidade": RadioSelect()})
        #formoralidade_factory = modelform_factory(AvaliacaoAD, ComunicOralidade, form=ComunicOralidadeForm)
        formoralidade_factory = inlineformset_factory(AvaliacaoAD, ComunicOralidade, form=ComunicOralidadeForm, can_delete=False)
        formtipodevozcad_factory = inlineformset_factory(AvaliacaoAD, TipoVozCad, form=TipodeVozCadForm, can_delete=False)
        formressoanacia_factory = inlineformset_factory(AvaliacaoAD, RessonanciaCad, form=RessonanciaCad, can_delete=False)
        formataquevocal_factory = inlineformset_factory(AvaliacaoAD, RessonanciaCad, form=AtaqueVocalCad, can_delete=False)
        formpitch_factory = inlineformset_factory(AvaliacaoAD, PitchCad, form=PitchCadForm, extra=3, can_delete=False)
        formloudness_factory = inlineformset_factory(AvaliacaoAD, LoudnessCad, form=PitchCadForm, extra=3, can_delete=False)
        formmodulacao_factory = inlineformset_factory(AvaliacaoAD, ModulacaoCad, form=PitchCadForm, extra=3)
        formqualidadeemis_factory = inlineformset_factory(AvaliacaoAD, QualidadeemisCad, form=QualidadeemisCadForm, extra=4, can_delete=False)
        
        formoralidade = formoralidade_factory(request.POST)
        formtipodevozcad = formtipodevozcad_factory(request.POST)
        formressonanciacad = formressoanacia_factory(request.POST)
        formataquevocalcad = formataquevocal_factory(request.POST)
        formpitchcad = formpitch_factory(request.POST)
        formloudnesscad = formloudness_factory(request.POST)
        formmodulacaocad = formmodulacao_factory(request.POST)
        formqualidadeemiscad = formqualidadeemis_factory(request.POST)
        
        if form.is_valid() and formoralidade.is_valid() and formtipodevozcad.is_valid() and formressonanciacad.is_valid() and formataquevocalcad.is_valid() and formpitchcad.is_valid and formloudnesscad.is_valid and formmodulacaocad.is_valid and formqualidadeemiscad.is_valid:
            avaliacao = form.save()
            formoralidade.instance = avaliacao
            formtipodevozcad.instance = avaliacao
            formressonanciacad.instance = avaliacao
            formataquevocalcad.instance = avaliacao
            formpitchcad.instance = avaliacao
            formloudnesscad.instance = avaliacao
            formoralidade.save()
            formtipodevozcad.save()
            formressonanciacad.save()
            formataquevocalcad.save()
            formpitchcad.save()
            formloudnesscad.save()
            formmodulacaocad.save()
            formqualidadeemiscad.save()
            
            form = AvaliacaoADForm()
            formoralidade = ComunicOralidadeForm()
            formtipodevozcad = TipodeVozCadForm()
            formressonanciacad = RessonanciaCadForm()
            formataquevocalcad = AtaqueVocalCadForm()
            formpitchcad = PitchCadForm()
            formloudnesscad = LoudnessCad()
            formmodulacaocad = ModulacaoCad()
            formqualidadeemis = QualidadeemisCad()
            
            
            
        context = {
            'form' : form,
            'formoralidade' : formoralidade,
            'formtipodevozcad': formtipodevozcad,
            'formressonanciacad': formressonanciacad,
            'formataquevocalcad' : formataquevocalcad,
            'formpitchcad': formpitchcad,
            'formloudnesscad' : formloudnesscad,
            'formmodulacaocad': formmodulacaocad,
            'formqualidadeemis': formqualidadeemis,
            
            
        }
        
        return render(request, 'clinicaAurifono/avaliacaoad.html', context=context)

"""def avaliacaoad(request):
    if request.method == 'GET':
        avaliacaoads = AvaliacaoAD.objects.all()
        form = AvaliacaoADForm()
        formoralidade_factory = modelform_factory(ComunicOralidade, ComunicOralidadeForm,fields=('ComunicOral', 'resp_oralidade'),localized_fields='__all__')
        formoralidade = formoralidade_factory()
        #for ft in formoralidade:
        #    print(ft)
        context = {
            'form': form,
            'formoralidade': formoralidade,
            
        }
        return render(request, 'avaliacaoad.html', context=context)
    elif request.method == 'POST':
        form = AvaliacaoADForm(request.POST)
        formoralidade_factory = modelform_factory(ComunicOralidade, ComunicOralidadeForm,fields=('ComunicOral', 'resp_oralidade'),localized_fields='__all__')
        formoralidade = formoralidade_factory(request.POST)
        if form.is_valid() and formoralidade.is_valid():
            avaliacao = form.save()
            formoralidade.instance = avaliacao
            formoralidade.save()
            form = AvaliacaoADForm()
            formoralidade = ComunicOralidadeForm()
        
        context = {
            'form' : form,
            'formoralidade' : formoralidade,
      
        }
        return render(request, 'avaliacaoad.html', context=context)    
"""        