from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    profile_path = models.CharField(max_length=100, null=True)


class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    profile_path = models.CharField(max_length=100, null=True)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=100)
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor, related_name='movies')
    watched_users = models.ManyToManyField(User, related_name='watching_movies')


class Review(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(User, through='Like', related_name='liking_reviews')


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    is_seen = models.BooleanField(null=True)
    created_at = models.DateField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)