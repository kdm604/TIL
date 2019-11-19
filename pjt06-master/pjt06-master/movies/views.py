from django.shortcuts import render, redirect , get_object_or_404
from .models import Movie, Comment
from .forms import MovieForm, CommentForm

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies ,}
    return render(request, 'movies/index.html', context) 

def create(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('movies:index')
    else:
        context = {'form':form ,}
        return render(request, 'movies/forms.html', context) 

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment_form = CommentForm()
    comments = Comment.objects.all()
    context = {'movie': movie , 'comment_form':comment_form , 'comments':comments}
    return render(request, 'movies/detail.html', context)

def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
        return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
        context = {'form':form ,}
        return render(request, 'movies/forms.html', context)

def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
    return redirect('movies:index')

def comments_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie_id = movie.pk
            comment = comment_form.save()
    return redirect('movies:detail', movie.pk)
   



        