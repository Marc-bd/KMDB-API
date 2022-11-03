from django.db import models


class ReviewChoices(models.TextChoices):
    MUST_WATCH =  "Must Watch" 
    SHOULD_WATCH = "Should Watch"
    AVOID_WATCH = "Avoid Watch"
    NO_OPINION = "No Opinion"

class Review(models.Model): 
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False, null=True)

    recomendation = models.CharField(
        max_length=50,
        choices=ReviewChoices.choices,
        default=ReviewChoices.NO_OPINION
    )

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="review")

    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="review")

   