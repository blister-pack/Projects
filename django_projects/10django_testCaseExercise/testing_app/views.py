from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(
        request, "testing_app/home.html", {"message": "Welcome to the homepage!"}
    )


def about_view(request):
    return render(request, "testing_app/about.html", {"message": "About us page."})
