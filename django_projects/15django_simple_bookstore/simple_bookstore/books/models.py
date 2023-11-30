from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("book_edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("book_delete", kwargs={"pk": self.pk})
