from django.urls import path
from .views import index,show_movie,add_movie,edit_movie,delete_movie

app_name= 'movies'

urlpatterns = [
    path("", index, name="index"),
    path("<int:pk>/details", show_movie, name="movie-details"),
    path("add/", add_movie, name="add-movie"),
    path("<int:pk>/edit", edit_movie, name="edit-movie"),
    path("<int:pk>/delete", delete_movie, name="delete-movie"),
]
