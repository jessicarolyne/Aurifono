from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import profissionalEncForm
from .models import ProfissionalEnc
from django.core.paginator import Paginator
#from paciente.models import Paciente
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def profissional(request, id):
    profissional = get_object_or_404(ProfissionalEnc, pk=id)
    return render(request, 'clinicaAurifono/profissional.html', {'profissional' : profissional})

@login_required
def novoProfissional(request):
    if request.method == 'POST':
        form = ProfissionalEnc(request.POST)
        if form.is_valid():
            profissional_profissional = form.save(commit=False)
            profissional_profissional.save()
            return redirect('../buscarProfissional')
    else:
        form = ProfissionalEnc()
        return render(request, 'clinicaAurifono/novoProfissional.html', {'form' : form})

@login_required
def editarProfissional(request, id):
    profissional = get_object_or_404(ProfissionalEnc, pk=id)
    form = profissionalEncForm(instance=profissional)
    if request.method == 'POST':
        form = profissionalEncForm(request.POST, instance=profissional)
        if form.is_valid():
            profissional.save()
            return redirect('../buscar')
        else:
            return render(request, 'clinicaAurifono/editar.html', {'form' : form, 'profissional' : profissional})
    else:
        return render(request, 'clinicaAurifono/editarProfissional.html', {'form' : form, 'profissional' : profissional})

@login_required
def excluirProfissional(request, id):
    profissional = get_object_or_404(ProfissionalEnc, pk=id)
    profissional.delete()
    messages.info(request,'Profissional excluído com sucesso!')
    return redirect('../buscarProfissional')

@login_required
def buscaProfissional(request):
    busca = request.GET.get('busca')
    if busca:
        profissionais = ProfissionalEnc.objects.filter(nome__icontains=busca)
    else:
        profissionais_lista = ProfissionalEnc.objects.all()
        paginator = Paginator(profissionais_lista, 8)
        page = request.GET.get('page')
        profissionais = paginator.get_page(page)
    return render(request, 'clinicaAurifono/buscarProfissional.html', {'profissionais' : profissionais})

# def profissionalenc(request):
#     if request.method == 'GET':
#         profissionalencs = ProfissionalEnc.objects.all()
#         form = ProfissionalEncForm()
#         context = {
#             'profissionalencs' : profissionalencs,
#             'form' : form,
#         }
#         return render(request, 'profissionalenc.html', context)
#     elif request.method == 'POST':
#         form = ProfissionalEncForm(request.POST)
#         if form.is_valid():
#             profissional = form.save()
#             form = ProfissionalEncForm()
#         context = { 
#            'form' : form,
#         }
#         return render(request, 'profissionalenc.html', context=context)

# def verprofissional(request, pk):
#     data = {}
#     data['prof'] = ProfissionalEnc.objects.get(pk=pk)
#     return render(request, 'verprofissional.html', data) 

# def editprofissional(request, pk):
#     data = {}
#     data['prof'] = ProfissionalEnc.objects.get(pk=pk)
#     data['form'] = ProfissionalEncForm(instance=data['prof'])
#     return render(request, 'profissionalenc.html', data) 
#     #return render(request, 'profissionalenc.html', data)
#     return redirect('ProfissionalEnc')

# def updateprofissional(request, pk):
#     data = {}
#     data['prof'] = ProfissionalEnc.objects.get(pk=pk)
#     form = ProfissionalEncForm(request.POST, instance=data['prof'])
#     if form.is_valid():
#         form.save()
#         return redirect('profissionalenc')  

# def deleteprofissional(request, pk):
#     prof = ProfissionalEnc.objects.get(pk = pk)
#     prof.delete() 
#     return redirect('profissionalenc') 

# def paginacao(request):
#     data = {}
#     all = ProfissionalEnc.objects.all()
#     paginator = Paginator(all, 5)
#     pages = request.GET.get('page')
#     data['db'] = paginator.get_page(pages)
#     return render(request, 'profissionalenc.html', data)

# def busca(request):
#     data = {}
#     search = request.GET.get('search')
#     if search:
#         data['db'] = ProfissionalEnc.objects.filter(nome__icontains=search)
#     else:
#         data['db'] = ProfissionalEnc.objects.all()
     
#     return render(request, 'profissionalenc.html', data)

"""def update(request, profissionalenc_id):
    if request.method == 'GET':
        profissionalencs = ProfissionalEnc.objects.all()
        profissionalenc = ProfissionalEnc.objects.filter(id=profissionalenc_id).first()
        
        form = ProfissionalEncForm(instance=profissionalenc)
        context = {
            'profissionalencs' : profissionalencs,
            'form' : form,
        }

        return render(request, 'profissionalenc.html', context)
          
    elif request.method == 'POST':
        profissionalenc = ProfissionalEnc.objects.filter(id=profissionalenc_id).first()
        form = ProfissionalEncForm(request.POST, instance=profissionalenc)
        if form.is_valid():
            form.save()
            #return redirect('/')
        else:
            profissionalencs = ProfissionalEnc.objects.all()
     
            context = {
                'profissionalencs' : profissionalencs,
                'form' : form,
            }
            return render(request, 'profissionalenc.html', context)
"""        