from django.shortcuts import render, redirect

from movie.forms import CreateMovieForm

from .models import Movie
from django.contrib import messages

# Create your views here.


def movie_list(request):
    context = {
        "movies": Movie.objects.all(),
    }
    return render(request, "movie/all_movies.html", context)


def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, "movie/movie_details.html", {"movie": movie})


def search_movies(request, term):
    movies = Movie.objects.filter(title__icontains=term)
    return render(request, "movie/movie_search.html", {"movies": movies})


def search_bar(request):
    if request.method == "POST":
        search_term = request.POST.get("search_term")
        return redirect("movie-search", term=search_term)
    return render(request, "movie/search_bar.html")


def good_search_bar(request):
    g_search_term = request.GET.get("good_search_term")

    if g_search_term:
        movies = Movie.objects.filter(title__icontains=g_search_term)
    else:
        movies = Movie.objects.all()

    return render(request, "movie/good_search.html", {"movies": movies})


def create_movie(request):
    if request.method == "POST":
        form = CreateMovieForm(request.POST)
        if form.is_valid():
            form.save()
            # movie_title = form.cleaned_data.get("title")
            # messages.success(request, f"Movie saved - {movie_title}")
            return redirect("movie-list")
    else:
        form = CreateMovieForm()
    return render(request, "movie/create_movie.html", {"form": form})
