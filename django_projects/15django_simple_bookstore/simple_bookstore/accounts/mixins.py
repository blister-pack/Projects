from django.http import HttpResponseRedirect
from django.urls import reverse

class UserRequiredMixin:
    # Ensures the user is authenticated
    def dispatch(self, request, *args, **kwargs):
        pass
    
    pass