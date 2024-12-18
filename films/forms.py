
from django import forms
from .models import Film, Genre, Review, Subgenre

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['naam', 'jaar', 'genre', 'subgenre']
        widgets = {
            'genre': forms.Select(),
            'subgenre': forms.Select(),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'verhaal', 'acteurs', 'visuals', 'audio', 'extra']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }