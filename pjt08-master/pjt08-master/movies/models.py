from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=40)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Review(models.Model):
    content = models.CharField(max_length=40)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
