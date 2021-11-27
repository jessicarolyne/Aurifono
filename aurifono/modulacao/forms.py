from django import forms
from django.forms import fields
from modulacao.models import Modulacao

class ModulacaoForm(forms.ModelForm):
    class Meta:
        model = Modulacao
        fields = '__all__'
