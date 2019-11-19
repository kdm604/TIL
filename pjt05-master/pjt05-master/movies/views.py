from django.shortcuts import render, redirect
from .models import Movies
def index(request):
    movies = Movies.objects.order_by('-pk')
    context = {'movies':movies}
 
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/create.html')


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        desription = request.POST.get('desription')
        movies = Movies(title=title, title_en=title_en,
        audience=audience, open_date=open_date, genre=genre,
        watch_grade=watch_grade, score=score, poster_url=poster_url,
        desription=desription)
        movies.save()
        return redirect('movies:index')

  

def detail(request, movies_pk):
    movies = Movies.objects.get(pk=movies_pk)
    context = {'movies': movies }
    return render(request, 'movies/detail.html', context)


def edit(request, movies_pk):
    movies = Movies.objects.get(pk=movies_pk)
    context = {'movies': movies }
    return render(request, 'movies/update.html', context)

def update(request, movies_pk):
    if request.method == 'POST':
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        desription = request.POST.get('desription')
        movies = Movies(title=title, title_en=title_en,
        audience=audience, open_date=open_date, genre=genre,
        watch_grade=watch_grade, score=score, poster_url=poster_url,
        desription=desription)
        movies.save()
        return redirect('movies:index')

def delete(request, movies_pk):
    movies = Movies.objects.get(pk=movies_pk)
    movies.delete()
    return redirect('movies:index')
