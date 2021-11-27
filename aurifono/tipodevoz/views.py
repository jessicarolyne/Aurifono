from django.shortcuts import redirect, render
from tipodevoz.forms import TipoVozForm
from tipodevoz.models import TipoVoz

def tipodevoz(request):
    if  request.method == 'GET':
        
        tipovozs = TipoVoz.objects.all()
        
        form = TipoVozForm()
        
        context = {
            'tipovozs' : tipovozs,
            'form' : form,
        }
        return render(request, 'tipodevoz.html', context=context)
    elif request.method == 'POST':
        form = TipoVozForm(request.POST)
         
        if form.is_valid():
            
            tipov = form.save()
            form = TipoVozForm()
         
        context = {
            'form': form
        }
        return render(request, 'tipodevoz.html', context=context)
    
def vertipodevoz(request, pk):
    data = {}
    data['tipodevoz'] = TipoVoz.objects.get(pk=pk)
    return render(request, 'vertipodevoz.html', data) 

def edittipodevoz(request, pk):
    data = {}
    data['tipodevoz'] = TipoVoz.objects.get(pk=pk)
    data['form'] = TipoVozForm(instance=data['tipodevoz'])
    return render(request, 'tipodevoz.html', data) 
    

def updatetipodevoz(request, pk):
    data = {}
    data['tipodevoz'] = TipoVoz.objects.get(pk=pk)
    form = TipoVozForm(request.POST, instance=data['tipodevoz'])
    if form.is_valid():
        form.save()
        return redirect('tipodevoz')  

def deletetipodevoz(request, pk):
    tipodevoz = TipoVoz.objects.get(pk = pk)
    tipodevoz.delete() 
    return redirect('/tipodevoz/') 

def paginacao(request):
    data = {}
    all = TipoVoz.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'tipodevoz.html', data)

def busca(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = TipoVoz.objects.filter(nome__icontains=search)
    else:
        data['db'] = TipoVoz.objects.all()
     
    return render(request, 'tipodevoz.html', data)    