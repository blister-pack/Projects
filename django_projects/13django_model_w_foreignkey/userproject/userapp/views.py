from django.shortcuts import render
from .models import Profile
from django.views.generic import ListView, DetailView

# Create your views here.


class ProfileList(ListView):
    model = Profile
    template_name = "userapp/prof_view.html"
    context_object_name = "profiles"


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "userapp/prof_detail_view.html"
    context_object_name = "detail_profiles"
