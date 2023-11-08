from django.shortcuts import render
from .data import POSTS

# Create your views here.

def post_view(request):
    return render(request, "library_posts/postpage.html", {"posts": POSTS})