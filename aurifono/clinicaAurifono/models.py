from django.db import models
from django.db.models.base import Model
from django.db.models.fields import TextField

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
        ('DI', 'DIREITA')
    )
    DataAvaliacao = models.DateField(verbose_name='Data da Avaliação')
    QOrelha = models.CharField(
        max_length=2,
        choices=ORELHA
    )
    paciente_id = models.ForeignKey(paciente_paciente, on_delete=models.PROTECT, verbose_name='Paciente')
    def __str__(self):
        return "{} ({})".format(self.paciente_id, self.DataAvaliacao)

class comunicoral_comunicoral(models.Model):
    dsc_habilidade = models.CharField(max_length=150, verbose_name='Descrição da Habilidade')
    def __str__(self):
        return self.dsc_habilidade

class comunicoralidade_comunicoralidade(models.Model):
    resp_oralidade = models.CharField(max_length=1, verbose_name='Resp. Oralidade')
    ComunicOral_id = models.ForeignKey(comunicoral_comunicoral, on_delete=models.PROTECT, verbose_name='Comunicação Oral')
    avaliacaoAD_id = models.ForeignKey(avaliacaoad_avaliacaoad, on_delete=models.PROTECT, verbose_name='Avaliação')
    def __str__(self):
        return self.resp_oralidade