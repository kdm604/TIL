from django.contrib import admin
from .models import Movie,Review,Genre

class MovieAdmin(admin.ModelAdmin):
  list_display = ('pk', 'title',)
admin.site.register(Movie, MovieAdmin)

class GenreAdmin(admin.ModelAdmin):
  list_display = ('pk', 'name',)
admin.site.register(Genre, GenreAdmin)

class ReviewAdmin(admin.ModelAdmin):
  list_display = ('pk','content', )
admin.site.register(Review, ReviewAdmin)
