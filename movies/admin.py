from django.contrib import admin
from movies.models import Actor, Category, Movie


admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Movie)
