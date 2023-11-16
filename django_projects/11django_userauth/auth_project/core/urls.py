from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProtectedView.as_view(), name="protected"),
]
