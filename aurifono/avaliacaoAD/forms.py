from django import forms
from django.forms import fields
from avaliacaoAD.models import AtaqueVocalCad, AvaliacaoAD, ComunicOralidade, ModulacaoCad, PitchCad, QualidadeemisCad, RessonanciaCad, TipoVozCad

class AvaliacaoADForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoAD
        fields = '__all__'

class ComunicOralidadeForm(forms.ModelForm):
    class Meta:
        model = ComunicOralidade
        fields = '__all__'
        
class TipodeVozCadForm(forms.ModelForm):
    class Meta:
        model = TipoVozCad
        fields = '__all__'        
        
class RessonanciaCadForm(forms.ModelForm):
    class Meta:
        model = RessonanciaCad
        fields = '__all__'

class AtaqueVocalCadForm(forms.ModelForm):
    class Meta:
        model = AtaqueVocalCad
        fields = '__all__'        

class PitchCadForm(forms.ModelForm):
    class Meta:
        model = PitchCad
        fields = '__all__'        
        
class ModulacaoCadForm(forms.ModelForm):
    class Meta:
        model = ModulacaoCad
        fields = '__all__'        
        
class QualidadeemisCadForm(forms.ModelForm):
    class Meta:
        model = QualidadeemisCad
        fields = '__all__'
            