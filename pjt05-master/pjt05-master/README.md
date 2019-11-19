# pjt05 



```
1번 요구사항
movie라는 클래스에 요구하는 정보사항들을 저장할수 있게 models.py 작성

from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20)
    audience = models.IntegerField()
    open_date = models.DateTimeField(auto_now=False)
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    desription = models.TextField()

```

```
2번 요구사항


*영화목록 페이지*
views.py 에서
def index(request):
    movies = Movies.objects.order_by('-pk')
    context = {'movies':movies}
인덱스 함수를 만들고 index.html 파일에 영화 이름과 평점만을 보이게 영화목록 페이지를 작성

{% extends 'base.html' %}

{% block body %}
    <a href="{% url 'movies:new' %}">새 영화 등록</a>
    <h2 class="text-center">영화 목록</h2>
    {% for movie in movies %}
        <p>영화 제목: <a href="{% url 'movies:detail' movie.pk%}">{{ movie.title }}</a></p>
        <p>영화 평점: {{ movie.score }}</p>
        <hr>
    {% endfor %}
  
{% endblock %}
```

```

*영화 정보 생성*

new - create 함수와 create.html 파일을 통해 영화 정보를 입력받음

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
        
     
{% extends 'base.html' %}

{% block body %}
    <h2 class="text-center">영화 정보 생성</h2>
    <form action="{% url 'movies:create' %}" method="POST">
        {% csrf_token %}
        <label for="title">영화명</label>
        <input type="text" name="title" id="title"><br>
        <label for="title_en">영화명(영문)</label>
        <input type="text" name="title_en" id="title_en"><br>
        <label for="audience">누적 관객수</label>
        <input type="number" name="audience" id="audience"><br>
        <label for="open_date">개봉일</label>
        <input type="date" name="open_date" id="open_date"><br>
        <label for="genre">장르</label>
        <input type="text" name="genre" id="genre"><br>
        <label for="watch_grade">관람 등급</label>
        <input type="text" name="watch_grade" id="watch_grade"><br>
        <label for="score">평점</label>
        <input type="number" step="0.01" name="score" id="score"><br>
        <label for="poster_url">포스터 이미지 URL</label>
        <input type="text" name="poster_url" id="poster_url"><br>
        <label for="desription">영화소개</label>
        <textarea name="desription" id="desription" cols="30" rows="5"></textarea><br>
        <input type="submit" value="글 작성">
    </form>
    <hr>
    <a href="{% url 'movies:index' %}">[목록]</a>

{% endblock %}


```



```
*영화 정보 조회*

def detail(request, movies_pk):
    movies = Movies.objects.get(pk=movies_pk)
    context = {'movies': movies }
    return render(request, 'movies/detail.html', context)
    
{% extends 'base.html' %}
{% block body %}

<h2 class="text-center">영화 정보 조회</h2>
<hr>
<p>영화 제목: {{ movies.title }}</p>
<p>영화 제목(영문): {{ movies.title_en }}</p>
<p>누적 관객수: {{ movies.audience }}</p>
<p>영화 개봉일: {{ movies.open_date }}</p>
<p>영화 장르: {{ movies.genre }}</p>
<p>관람 등급: {{ movies.watch_grade }}</p>
<p>평점: {{ movies.score }}</p>
<p>포스터 이미지: {{ movies.poster_url }}</p>
<p>영화 소개: {{ movies.desription }}</p>



<a href="{% url 'movies:index' %}">[목록]</a> <br>
<a href="{% url 'movies:edit' movies.pk %}">[수정]</a><br>
<a href="{% url 'movies:delete' movies.pk %}">[삭제]</a><br>
{% endblock %}

영화 정보 조회 페이지에서 목록or수정or삭제가 가능하게 링크를 걸고
링크를 클릭하면 해당 url로 이동하게 만듬
```

```
*영화 정보 수정*
edit - update 함수를 통해서 영화 정보를 수정
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

{% extends 'base.html' %}

{% block body %}
    <h2 class="text-center">영화 정보 수정</h2>
    <form action="{% url 'movies:update' movies.pk %}" method="POST">
        {% csrf_token %}
        <label for="title">영화명</label>
        <input type="text" name="title" id="title" value="{{movies.title}}"><br>
        <label for="title_en">영화명(영문)</label>
        <input type="text" name="title_en" id="title_en" value="{{movies.title_en}}"><br>
        <label for="audience">누적 관객수</label>
        <input type="number" name="audience" id="audience" value="{{movies.audience}}"><br>
        <label for="open_date">개봉일</label>
        <input type="date" name="open_date" id="open_date"value="{{movies.open_date|date:"Y-m-d" }}"><br>
        <label for="genre">장르</label>
        <input type="text" name="genre" id="genre" value="{{movies.genre}}"><br>
        <label for="watch_grade">관람 등급</label>
        <input type="text" name="watch_grade" id="watch_grade" value="{{movies.watch_grade}}"><br>
        <label for="score">평점</label>
        <input type="number" step="0.01" name="score" id="score" value="{{movies.score}}"><br>
        <label for="poster_url">포스터 이미지 URL</label>
        <input type="text" name="poster_url" id="poster_url" value="{{movies.poster_url}}"><br>
        <label for="desription">영화소개</label>
        <textarea name="desription" id="desription" cols="30" rows="5">{{movies.desription}}</textarea><br>
        <input type="submit" value="글 작성">
    </form>
    <hr>
    <a href="{% url 'movies:index' %}">[메인 페이지]</a>

{% endblock %}

개봉일을 넘길때는 {{movies.open_date|date:"Y-m-d" }} 요렇게 넘겨야됨
```

```
*영화 삭제*
영화 정보 조회 페이지에서 삭제를 누르면 url을 통해 views.py 에서 딜리트 함수를 실행
def delete(request, movies_pk):
    movies = Movies.objects.get(pk=movies_pk)
    movies.delete()
    return redirect('movies:index')
    
삭제가 되면 리다이렉트를 통해 영화 목록페이지로 이동하게 만듬
```

