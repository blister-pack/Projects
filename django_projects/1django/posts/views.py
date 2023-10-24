from django.shortcuts import render
from django.http import HttpResponse
from .data import POSTS

# Create your views here.

def postsView(request):
    return HttpResponse(POSTS)