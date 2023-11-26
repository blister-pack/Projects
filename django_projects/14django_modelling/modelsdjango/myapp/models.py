from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})
