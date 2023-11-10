from django import forms


class CreateMovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=50)
    year = forms.IntegerField()
    director = forms.CharField(max_length=50)
    description = forms.CharField(max_length=500)
