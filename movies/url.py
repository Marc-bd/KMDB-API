from django.urls import path
from .views import MoviesDetailViews, MoviesViews


urlpatterns = [
    path("movies/", MoviesViews.as_view()),
    path("movies/<int:movie_id>/", MoviesDetailViews.as_view())
]