from django.urls import path
from .views import postsView

urlpatterns = [path("", postsView, name="home")]
