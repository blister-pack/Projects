from urllib import response
from django.test import TestCase
from django.urls import reverse
from .models import Article

# Create your tests here.


class ArticleTest(TestCase):
    def setUp(self) -> None:
        self.test_article = Article.objects.create(
            title="Test title",
            content="Test content",
        )

    def test_article_creation(self):
        self.assertEqual(self.test_article.title, "Test title")
        self.assertEqual(self.test_article.content, "Test content")

    def test_article_list_status(self):
        response = self.client.get(reverse("article-list"))
        self.assertEqual(response.status_code, 200)

    def test_article_create_view_template(self):
        response = self.client.get(reverse("article-create"))
        self.assertTemplateUsed(response, "myapp/create_article_form.html")
