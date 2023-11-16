from django.http import HttpResponseForbidden

# Create your views here.


class UserAuthMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You are not a superuser.")

        return super().dispatch(request, *args, **kwargs)
