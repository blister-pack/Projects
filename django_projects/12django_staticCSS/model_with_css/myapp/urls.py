from django.urls import path
from . import views

urlpatterns = [
    path("", views.MyItemList.as_view(), name="list-view"),
]
