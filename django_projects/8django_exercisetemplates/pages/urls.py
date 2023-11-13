from django.urls import path
from . import views

urlpatterns = [
    path("", views.SayHelloView.as_view(), name="hello-view"),
    path("about/", views.AboutView.as_view(), name="about-view"),
]
