from django.shortcuts import render
from .models import Item
from django.views.generic import ListView

# Create your views here.


class MyItemList(ListView):
    model = Item
    template_name = "myapp/my_item_list.html"
    context_object_name = "items"
