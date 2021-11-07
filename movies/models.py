from django.db import models

# Create your models here.
class Category(models.Model):
    genre = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.genre

class Actor(models.Model):
    name = models.CharField("Cast Name", max_length=255)

    def __str__(self) -> str:
        return self.name

class Movie(models.Model):  # My table in the database

    # slug = models.SlugField()
    active = models.BooleanField(default=True)

    name = models.CharField("Movie Name", max_length=255, unique=True)

    description = models.TextField(verbose_name="Movie Description")

    likes = models.IntegerField(default=0, null=True)

    watch_count = models.IntegerField(default=0, null=True)

    rate = models.PositiveIntegerField(default=0, null=True)

    production_date = models.DateField(null=True, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)

    modification_date = models.DateTimeField(auto_now=True)

    poster = models.ImageField(upload_to="movies/images", blank=True)

    # video = models.FileField(upload_to="movies/videos")

    def __str__(self) -> str:
        return self.name
