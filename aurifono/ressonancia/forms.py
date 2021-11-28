from django import forms
from django.forms import fields
from ressonancia.models import Ressonancia

class RessonanciaForm(forms.ModelForm):
    class Meta:
        model = Ressonancia
        fields = '__all__'
