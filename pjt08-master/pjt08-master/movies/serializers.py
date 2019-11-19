from rest_framework import serializers
from .models import Movie, Genre, Review

class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'audience', 'poster_url', 'description', 'genre_id', )


class Genreserializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', )

class GenreDetailserializer(Genreserializer):
    movies = Movieserializer(source='movie_set', many=True)

    class Meta(Genreserializer.Meta):
      fields = Genreserializer.Meta.fields + ('movies', )



class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'content', 'score', 'movie_id', )


