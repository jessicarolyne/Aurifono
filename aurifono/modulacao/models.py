from django.db import models

class Modulacao(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Modulação"
        
    def __str__(self):
        return self.descricao