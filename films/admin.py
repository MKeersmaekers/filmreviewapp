from django.contrib import admin
from .models import Film, Review, Genre, Subgenre

# Register your models here.

admin.site.register(Genre)
admin.site.register(Subgenre)
admin.site.register(Film)
admin.site.register(Review)