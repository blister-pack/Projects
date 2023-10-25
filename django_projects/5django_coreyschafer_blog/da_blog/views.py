from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "da_blog/home.html")


def about(request):
    return render(request, "da_blog/about.html")
