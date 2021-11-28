from django.db import models
from datetime import datetime

from ProfissionalEnc.models import ProfissionalEnc

class Paciente(models.Model):
    SEXO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )
    nome = models.CharField(max_length=100)
    RG = models.CharField(max_length=14)
    CPF = models.CharField(max_length=14)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    Profissional_id = models.ForeignKey(ProfissionalEnc, on_delete=models.CASCADE)
    DataCadastro = models.DateTimeField(default=datetime.now, blank=True)
    DataNascimento = models.DateTimeField(blank=True)
    
    class Meta:
        verbose_name_plural = "Cadastro de Pacientes"
    
    def __str__(self):
        return self.nome      