from django.db import models

# Create your models here.
class Qualidadeemis(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Qualidade na Emissão"
        
    def __str__(self):
        return self.descricao