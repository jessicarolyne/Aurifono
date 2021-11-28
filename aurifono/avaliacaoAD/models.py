from datetime import datetime
from django.db import models
from paciente.models import Paciente
from ComunicOral.models import ComunicOral
from qualidadeemis.views import qualidadeemis
from ressonancia.models import Ressonancia
from tipodevoz.models import TipoVoz
from ataquevocal.models import AtaqueVocal
from pitch.models import Pitch
from loudness.models import Loudness
from modulacao.models import Modulacao
from qualidadeemis.models import Qualidadeemis

class AvaliacaoAD(models.Model):
    ORELHA_CHOICE = (
        ('OE', 'Orelha Esquerda'),
        ('OD', 'Orelha Direita'),
        ('AM', 'Ambas'),
    )
    DataAvaliacao = models.DateTimeField(default=datetime.now)
    QOrelha = models.CharField(max_length=2, choices=ORELHA_CHOICE)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
      
    class Meta:
        verbose_name_plural = "Avaliação Adulto"
    
    def __str__(self):
        return str(self.paciente)
    

class ComunicOralidade(models.Model):
    avaliacaoAD = models.ForeignKey(AvaliacaoAD, on_delete=models.DO_NOTHING)
    ComunicOral = models.ForeignKey(ComunicOral, on_delete=models.DO_NOTHING)
    resp_oralidade = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )
    
    class Meta:
        verbose_name_plural = "Respostas das Perguntas"    
        
    def __str__(self):
        return str(self.resp_oralidade)    
     
        
class TipoVozCad(models.Model):
    avaliacaoAD = models.ForeignKey(AvaliacaoAD, on_delete=models.DO_NOTHING)
    tipovoz = models.ForeignKey(TipoVoz, on_delete=models.DO_NOTHING)
    repostas = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )    
      
    class Meta:
        verbose_name_plural = "Repostas da Pergunta Tipo Voz"    
        
    def __str__(self):
        return str(self.repostas)             
        
class RessonanciaCad(models.Model):
    avaliacaoAD = models.ForeignKey(AvaliacaoAD, on_delete=models.DO_NOTHING)
    ressonancia = models.ForeignKey(Ressonancia, on_delete=models.DO_NOTHING)
    resposta = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )    
      
    class Meta:
        verbose_name_plural = "Repostas das Perguntas Ressonancia"    
        
    def __str__(self):
        return str(self.resposta)                      

class AtaqueVocalCad(models.Model):
        avaliacaoAD = models.ForeignKey(AvaliacaoAD, on_delete=models.DO_NOTHING)
        ataquevocal = models.ForeignKey(AtaqueVocal, on_delete=models.DO_NOTHING)
        resposta = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )    
        
class PitchCad(models.Model):
    avaliacaoAD = models.ForeignKey(AvaliacaoAD, on_delete=models.DO_NOTHING)
    pitch = models.ForeignKey(Pitch, on_delete=models.DO_NOTHING)
    resposta = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )   
    
class LoudnessCad(models.Model):
    avaliacaoAD = models.ForeignKey(AvaliacaoAD, on_delete=models.DO_NOTHING)
    loudness = models.ForeignKey(Loudness, on_delete=models.DO_NOTHING)
    resposta = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )   
    
class ModulacaoCad(models.Model):
    avaliacaoAD = models.ForeignKey(AvaliacaoAD, on_delete=models.DO_NOTHING)
    modulacao = models.ForeignKey(Modulacao, on_delete=models.DO_NOTHING)
    resposta = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )    
    
class QualidadeemisCad(models.Model):
    avaliacaoAD = models.ForeignKey(AvaliacaoAD, on_delete=models.DO_NOTHING)
    qualidadeemis = models.ForeignKey(Qualidadeemis, on_delete=models.DO_NOTHING)
    resposta = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )        