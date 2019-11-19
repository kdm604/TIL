from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20)
    audience = models.IntegerField()
    open_date = models.DateTimeField(auto_now=False)
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    desription = models.TextField()


