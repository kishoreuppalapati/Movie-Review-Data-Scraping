from django.shortcuts import render
from django.views.generic import ListView

from .models import Movie

class HomeView(ListView):
    template_name = 'home.html'
    model = Movie

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set
        