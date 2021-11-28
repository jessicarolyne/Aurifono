from django.contrib import admin
from .models import ProfissionalEnc

class ListandoProfissionalEnc(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(ProfissionalEnc, ListandoProfissionalEnc)
