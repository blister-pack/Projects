from django.shortcuts import render
from django.views.generic import TemplateView
from .mixins import UserAuthMixin

# Create your views here.


class ProtectedView(UserAuthMixin, TemplateView):
    template_name = "core/protected.html"
