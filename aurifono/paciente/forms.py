from django import forms
from .models import Paciente


class pacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('RG','CPF','nome', 'DataNascimento', 'sexo', 'Profissional_id')
