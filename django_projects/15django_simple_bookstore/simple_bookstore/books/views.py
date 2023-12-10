from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from accounts.mixins import UserRequiredMixin
from .models import Book
from .forms import CreateBookForm

# Create your views here.


class BookListView(UserRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"


class BookDetailView(UserRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"


class BookCreateView(UserRequiredMixin, CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = "books/book_create.html"
    success_url = "/books/"


class BookUpdateView(UserRequiredMixin, UpdateView):
    model = Book
    template_name = "books/book_update.html"
    fields = "__all__"
    success_url = "/books/"


class BookDeleteView(UserRequiredMixin, DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = "/books/"
