from django import forms
from .models import LoudnessCad, ModulacaoCad, PitchCad, AtaqueVocal, AtaqueVocalCad, Loudness, Modulacao, Pitch, Qualidadeemis, QualidadeemisCad, Ressonancia, RessonanciaCad, TipoVoz, TipoVozCad, avaliacaoad_avaliacaoad, comunicoral_comunicoral, comunicoralidade_comunicoralidade, paciente_paciente
from .models import profissionalenc_profissionalenc
from django import forms

class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente_paciente
        fields = ('RG','CPF','nome', 'DataNascimento', 'sexo', 'Profissional_id')

class profissionalForm(forms.ModelForm):
    class Meta:
        model = profissionalenc_profissionalenc
        fields = ('nome','status')
        
class ComunicOralForm(forms.ModelForm):
    class Meta:
        model = comunicoral_comunicoral
        fields = '__all__'        
        
class TipoVozForm(forms.ModelForm):
    class Meta:
        model = TipoVoz
        fields = '__all__'
        
class RessonanciaForm(forms.ModelForm):
    class Meta:
        model = Ressonancia
        fields = '__all__'                
        
class AtaqueVocalForm(forms.ModelForm):
    class Meta:
        model = AtaqueVocal
        fields = '__all__'        
        
class PitchForm(forms.ModelForm):
    class Meta:
        model = Pitch
        fields = '__all__'

class LoudnessForm(forms.ModelForm):
    class Meta:
        model = Loudness
        fields = '__all__'
        
class ModulacaoForm(forms.ModelForm):
    class Meta:
        model = Modulacao
        fields = '__all__'                
        
class QualidadeemissForm(forms.ModelForm):
    class Meta:
        model = Qualidadeemis
        fields = '__all__'        
        
class AvaliacaoADForm(forms.ModelForm):
    class Meta:
        model = avaliacaoad_avaliacaoad
        fields = '__all__'        
        
class ComunicOralidadeForm(forms.ModelForm):
    class Meta:
        model = comunicoralidade_comunicoralidade
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
        
class LoudnessCadForm(forms.ModelForm):
    class Meta:
        model = LoudnessCad
        fields = '__all__'        

class ModulacaoCadForm(forms.ModelForm):
    class Meta:
        model = ModulacaoCad
        fields = '__all__'        
        
class QualidadeemisCadForm(forms.ModelForm):
    class Meta:
        model = QualidadeemisCad
        fields = '__all__'
            


                   
        