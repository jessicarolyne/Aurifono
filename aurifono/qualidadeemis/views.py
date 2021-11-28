from django.shortcuts import render
from qualidadeemis.forms import QualidadeemisForm
from qualidadeemis.models import Qualidadeemis

def qualidadeemis(request):
    if request.method == 'GET':
        
        qualidadeemiss = Qualidadeemis.objects.all()
        
        form = QualidadeemisForm()
        
        context = {
            'qualidadeemiss' : qualidadeemiss,
            'form' : form,
        }
        return render(request, 'qualidadeemis.html', context=context)
    elif request.method == 'POST':    
        form = QualidadeemisForm(request.POST)
        if form.is_valid():
            
            qualidadeemisv = form.save()
            form = QualidadeemisForm()
            
        context = {
            'form' : form
        }
        return render(request, 'qualidadeemis.html', context=context)
            