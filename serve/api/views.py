from rest_framework import generics

from serve.models import Movie
from .serializers import MovieSerializer

# Create your views here.
class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
