from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookUpdateView,
    BookCreateView,
    BookDeleteView,
)

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("create/", BookCreateView.as_view(), name="book_create"),
    path("edit_book<int:pk>/", BookUpdateView.as_view(), name="book_edit"),
    path("delete_book<int:pk>/", BookDeleteView.as_view(), name="book_delete"),
]
