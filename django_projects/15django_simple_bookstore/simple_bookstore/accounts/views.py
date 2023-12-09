from wsgiref.util import request_uri
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup_view(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # this passes the post request date into the form

        if form.is_valid():
            form.save()

    return render(request, "accounts/signup.html", {"form": form})
