from django import forms
from django.shortcuts import redirect, render
from .models import Movie
from .forms import MovieForm


def index(request):
    all_movies = Movie.objects.all()
    print(request)
    return render(request, "movies/index.html", context={"movies": all_movies})


def show_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, "movies/movie_details.html", context={"movie": movie})


def add_movie(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("movies:index")

    return render(request, "movies/add_movie.html", context={"form": form})


def edit_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if request.method == "POST":
        form = MovieForm(data=request.POST, files=request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movies:movie-details", pk=movie.id)

    return render(
        request, "movies/edit_movie.html", context={"form": form, "movie": movie}
    )


def delete_movie(request, pk):
    Movie.objects.get(id=pk).delete()
    return redirect("movies:index")
