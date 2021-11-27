from django.shortcuts import redirect, render
from ataquevocal.forms import AtaqueVocalForm
from ataquevocal.models import AtaqueVocal
# Create your views here.

def ataquevocal(request):
    if request.method =='GET':
        
        ataquevocals = AtaqueVocal.objects.all()
        
        form = AtaqueVocalForm()
        
        context = {
            'ataquevocals' : ataquevocals,
            'form' : form,
        }
        return render (request, 'ataquevocal.html', context=context)
    elif request.method == 'POST':
        
        form = AtaqueVocalForm(request.POST)
        
        if form.is_valid():
            
            ataquev = form.save()
            form = AtaqueVocalForm()
        
        context = {
            'form' : form
        }    
        return render(request, 'ataquevocal.html', context=context)

def verataquevocal(request, pk):
    data = {}
    data['ataquevocal'] = AtaqueVocal.objects.get(pk=pk)
    return render(request, 'verataquevocal.html', data) 

def editataquevocal(request, pk):
    data = {}
    data['ataquevocal'] = AtaqueVocal.objects.get(pk=pk)
    data['form'] = AtaqueVocalForm(instance=data['ataquevocal'])
    return render(request, 'ataquevocal.html', data) 
    

def updateataquevocal(request, pk):
    data = {}
    data['ataquevocal'] = AtaqueVocal.objects.get(pk=pk)
    form = AtaqueVocalForm(request.POST, instance=data['ataquevocal'])
    if form.is_valid():
        form.save()
        return redirect('ataquevocal')  

def deleteataquevocal(request, pk):
    ataquevocal = AtaqueVocal.objects.get(pk = pk)
    ataquevocal.delete() 
    return redirect('/ataquevocal/') 

def paginacao(request):
    data = {}
    all = ataquevocal.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'ataquevocal.html', data)

def busca(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = AtaqueVocal.objects.filter(nome__icontains=search)
    else:
        data['db'] = AtaqueVocal.objects.all()
     
    return render(request, 'ataquevocal.html', data)        