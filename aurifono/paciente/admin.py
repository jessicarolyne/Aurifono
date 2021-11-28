from django.contrib import admin
from .models import Paciente

class ListandoPaciente(admin.ModelAdmin):
    list_display = ('id', 'nome', 'RG', 'CPF', 'DataCadastro', 'DataNascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10
admin.site.register(Paciente, ListandoPaciente)



