from django.db import models

class Loudness(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Loudness"
        
    def __str__(self):
        return self.descricao
