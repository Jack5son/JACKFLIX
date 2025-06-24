from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from . import forms
from . import models

def cadastro(request):
    form = forms.SerieForm()
    if request.method == 'POST':
        print("Vou salvar os dados!")
        form = forms.SerieForm(request.POST)

        if form.is_valid():
            print("Salvando")
            form.save(commit=True)
        else:
            print('error')
    series_list = models.Serie.objects.order_by('nome');
    data_dict = {'form': form, 'serie_records': series_list}
    return render(request, 'serie/serie.html', data_dict)


def delete(request, id):
    try:
        models.Serie.objects.filter(id=id).delete()
        form = forms.SerieForm()
        series_list = models.Serie.objects.order_by('nome')
        data_dict = {'form': form, 'serie_records': series_list}
        return render(request, 'serie/serie.html', data_dict)
    except:
        return HttpResponseNotAllowed

def update(request, id):
    item = models.Serie.objects.get(id=id)
    form = forms.SerieForm(request.POST or None, instance=item)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('serie_list')

    data_dict = {'form': form, 'id': id}
    return render(request, 'serie/serie.upd.html', data_dict)
