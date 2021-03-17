from django.shortcuts import render
from django.views.generic import ListView
from .models import table

class taskListView(ListView):
    model = table
    template_name = "list.html"

