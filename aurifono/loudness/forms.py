from django import forms
from django.forms import fields
from loudness.models import Loudness

class LoudnessForm(forms.ModelForm):
    class Meta:
        model = Loudness
        fields = '__all__'
