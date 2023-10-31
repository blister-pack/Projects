from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# posts = [
#     {
#         "author": "DJ_BlyatMan",
#         "title": "Blog Post 1",
#         "content": "First post content",
#         "date_posted": "October 26, 2023",
#     },
#     {
#         "author": "Jane Doe",
#         "title": "Jane's hair routine",
#         "content": "You should be drying your hair by vigorously whipping it back and forth",
#         "date_posted": "October 22, 2023",
#     },
# ]


def home(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "da_blog/home.html", context)


def about(request):
    return render(request, "da_blog/about.html", {"title": "About"})
