from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    naam = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.naam

class Subgenre(models.Model):
    naam = models.CharField(max_length=100, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="subgenres")

    def __str__(self):
        return f"{self.naam} ({self.genre.naam})"

class Film(models.Model):
    naam = models.CharField(max_length=255)
    jaar = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="films")
    subgenre = models.ForeignKey(Subgenre, on_delete=models.SET_NULL, null=True, blank=True, related_name="films")

    def __str__(self):
        return self.naam

class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="reviews")
    gebruiker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    verhaal = models.TextField()
    acteurs = models.TextField()
    visuals = models.TextField(null=True, blank=True)
    audio = models.TextField(null=True, blank=True)
    extra = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Review of {self.film.naam} by {self.gebruiker.username}"
