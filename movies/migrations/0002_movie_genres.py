# Generated by Django 4.1.2 on 2022-10-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("genres", "0002_remove_genre_movies"),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(related_name="movies", to="genres.genre"),
        ),
    ]
