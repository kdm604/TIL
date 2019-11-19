# pjt07 - 19|11|01



## 요구 사항 1. 데이터베이스 설계

```python
movies-models.py 에 Genre,Movie,Review 모델 만들기.

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Genre(models.Model):
    name = models.CharField(max_length=40)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=300)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies", blank=True)

class Review(models.Model):
    content = models.CharField(max_length=40)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
```



## 요구 사항 2. Seed Data 반영 

```
아래의 명령어로 주어진 genre.json, movie.json 을 movie/fixtures 디렉토리로 옮김
$ python manage.py loaddata genre.json
Installed 11 object(s) from 1 fixture(s)
$ python manage.py loaddata movie.json
Installed 10 object(s) from 1 fixture(s)
```



## 요구 사항 3. accounts App

```
*** crud/templates/base.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>

    
    <div class="container">
        <a href="{% url 'movies:index' %}" class="mx-2">메인</a>
        <a href="{% url 'accounts:users' %}" class="mx-2">사용자목록</a>
        <a href="{% url 'accounts:signup' %}" class="mx-2"> signup </a>
        <a href="{% url 'accounts:login' %}" class="mx-2"> login </a>
        <a href="{% url 'accounts:logout' %}" class="mx-2"> logout </a>
    
        <h1 class="text-center">PJT07</h1>
        {{request.user}}
        {% block body %}
        {% endblock %}
    </div>



    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```



```
유저 회원가입과 로그인, 로그아웃 기능을 구현해야 합니다.

*** accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model


def users(request):
    User = get_user_model()
    users = User.objects.all()
    context = {'users': users ,}
    return render(request, 'users.html', context)


def user_detail(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    reviews = user.review_set.all()
    movies = user.like_movies.all()
    context = {
        'user': user,
        'reviews': reviews,
        'movies': movies,        
    }
    return render(request, 'user_detail.html', context)



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = UserCreationForm()
    context = {'form': form ,}
    return render(request, 'auth_form.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {'form': form ,}
    return render(request, 'auth_form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')



*** accounts/templates/auth.form.html
{% extends 'base.html' %}

{% block body %}
    <h2>회원가입</h2>
    <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="submit">
    </form>
{% endblock %}


*** accounts/templates/user_detail.html
{% extends 'base.html' %}

{% block body %}
    <p>사용자: {{ user.username }}</p>
    <p>
    <h5>평점 목록</h5>
    {% for review in reviews %}
      <ul>
        <li>{{ review.score }}점 - {{ review.content }}</li>
      </ul>
    {% endfor %}
    <hr>
    <h5>좋아요한 영화</h5>
    </p>
    {% for like_movie in movies %}
      <ul>
        <li>{{ like_movie.title }}</li>
      </ul>
    {% endfor %}
  
{% endblock %}


*** accounts/templates/users.html

{% extends 'base.html' %}

{% block body %}
    {% for user in users %}
        <a href="{% url 'accounts:user_detail' user.pk %}">
        <p>사용자: {{ user.username }}</p>
        </a>
        

    {% endfor %}


{% endblock %}
```



## 요구 사항 4. movies App

```
Genre와 영화는 생성/수정/삭제를 만들지 않습니다. 단, 관리자를 위하여 관리자 계정과 함께 관리자 페
이지를 생성합니다


*** movies/views.py

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
   
 
 *** movies/templates/index.html
 {% extends 'base.html' %}

{% block body %}
    <h2 class="text-center">INDEX</h2>
    {% for movie in movies %}
        <p><b>영화제목: {{ movie.title }}</b></p>

        <a href="{% url 'movies:detail' movie.pk %}">
            <img src="{{ movie.poster_url }}" alt="{{ movie.title }}" width="200px">
        </a>
        <P><a href="{% url 'movies:like' movie.pk %}">좋아요!!</a></P>
        <p>{{ movie.like_users.all | length }} 명이 좋아합니다.</p>
        <hr>
    {% endfor %}

{% endblock %}


*** movies/templates/detail.html

{% extends 'base.html' %}

{% block body %}
    <h2 class="text-center">DETAIL</h2>
    <p>영화명: {{ movie.title }}</p>
    <p>누적 관객수: {{ movie.audience }}</p>
    <p>포스터 이미지 URL: {{ movie.poster_url }}</p>
    <p>영화 소개: {{ movie.description }}</p>
    <p>장르: {{ movie.genre_id }}</p>

    <hr>
    <form action="{% url 'movies:create_review' movie.pk %}" method='POST'>
    {% csrf_token %}
    {{ review_form.as_p}}
    <input type="submit" value="submit">
    </form>
    <hr>
    {% for review in reviews %}
        <p>작성자: {{ review.user }}</p>
        <p>평점: {{ review.score }} / 리뷰: {{ review.content }}</p>
        
        <form action="{% url 'movies:delete_review' movie.pk review.pk %}" method="POST">
            {% csrf_token %} 
            {% if review.user == request.user %}
                <input type="submit" value="삭제">
            {% endif %}
        </form>
    {% endfor %}

{% endblock %}
```



## 권대민's Comment

```
프로젝트를 페어로 진행하면서 드라이버와 네비게이터를 구분해서 각자의 역할을 수행할때 프로젝트를 진행 함에 있어서 더 탄력적인 진행이 가능한 것 같다. 특히 네비게이터가 되었을때 명세에서 원하는 기능을 어떻게 구현해야하는지를 드라이버에게 알려줄 때 코드를 외우는 것이 아니라 이해하며 넘어가야 되겠다고 다시 한번 느꼈다.
그리고 드라이버와 네비게이터 둘다 모르는 것이 발생했을때 같이 구글링을 통해 답을 찾아냈을 때 머리속에 더 선명하게 각인 되는 것 같았다. 
페어 프로젝트를 하면서 어려웠던 점은 네비게이터 역할을 수행할 때 드라이버가 모르는 것이 발생 했을때 바로 정답을 말해주지 않고 질문을 통해 드라이버 스스로 답을 찾게 하는것이 쉽지 않았다. 드라이버뿐만 아니라 네비게이터도 확실하게 이해를 하고 질문을 해야 드라이버가 답을 찾을수 있을것 같다.
```



## 서혜영's Comment

```
혼자 프로젝트를 진행할때는 스스로 모든 것을 구현해야해서 부담도 크고 힘든 순간(?)이 왔을 때 그냥 그저 진짜 힘들었다. 하지만 팀으로 프로젝트를 진행하니 내가 모르는 것을 옆사람은 알고 있어서 힘이 되고 도움이 되는 부분이 있었고, 옆사람도 함께 몰라서 더 힘든 순간(?)이 오기도 했다. 하지만 우리에겐 구글이 있었고 어려움을 극복할 수 있었다.
'백지장도 맞들면 낫다.'라는 속담을 몸소 체험하는 소중한 시간이었다!! 개인적으로는 혼자서 하는 프로젝트보다 함께하는 프로젝트가 좀 더 재미있게 할 수 있었고, 실력 향상에 더 도움이 되는 것 같다.
```



