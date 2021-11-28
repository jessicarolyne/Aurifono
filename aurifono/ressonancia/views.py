from django.shortcuts import redirect, render, resolve_url
from ressonancia.forms import RessonanciaForm
 
from ressonancia.models import Ressonancia

def ressonancia(request):
    if request.method == "GET":
        
        ressonancias = Ressonancia.objects.all()
        
        form = RessonanciaForm()
        
        context = {
            'ressonancias' : ressonancias,
            'form' : form,
        }
        return render(request, 'ressonancia.html', context=context)
    elif request.method == 'POST':
        
        form = RessonanciaForm(request.POST)
        if form.is_valid():
            
            ressonanciaf = form.save()
            form = RessonanciaForm
        
        context = {
            'form' : form
        }    
        
        return render(request, 'ressonancia.html', context=context)
    
def verressonancia(request, pk):
    data = {}
    data['ressona'] = Ressonancia.objects.get(pk=pk)
    return render(request, 'verressonancia.html', data) 

def editressonancia(request, pk):
    data = {}
    data['ressona'] = Ressonancia.objects.get(pk=pk)
    data['form'] = RessonanciaForm(instance=data['ressona'])
    return render(request, 'ressonancia.html', data) 
    

def updateressonancia(request, pk):
    data = {}
    data['ressona'] = Ressonancia.objects.get(pk=pk)
    form = RessonanciaForm(request.POST, instance=data['ressona'])
    if form.is_valid():
        form.save()
        return redirect('ressonancia')  

def deleteressonancia(request, pk):
    ressona = Ressonancia.objects.get(pk = pk)
    ressona.delete() 
    return redirect('/ressonancia/') 

def paginacao(request):
    data = {}
    all = ressonancia.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'ressonancia.html', data)

def busca(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Ressonancia.objects.filter(nome__icontains=search)
    else:
        data['db'] = Ressonancia.objects.all()
     
    return render(request, 'ressonancia.html', data)        