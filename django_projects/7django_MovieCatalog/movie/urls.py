from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_list, name="movie-list"),
    path("<int:pk>/", views.movie_details, name="movie-details"),
    path("search/", views.search_bar, name="search-bar"),
    path("search/title=<str:term>/", views.search_movies, name="movie-search"),
    path("good_search/", views.good_search_bar, name="gud-search"),
    path("create_movie/", views.create_movie, name="create-movie"),
]


# only use the as_view() when you're using class-based views
