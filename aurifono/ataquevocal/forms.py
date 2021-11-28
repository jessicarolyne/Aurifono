from django import forms
from django.forms import fields
from ataquevocal.models import AtaqueVocal

class AtaqueVocalForm(forms.ModelForm):
    class Meta:
        model = AtaqueVocal
        fields = '__all__'
