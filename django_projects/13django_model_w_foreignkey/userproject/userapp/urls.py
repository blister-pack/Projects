from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProfileList.as_view(), name="profile-list"),
    path("detail/<int:pk>/", views.ProfileDetailView.as_view(), name="profile-detail"),
]
