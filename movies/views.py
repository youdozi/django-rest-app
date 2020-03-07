from django.shortcuts import render
from rest_framework import viewsets

from .MovieSerializer import MovieSerializer
from .models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
