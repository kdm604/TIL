from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre, Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Movieserializer, Genreserializer, Reviewserializer, GenreDetailserializer
from IPython import embed

@api_view(['GET'])
def movies_list(request):
    movies = Movie.objects.all()
    serializer = Movieserializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genres_list(request):
    genres = Genre.objects.all()
    serializer = Genreserializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genres_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreDetailserializer(genre)
    return Response(serializer.data)

@api_view(['GET'])
def movies_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = Movieserializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def reviews_create(request, movie_pk):
    serializer = Reviewserializer(data=request.data)
    # embed()
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id = movie_pk)
    return Response({'message': '작성되었습니다.'})

@api_view(['PUT', 'DELETE'])
def reviews_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        serializer = Reviewserializer(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '수정되었습니다.'})
    else:
        review.delete()
        return Response({'message': '삭제되었습니다.'})