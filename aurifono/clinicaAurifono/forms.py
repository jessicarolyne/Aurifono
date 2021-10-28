from django import forms
from django.db import models
from django.db.models import fields
from .models import paciente_paciente

class pacienteForm(forms.ModelForm):
    class Dados:
        models = paciente_paciente
        fields('RG','CPF','nome','DataNascimento')