from django.db import models

class AtaqueVocal(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Ataque Vocal"
        
    def __str__(self):
        return self.descricao