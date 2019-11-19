from django import forms
from .models import Movie, Genre, Review


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)



class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'audience', 'poster_url', 'description',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content', 'score', )
