from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    year = [i for i in range(1950, 2021)]
    open_date = forms.DateField(
        widget=forms.SelectDateWidget(years=year),
   )
    
    score = forms.NumberInput(
        attrs={
            'step':'0.01',
        }
    )
    class Meta:
        model = Movie
        fields = ('title', 'title_en', 'audience', 'open_date', 'genre', 'watch_grade','score','poster_url','description',)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('score', 'content' ,)