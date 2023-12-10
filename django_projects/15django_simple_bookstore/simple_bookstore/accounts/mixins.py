from django import dispatch
from django.http import HttpResponseRedirect
from django.urls import reverse


class UserRequiredMixin:
    # Ensures the user is authenticated
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"), *args, **kwargs)

        return super().dispatch(request, *args, **kwargs)
