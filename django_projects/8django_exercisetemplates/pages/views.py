from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class SayHelloView(TemplateView):
    template_name = "pages/hello.html"


class AboutView(TemplateView):
    template_name = "pages/about.html"
