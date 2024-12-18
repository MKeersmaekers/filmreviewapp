# reviews/urls.py

from django.urls import path
from . import views
from films.views import FilmCreateView, FilmDetailView, Home, ReviewCreateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

urlpatterns = [
    # Register a new user

    # path('register/', 
    #      CreateView.as_view(
    #          template_name='registration/register.html',
    #          form_class=UserCreationForm,
    #          success_url=reverse_lazy('login')
    #      ), 
    #      name='register'),

    # Login
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Logout
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    # Password Reset
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', Home.as_view(), name='home'),
    path('film/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('add-film/', FilmCreateView.as_view(), name='add_film'),
    path('film/<int:pk>/add-review/', ReviewCreateView.as_view(), name='add_review'),
]
