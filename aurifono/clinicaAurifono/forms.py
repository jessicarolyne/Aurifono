from django import forms
from .models import TipoVoz, comunicoral_comunicoral, paciente_paciente
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