from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Watchable(models.TextChoices):
    MUST_WATCH = "Must watch"
    SHOULD_WATCH = "Should watch"
    AVOID_WATCH = "Avoid watch"
    NO_OPINION = "No opinion"


class Review(models.Model):
    stars = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    review = models.TextField(unique=True)
    spoilers = models.BooleanField(default=False, null=True, blank=True)
    recomendation = models.CharField(
        max_length=50, choices=Watchable.choices, default=Watchable.NO_OPINION
    )

    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    critic = models.ForeignKey("users.User", on_delete=models.CASCADE)


# Create your models here.
