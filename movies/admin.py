from django.contrib import admin
from movies.models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'get_actors', 'resume')

    @admin.display(description='Actors')
    def get_actors(self, obj):
        return ", ".join([actor.name for actor in obj.actors.all()])