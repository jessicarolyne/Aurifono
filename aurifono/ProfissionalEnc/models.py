from django.db import models
from datetime import datetime

from django.db.models.enums import Choices


class ProfissionalEnc(models.Model):
    STATUS_CHOICE = (
        ('A', 'Ativo'),
        ('N', 'Não Ativo'),
        
    )
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)
    
    
    class Meta:
        verbose_name_plural = "Cadastro de Profissionais"
    
    def __str__(self):
        return self.nome