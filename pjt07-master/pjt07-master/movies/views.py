from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm, ReviewForm
from .models import Movie, Review, Genre
from django.contrib.auth.decorators import login_required


def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {'movies': movies ,}
    return render(request, 'index.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review_form = ReviewForm()
    reviews = movie.review_set.all()
    context = {
        'movie': movie,
        'review_form': review_form,
        'reviews': reviews,
    }
    return render(request, 'detail.html', context)

@login_required
def create_review(request, movie_pk):
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviews = form.save(commit=False)
            reviews.user = request.user
            reviews.movie_id = movie_pk
            reviews.save()
            return redirect('movies:detail', movie_pk)
        return redirect('movies:index')

def delete_review(request, movie_pk, review_pk):
    if request.method == 'POST':
        review = get_object_or_404(Review, pk=review_pk)
        if review.user == request.user:
            review.delete()
        return redirect('movies:detail', movie_pk)


def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    return redirect('movies:index')
    