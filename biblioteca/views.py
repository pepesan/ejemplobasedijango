from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from biblioteca.models import Genre

class GenreListView(ListView):

    model = Genre
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GenreDetailView(DetailView):

    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class GenreCreate(CreateView):
    model = Genre
    fields = ['name']


class GenreUpdate(UpdateView):
    model = Genre
    fields = ['name']
    template_name_suffix = '_update_form'

class GenreDelete(DeleteView):
    model = Genre
    success_url = reverse_lazy('genre-list')

import django_tables2 as tables

class GenreTable(tables.Table):
    class Meta:
        model = Genre

def simple_list(request):

    table = GenreTable(Genre.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'biblioteca/simple_list.html', {'table': table})


@csrf_exempt
def list_json(request):
    data={'error':"No hay Datos"}
    status=500
    try:
        #data['objetos']=serialize('json', Genre.objects.all())
        data['objetos'] = list(Genre.objects.all().values('id','name'))

        print(data['objetos'])
        status=200
        del data['error']
    except:
        print ('Fallo al acceder a la BBDD')
    return JsonResponse(data,status=status)

@csrf_exempt
def get_json(request,pk):
    data = {'error': "No hay Datos"}
    status = 500
    try:
        #data['objetos']=serialize('json', Genre.objects.all())
        data['objeto'] = list(Genre.objects.filter(id=pk).values('id','name'))[0]
        #print(data['objeto'])
        status=200
        del data['error']
    except:
        print ('Fallo al acceder a la BBDD')
    return JsonResponse(data,status=status)