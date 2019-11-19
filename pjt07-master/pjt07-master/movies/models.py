from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Genre(models.Model):
    name = models.CharField(max_length=40)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=300)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies", blank=True)

class Review(models.Model):
    content = models.CharField(max_length=40)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    