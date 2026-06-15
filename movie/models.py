from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    actor_img = models.ImageField(upload_to='actor_image/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


CONTENT_TYPES = [
    ("film", "Film"),
    ("tv_show", "TV Show"),
]

class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    year = models.IntegerField(default=20, blank=True, null=True)
    content_type = models.CharField(
        max_length=20,
        choices=CONTENT_TYPES,
        default="film"
    )
    movie_img = models.ImageField(upload_to='movie_image/')
    actor = models.ManyToManyField(Actor, related_name="movie_actors")
    link = models.URLField(max_length=650, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
