from django import forms
from django.forms import fields
from qualidadeemis.models import Qualidadeemis

class QualidadeemisForm(forms.ModelForm):
    class Meta:
        model = Qualidadeemis
        fields = '__all__'
