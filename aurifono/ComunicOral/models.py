from django.db import models
 
class ComunicOral(models.Model):
   dsc_habilidade = models.CharField(max_length=150) 
   
   class Meta:
        verbose_name_plural = "Comunicação Oral Perguntas"
      
   def __str__(self):
        return self.dsc_habilidade
   
    
    

    

