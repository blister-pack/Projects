from django import forms
from .models import Movie


class CreateMovieForm(forms.ModelForm):
    # title = forms.CharField(max_length=100)
    # genre = forms.CharField(max_length=50)
    # year = forms.IntegerField()
    # director = forms.CharField(max_length=50)
    # description = forms.CharField(max_length=500)

    class Meta:
        model = Movie
        fields = ["title", "genre", "year", "director", "description"]
