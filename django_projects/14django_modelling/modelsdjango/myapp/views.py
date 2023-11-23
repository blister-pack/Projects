from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import Article
from .forms import CreateArticleForm


# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = "myapp/articles.html"
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "myapp/article_detail.html"
    context_object_name = "article"


class ArticleCreateView(CreateView):
    model = Article
    form_class = CreateArticleForm
    template_name = "myapp/create_article_form.html"
    success_url = "article/"
