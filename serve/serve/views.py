from django.views.generic import ListView

from . models import Movie

class HomeView(ListView):
    template_name = 'home.html'
    
    def get_queryset(self):
        return Movie.objects.all()
        