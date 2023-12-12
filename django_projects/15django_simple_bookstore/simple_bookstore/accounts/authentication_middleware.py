import logging
from typing import Any
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


class AuthenticationMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Any:
        print(f"AuthenticationMiddleware: Processing request for {request.path}")
        # this code is executed before the view and
        # further middleware are called
        login_url = reverse("login")
        signup_url = reverse("signup")

        if request.path not in [login_url, signup_url]:
            if not request.user.is_authenticated:
                print("User is not authenticated. Redirecting to login.")
                # while not (request.path == reverse("login")):
                return redirect(reverse("login"))

        else:
            print("User is authenticated. Proceeding with the middleware.")

        response = self.get_response(request)

        # this code is executed after the view and
        # further middleware are called
        # this is determined by the response = self.get_response(request)
        print(
            f"AuthenticationMiddleware: Processing response with status code {response.status_code}"
        )

        return response
