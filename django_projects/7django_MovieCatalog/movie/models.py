from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    director = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.title}, {self.year}, directed by {self.director}"
