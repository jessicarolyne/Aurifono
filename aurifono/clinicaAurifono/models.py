from django.db import models
from django.db.models.base import Model
from django.db.models.fields import TextField
from datetime import datetime

class profissionalenc_profissionalenc(models.Model):
    STATUS = (
        ('1','Ativo'),
        ('0','Inativo')
    )
    nome = models.CharField(max_length=100, verbose_name='Nome')
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        verbose_name='Status',    
    )
    def __str__(self):
        return self.nome

class paciente_paciente(models.Model):
    SEXO = (
        ('feminino', 'Feminino'),
        ('masculino', 'Masculino'),
    )
    RG = models.CharField(max_length=12)
    CPF = models.CharField(max_length=14)
    nome = models.CharField(max_length=100, verbose_name='Nome')
    DataNascimento = models.DateField(verbose_name='Data de Nascimento')
    DataCadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data do cadastro')
    DataAtualizacao = models.DateTimeField(auto_now=True, verbose_name='Data da ultima atualização')
    sexo = models.CharField(
        max_length=9,
        choices=SEXO,
        verbose_name='Sexo'
    )
    Profissional_id = models.ForeignKey(profissionalenc_profissionalenc, on_delete=models.PROTECT, verbose_name='Profissional Responsável')
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.DataNascimento)

class avaliacaoad_avaliacaoad(models.Model):
    ORELHA = (
        ('ES', 'ESQUERDA'),
        ('DI', 'DIREITA'),
        ('AM', 'AMBAS'),
    )
    DataAvaliacao = models.DateField(default=datetime.now)
    QOrelha = models.CharField(max_length=2, choices=ORELHA)
    paciente_id = models.ForeignKey(paciente_paciente, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.paciente_id)

class comunicoral_comunicoral(models.Model):
    dsc_habilidade = models.CharField(max_length=150, verbose_name='Descrição da Habilidade')
    def __str__(self):
        return self.dsc_habilidade

class comunicoralidade_comunicoralidade(models.Model):
    avaliacaoAD_id = models.ForeignKey(avaliacaoad_avaliacaoad, on_delete=models.PROTECT, verbose_name='Avaliação')
    ComunicOral_id = models.ForeignKey(comunicoral_comunicoral, on_delete=models.PROTECT, verbose_name='Comunicação Oral')
    #avaliacaoAD_id = models.ForeignKey(avaliacaoad_avaliacaoad, on_delete=models.PROTECT)
    #ComunicOral_id = models.ForeignKey(comunicoral_comunicoral, on_delete=models.PROTECT)
    resp_oralidade = models.CharField(max_length=1, verbose_name='Resp. Oralidade',default="N",choices=(
        ('S', 'Sim'),
        ('N', 'Nâo'),
    ))
    
    def __str__(self):
        return str(self.resp_oralidade)
    

class TipoVoz(models.Model):
    descricao = models.CharField(max_length=150)
    
    class Meta:
        verbose_name_plural = "Tipo de Voz"
        
    def __str__(self):
        return self.descricao
    
    
class Ressonancia(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Tipo de Ressonancia"
        
    def __str__(self):
        return self.descricao
    
class AtaqueVocal(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Ataque Vocal"
        
    def __str__(self):
        return self.descricao

class Pitch(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Pitch"
        
    def __str__(self):
        return self.descricao            
    
class Loudness(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Loudness"
        
    def __str__(self):
        return self.descricao
    
class Modulacao(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Modulação"
        
    def __str__(self):
        return self.descricao    

class Qualidadeemis(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Qualidade na Emissão"
        
    def __str__(self):
        return self.descricao   
    
## cadastro das avalições

class TipoVozCad(models.Model):
    avaliacaoAD_id = models.ForeignKey(avaliacaoad_avaliacaoad, on_delete=models.PROTECT, verbose_name='Avaliação')
    tipovoz_id = models.ForeignKey(TipoVoz, on_delete=models.PROTECT, verbose_name='Tipo de Voz')
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
    avaliacaoAD = models.ForeignKey(avaliacaoad_avaliacaoad, on_delete=models.PROTECT)
    ressonancia = models.ForeignKey(Ressonancia, on_delete=models.PROTECT)
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
    avaliacaoAD = models.ForeignKey(avaliacaoad_avaliacaoad, on_delete=models.PROTECT)
    ataquevocal = models.ForeignKey(AtaqueVocal, on_delete=models.PROTECT)
    resposta = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
            )
    )
    
class PitchCad(models.Model):
    avaliacaoAD = models.ForeignKey(avaliacaoad_avaliacaoad, on_delete=models.PROTECT)
    pitch = models.ForeignKey(Pitch, on_delete=models.PROTECT)
    resposta = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )   
    
class LoudnessCad(models.Model):
    avaliacaoAD = models.ForeignKey(avaliacaoad_avaliacaoad, on_delete=models.PROTECT)
    loudness = models.ForeignKey(Loudness, on_delete=models.PROTECT)
    resposta = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )   
  
class ModulacaoCad(models.Model):
    avaliacaoAD = models.ForeignKey(avaliacaoad_avaliacaoad, on_delete=models.PROTECT)
    modulacao = models.ForeignKey(Modulacao, on_delete=models.PROTECT)
    resposta = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )    
    
class QualidadeemisCad(models.Model):
    avaliacaoAD = models.ForeignKey(avaliacaoad_avaliacaoad, on_delete=models.PROTECT)
    qualidadeemis = models.ForeignKey(Qualidadeemis, on_delete=models.PROTECT)
    resposta = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )    
    
            