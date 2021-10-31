from django import forms
from .models import paciente_paciente
from django import forms

class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente_paciente
        fields = ('RG','CPF','nome', 'DataNascimento', 'sexo', 'Profissional_id')