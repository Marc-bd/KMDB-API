from django.urls import path
from .views import ReviewDetailView, ReviewsViews


urlpatterns = [
    path("movies/<int:movie_id>/reviews/", ReviewsViews.as_view()),
    path("movies/<int:movie_id>/reviews/<int:review_id>/", ReviewDetailView.as_view())
]