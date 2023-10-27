from django.urls import path
from . import views

app_name = "da_blog"

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
]

# irrelevant test comment
