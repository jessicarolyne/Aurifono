from django.shortcuts import render
from loudness.forms import LoudnessForm
from loudness.models import Loudness

def loudness(request):
    if request.method == 'GET':
        
        loudnesss = Loudness.objects.all()
        
        form = LoudnessForm()
        
        context = {
            'loudnesss' : loudnesss,
            'form' : form,
        }
        
        return render(request, 'loudness.html', context=context)
    elif request.method == 'POST':
        form = LoudnessForm(request.POST)
        
        if form.is_valid():
            
            loudnessv = form.save()
            form = LoudnessForm()
            
        context = {
            'form' : form
        }
            
        return render(request, 'loudness.html', context=context)
        