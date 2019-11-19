##	pjt06 프로젝트

```
1) 요구사항-데이터베이스
영화에 대한 정보를 저장할 모델과 한줄평을 저장할 모델을 models.py에 작성
forms.py에 모델폼을 작성
```

```
2) 요구사항-페이지


영화목록 페이지
{% extends 'movies/base.html' %}
{% load static %}


{% block b %}

    <h1 class="text-center">영화 목록</h1>
    <img src="{% static '컨져링.jpg'%}" alt="컨져링"><br>
    <hr>
    <form action="{% url 'movies:create' %}" method="GET">
            <input type="submit" value="글 생성" class="btn btn-primary">
    </form>
    <hr>
    {% for movie in movies %}
        <a href="{% url 'movies:detail' movie.pk %}"><p>영화 제목: {{ movie.title }}</p></a>
        
        <p>영화 평점: {{ movie.score }}</p>
        <hr>
    {% endfor %}
    
{% endblock %}

static 을 통해 영화이미지를 영화목록 페이지에 뛰움
```

```
영화정보조회 페이지

{% extends 'movies/base.html' %}

{% block b %}
    <h1 class="text-center">영화 정보조회</h1>
    <p>영화 제목: {{ movie.title }}</p>
    <p>영화 제목(영문): {{ movie.title_en }}</p>
    <p>누적 관객수 : {{ movie.audience }}</p>
    <p>영화 개봉일: {{ movie.open_date }}</p>
    <p>영화 장르: {{ movie.genre }}</p>
    <p>영화 관람등급: {{ movie.watch_grade }}</p>
    <p>영화 평점: {{ movie.score }}</p>
    <p>영화 포스터: {{movie.poster_url }}</p>
    <p>영화 소개: {{ movie.description }}</p>
    <hr>


    {% for comment in comments %}
        <p>평점: {{ comment.score }} 한줄평: {{ comment.content }}</p>
        <hr>
    {% endfor %}
        
    <form action="{% url 'movies:comments_create' movie.pk %}" method="POST">
        {% csrf_token %}
        {{ comment_form }}
        <input type="submit" value="댓글 작성" class="btn btn-primary">
    </form>
    
    <form action="{% url 'movies:update' movie.pk %}" method="GET">
        <input type="submit" value="글 수정" class="btn btn-dark">
    </form>
    

    <form action="{% url 'movies:delete' movie.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="글 삭제" class="btn btn-danger">
    </form>

    <form action="{% url 'movies:index' %}" method="GET">
            <input type="submit" value="메인페이지" class="btn btn-primary">
    </form>

    
{% endblock %}


디테일 페이지에서 글수정,글목록,글삭제 링크를 설정하고
디테일 페이지에서 한줄평을 보이게 하고 등록도 가능하게 만듬
```

```
영화 정보 생성 or 수정 페이지

{% extends 'movies/base.html' %}

{% block b %}
    {% if request.resolver_match.url_name == 'create' %}
        <h1 class="text-center">영화 정보 생성</h1>
    {% else %}
        <h1 class="text-center">영화 정보 수정</h1>
    {% endif %}
    <form action="" method="POST">
        {% csrf_token %}
        {{ form.as_p }}


        {% if request.resolver_match.url_name == 'create' %}
            <input type="submit" value="글 작성" class="btn btn-primary">
        {% else %}
            <input type="submit" value="글 수정" class="btn btn-primary">
        {% endif %}
            
    </form>

{% endblock %}
```

```
views.py

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
```

