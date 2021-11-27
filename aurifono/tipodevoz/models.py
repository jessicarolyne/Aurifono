from django.db import models
 
class TipoVoz(models.Model):
    descricao = models.CharField(max_length=150)
    
    class Meta:
        verbose_name_plural = "Tipo de Voz"
        
    def __str__(self):
        return self.descricao
        