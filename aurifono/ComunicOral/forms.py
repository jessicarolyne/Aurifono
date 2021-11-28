from django import forms
from django.forms import fields
from ComunicOral.models import ComunicOral

class ComunicOralForm(forms.ModelForm):
    class Meta:
        model = ComunicOral
        fields = '__all__'
        
      