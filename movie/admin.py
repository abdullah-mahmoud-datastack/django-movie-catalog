from django.contrib import admin
from .models import Movie, Actor


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "content_type", "year", "description")
    ordering = ('title', 'date')
    filter_horizontal = ('actor',) # list_filter = ["actor"]
    search_fields = ("title", "year")
    list_filter = ["content_type"]


class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    ordering = ['name', 'date']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
