from django.views.generic import TemplateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Film, Review
from .forms import FilmForm, ReviewForm

# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    login_url = "/login/"
    redirect_field_name = "next"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query', '')  # Get the search query from the request
        if query:
            # If there's a search query, filter films by name or year
            films = Film.objects.filter(naam__icontains=query)
        else:
            # If no query, just get all films
            films = Film.objects.all()

        context['films'] = films
        return context
    
class FilmDetailView(LoginRequiredMixin, DetailView):
    model = Film
    template_name = "film_detail.html"
    context_object_name = "film"
    login_url = "/login/"
    redirect_field_name = "next"

class FilmCreateView(LoginRequiredMixin, CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'film_form.html'
    success_url = reverse_lazy('home')  # Redirect to home after successfully adding the film
    login_url = "/login/"
    redirect_field_name = "next"

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_form.html'
    login_url = "/login/"
    redirect_field_name = "next"

    def get_context_data(self, **kwargs):
        # Get the film from the URL
        film = get_object_or_404(Film, pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['film'] = film
        return context

    def form_valid(self, form):
        # Set the film based on the URL parameter
        film = get_object_or_404(Film, pk=self.kwargs['pk'])
        form.instance.film = film
        form.instance.gebruiker = self.request.user  # Set the current user as the reviewer
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the film detail page after submitting the review
        return reverse_lazy('film_detail', kwargs={'pk': self.object.film.pk})