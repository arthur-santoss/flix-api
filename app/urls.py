from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetriveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetriveUpdateDestroy
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name='genre_create_list'),
    path('genres/<int:pk>/', GenreRetriveUpdateDestroyView.as_view(), name='genre-detail-view'),

    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetriveUpdateDestroy.as_view(), name='actor-detail-view'),

    path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view')

    
]
