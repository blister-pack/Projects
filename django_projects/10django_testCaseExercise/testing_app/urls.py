from nturl2path import url2pathname
from django.urls import path
from .views import home_view, about_view

urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
]
