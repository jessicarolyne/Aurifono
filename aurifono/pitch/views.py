from django.shortcuts import render
from pitch.forms import PitchForm
from pitch.models import Pitch

def pitch(request):
    if request.method == 'GET':
        
        pitchs = Pitch.objects.all()
        
        form = PitchForm()
        
        context = {
            'pitchs' : pitchs,
            'form' : form,
        }
        return render(request, 'pitch.html', context=context)
    elif request.method == 'POST':    
        form = PitchForm(request.POST)
        if form.is_valid():
            
            pitchv = form.save()
            form = PitchForm()
            
        context = {
            'form' : form
        }
        return render(request, 'pitch.html', context=context)
            