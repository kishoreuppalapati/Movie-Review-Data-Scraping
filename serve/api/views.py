from rest_framework import generics

from serve.models import Movie
from .serializers import MovieSerializer
from .serializers import MovieNameSerializer
from .serializers import MovieYearSerializer
from .serializers import MovieYearNoSerializer

# Create your views here.
class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieAPIViewIDBase(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieAPIViewNameBase(generics.ListAPIView):
    queryset = Movie.objects.only('Name')
    serializer_class = MovieNameSerializer

class MovieAPIViewYearBase(generics.ListAPIView):
    queryset = Movie.objects.only('YearNo')
    serializer_class = MovieYearSerializer

class MovieAPIViewYearNoBase(generics.ListAPIView):
    queryset = Movie.objects.only('YearNo')
    serializer_class = MovieYearNoSerializer

