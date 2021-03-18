from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import table
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


    


class taskListView(LoginRequiredMixin, generic.ListView):
    model = table
    template_name = "list.html"

class taskCreateView(LoginRequiredMixin, generic.CreateView):
    model = table
    template_name = "create.html"
    fields = '__all__'


class taskUpdateiew(LoginRequiredMixin, generic.UpdateView):
    model = table
    template_name = "update.html"
    fields = '__all__'

class taskdetailView(LoginRequiredMixin, generic.DetailView):
    model = table
    template_name='detail.html'
    context_object_name = 'task'

class taskdeleteView(LoginRequiredMixin, generic.DeleteView):
    model = table
    template_name = "delete.html"
    context_object_name = 'task'
    success_url = reverse_lazy('list')

