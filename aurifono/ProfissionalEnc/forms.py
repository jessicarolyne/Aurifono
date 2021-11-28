from django import forms
from .models import ProfissionalEnc

class profissionalEncForm(forms.ModelForm):
    class Meta:
        model = ProfissionalEnc
        fields = ('nome','status')