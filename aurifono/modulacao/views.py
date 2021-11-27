from django.shortcuts import render
from modulacao.forms import ModulacaoForm
from modulacao.models import Modulacao

def modulacao(request):
    if request.method == 'GET':
        
        modulacaos = Modulacao.objects.all()
        
        form = ModulacaoForm()
        
        context = {
            'modulacaos' : modulacaos,
            'form' : form,
        }
        return render(request, 'modulacao.html', context=context)
    elif request.method == 'POST':
        
        form = ModulacaoForm(request.POST)
        if form.is_valid():
            
            modulacaov = form.save()
            form = ModulacaoForm()
            
        context = {
            'form' : form
        }   
        return render(request, 'modulacao.html', context=context) 
        