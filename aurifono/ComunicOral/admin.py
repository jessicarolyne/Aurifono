from django.contrib import admin
from .models import ComunicOral

class ListandoComunicacaoOral(admin.ModelAdmin):
    list_display = ('id', 'dsc_habilidade')

    
admin.site.register(ComunicOral, ListandoComunicacaoOral)    
