from django import forms
from django.forms import fields
from pitch.models import Pitch

class PitchForm(forms.ModelForm):
    class Meta:
        model = Pitch
        fields = '__all__'

