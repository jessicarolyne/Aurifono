from django.db import models
 
class Ressonancia(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Tipo de Ressonancia"
        
    def __str__(self):
        return self.descricao 
