from django.db import models


class Actor(models.Model):
    first_name = models.CharField("Cast Name", max_length=255)

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        ordering = ("first_name",)


class Category(models.Model):
    genre = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.genre

    class Meta:
        verbose_name_plural = "categories"


class MovieCode(models.Model):
    movie_code = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.code)


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

    poster = models.ImageField(upload_to="movies/images", blank=True, null=True)

    # video = models.FileField(upload_to="movies/videos")
    # Just to pass null errors at first
    actors = models.ManyToManyField(Actor, blank=True, null=True)
    movie_code = models.OneToOneField(
        MovieCode, blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    review = models.TextField(blank=True, null=True)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.review
