from django.shortcuts import render, redirect
from ComunicOral.forms import ComunicOralForm
from ComunicOral.models import ComunicOral
 
def comunicoral(request):
    if request.method == 'GET':
        comunicorals = ComunicOral.objects.all()
        form = ComunicOralForm()
        context = {
            'comunicorals': comunicorals,
            'form': form,
        }
        
        return render(request, 'comunicoral.html', context=context)
    elif request.method == 'POST':
        form = ComunicOralForm(request.POST)
        
        if form.is_valid():
            comunic = form.save()
            form = ComunicOralForm()
        
        context = {
            'form': form
        }
        
        return render(request, 'comunicoral.html', context=context)

def vercomunicoral(request, pk):
    data = {}
    data['comunic'] = ComunicOral.objects.get(pk=pk)
    return render(request, 'vercomunicoral.html', data) 

def editcomunicoral(request, pk):
    data = {}
    data['comunic'] = ComunicOral.objects.get(pk=pk)
    data['form'] = ComunicOralForm(instance=data['comunic'])
    return render(request, 'comunicoral.html', data) 
    

def updatecomunicoral(request, pk):
    data = {}
    data['comunic'] = ComunicOral.objects.get(pk=pk)
    form = ComunicOralForm(request.POST, instance=data['comunic'])
    if form.is_valid():
        form.save()
        return redirect('comunicoral')  

def deletecomunicoral(request, pk):
    comunic = ComunicOral.objects.get(pk = pk)
    comunic.delete() 
    return redirect('/comunicoral/') 

def paginacao(request):
    data = {}
    all = ComunicOral.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'comunicoral.html', data)

def busca(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = ComunicOral.objects.filter(nome__icontains=search)
    else:
        data['db'] = ComunicOral.objects.all()
     
    return render(request, 'comunicoral.html', data)


