from django.shortcuts import render
from django.views.generic.list import ListView
from mongodbapp.models import *

# Create your views here.

class ToolListView(ListView):

    model = Tool
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
