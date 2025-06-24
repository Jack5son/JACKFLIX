from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from . import forms
from . import models

def cadastro(request):
    form = forms.FilmeForm()
    if request.method == 'POST':
        print("Vou salvar os dados!")
        form = forms.FilmeForm(request.POST)

        if form.is_valid():
            print("Salvando")
            form.save(commit=True)
        else:
            print('error')
    filmes_list = models.Filme.objects.order_by('nome');
    data_dict = {'form': form, 'filme_records': filmes_list}
    return render(request, 'filme/filme.html', data_dict)


def delete(request, id):
    try:
        models.Filme.objects.filter(id=id).delete()
        form = forms.FilmeForm()
        filmes_list = models.Filme.objects.order_by('nome')
        data_dict = {'form': form, 'filme_records': filmes_list}
        return render(request, 'filme/filme.html', data_dict)
    except:
        return HttpResponseNotAllowed

def update(request, id):
    item = models.Filme.objects.get(id=id)
    form = forms.FilmeForm(request.POST or None, instance=item)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('filme_list') # Assumindo que você tenha um nome de URL

    data_dict = {'form': form, 'id': id}
    return render(request, 'filme/filme.upd.html', data_dict)
