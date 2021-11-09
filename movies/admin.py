from django.contrib import admin
from movies.models import Actor, Category, MovieCode, Movie, Review


class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "likes", "rate", "like_to_watch_ratio")
    ordering = ("name",)
    search_fields = ("name",)

    def like_to_watch_ratio(self, obj):
        if obj.watch_count == 0:
            return "Not enough watch count"
        else:
            return f"{(obj.likes / obj.watch_count) * 100:.0f}%"


admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(MovieCode)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
