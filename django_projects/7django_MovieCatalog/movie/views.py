from django.shortcuts import render
from .models import Movie


# Create your views here.
context = {
    "movies": Movie.objects.all(),
}


def movie_list(request):
    return render(request, "movie/all_movies.html", context)


def movie_details(request):
    return render(request, "movie/movie_details.html", context)


def search_movies(request):
    pass
