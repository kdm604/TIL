from django.contrib import admin
from .models import Movie,Review,Genre

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'audience', 'poster_url', 'description', 'genre_id',)

@admin.register(Review)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'score', 'movie_id', 'user_id',)

@admin.register(Genre)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)