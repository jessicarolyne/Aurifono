from django.contrib import admin
from . import models

class ComunicOralidadeInline(admin.TabularInline):
    model = models.ComunicOralidade
    extra = 1
    

class AvalidacaoADAdmin(admin.ModelAdmin):
    #filter_horizontal = ('DataAvaliacao',)
    inlines = [
        ComunicOralidadeInline,
    ]


class ListandoAvaliacaoAD(admin.ModelAdmin):
    list_display = ('id', 'DataAvaliacao', 'QOrelha', 'paciente')
    
   

admin.site.register(models.AvaliacaoAD, AvalidacaoADAdmin)
admin.site.register(models.ComunicOralidade)
