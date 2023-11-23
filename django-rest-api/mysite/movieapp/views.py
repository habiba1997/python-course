from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializer import MovieSerializer


# Create your views here.
class MovieApiView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
