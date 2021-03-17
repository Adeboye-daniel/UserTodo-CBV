from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import table

class taskListView(ListView):
    model = table
    template_name = "list.html"

class taskCreateView(CreateView):
    model = table
    template_name = "create.html"
    fields = '__all__'


class taskUpdateiew(UpdateView):
    model = table
    template_name = "update.html"
    fields = '__all__'

class taskdetailView(DetailView):
    model = table
    template_name='detail.html'
    context_object_name = 'task'

class taskdeleteView(DeleteView):
    model = table
    template_name = "delete.html"
    context_object_name = 'task'
    success_url = reverse_lazy('list')

