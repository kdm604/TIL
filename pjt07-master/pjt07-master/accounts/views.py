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