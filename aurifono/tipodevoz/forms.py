from django import forms
from django.forms import fields
from tipodevoz.models import TipoVoz
 
class TipoVozForm(forms.ModelForm):
    class Meta:
        model = TipoVoz
        fields = '__all__'