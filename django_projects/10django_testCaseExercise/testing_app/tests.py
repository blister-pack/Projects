from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.template import Context, Template
from testing_app.views import home_view, about_view

# Create your tests here.


class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "testing_app/home.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the homepage!")


class AboutViewTest(TestCase):
    def test_about_view(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "testing_app/about.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About us page.")
