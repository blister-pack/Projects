from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    bio = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


"""
models.CASCADE makes it so that if a user is deleted, any
profile instance that is related to that user is also deleted
"""
