from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('movies/', views.movies_list, name='movies_list'),
    path('genres/', views.genres_list, name='genres_list'),
    path('genres/<int:genre_pk>/', views.genres_detail, name='genres_detail'),
    path('movies/<int:movie_pk>/', views.movies_detail, name='movies_detail'),
    path('movies/<int:movie_pk>/reviews/', views.reviews_create, name='reviews_create'),
    path('reviews/<int:review_pk>/', views.reviews_update_delete, name='reviews_udpate_delete'),
]
